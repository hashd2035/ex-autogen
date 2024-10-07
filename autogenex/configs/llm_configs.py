import os

from dotenv import load_dotenv
load_dotenv()


class llm_configs:
    class open_ai:
        gpt4 = {
            "config_list": [
                {
                    "model": "gpt-4",
                    "temperature": 0.9,
                    "api_key": os.environ.get("OPENAI_API_KEY")
                }
            ]
        }

        
