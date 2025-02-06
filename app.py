from flask import Flask, request, jsonify
import datetime
import json
import logging
from database import conn, cursor
from ai_client import call_ai_model
from messenger_client import send_response_to_client
from config import LOG_FILE,MESSAGE_INTERVAL_SECONDS

app = Flask(__name__)
logging.basicConfig(filename=LOG_FILE, level=logging.ERROR)

def get_user_and_validate(user_media_id, user_media):
    try:
        cursor.execute(
            "SELECT id, daily_credits, total_credits, last_message_at FROM users WHERE media_id = %s AND media = %s",
            (user_media_id, user_media)
        )
        user = cursor.fetchone()

        if not user:
            cursor.execute("INSERT INTO users (media_id, media, daily_credits, total_credits) VALUES (%s, %s, 10, 0) RETURNING id, daily_credits, total_credits",
                           (user_media_id, user_media))
            user = cursor.fetchone()
            conn.commit()

        user_id, daily_credits, total_credits, last_message_at = user

        # بررسی فاصله زمانی بین پیام‌ها
        if last_message_at:
            last_message_at = last_message_at.replace(tzinfo=datetime.timezone.utc)
            if (datetime.datetime.now(datetime.timezone.utc) - last_message_at).total_seconds() < MESSAGE_INTERVAL_SECONDS:
                return None, "Message too soon"

        # بررسی اعتبار
        if daily_credits <= 0 and total_credits <= 0:
            return None, "No credits left"

        return user, None

    except Exception as e:
        logging.error(f"Database error: {e}")
        return None, "Database error"

@app.route("/receive_message", methods=["POST"])
def receive_message():
    try:
        data = request.get_json()
        message_id, text, reply_to, media_id, media = data["message_id"], data["text"], data["reply_to"], data["media_id"], data["media"]

        user, error_msg = get_user_and_validate(media_id, media)
        if not user:
            return jsonify({"error": error_msg}), 400

        user_id, daily_credits, total_credits, _ = user

        # کاهش اعتبار کاربر
        if daily_credits > 0:
            cursor.execute("UPDATE users SET daily_credits = daily_credits - 1, last_message_at = NOW() WHERE id = %s", (user_id,))
        else:
            cursor.execute("UPDATE users SET total_credits = total_credits - 1, last_message_at = NOW() WHERE id = %s", (user_id,))
        conn.commit()

        # ارسال پیام به مدل هوش مصنوعی
        ai_response, metadata = call_ai_model(text)
        if ai_response is None:
            return jsonify({"error": "AI service unavailable"}), 500

        # ذخیره پیام و پاسخ
        cursor.execute(
            "INSERT INTO messages (message_id, media, user_id, text, ai_response, ai_metadata, created_at) VALUES (%s, %s, %s, %s, %s, %s, NOW())",
            (message_id, media, user_id, text, ai_response, json.dumps(metadata))
        )
        conn.commit()

        # ارسال پاسخ به پیام‌رسان
        success = send_response_to_client(media,media_id, message_id, ai_response)
        if not success:
            return jsonify({"error": "Failed to send response"}), 500

        return jsonify({"response": ai_response}), 200

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
