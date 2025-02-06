import requests
import json
import logging
from config_integration import AI_PROVIDER, METIS_OPENAI_KEY

def call_ai_model(prompt):
    try:
        # برای این مرحله لازم نیست با ai وصل بشه
        # url, headers, payload = None, None, None

        # if AI_PROVIDER == "METIS-OPENAI":
        #     url = "https://api.openai.com/v1/chat/completions"
        #     headers = {"Authorization": f"Bearer {METIS_OPENAI_KEY}"}
        #     payload = {"model": "gpt-4", "messages": [{"role": "user", "content": prompt}]}
        # else:
        #     url = "https://api.deepseek.com/v1/chat/completions"
        #     headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
        #     payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}

        # response = requests.post(url, headers=headers, json=payload)
        # data = response.json()
        # return data["choices"][0]["message"]["content"], data.get("usage", {})
        return "test", {}

    except Exception as e:
        logging.error(f"AI request failed: {e}")
        return None, None