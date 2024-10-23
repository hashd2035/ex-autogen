import os

from dotenv import load_dotenv
load_dotenv()


class LlmConfigs:
    class OpenAi:
        gpt4 = {
            "config_list": [
                {
                    "model": "gpt-4",
                    "temperature": 0.9,
                    "api_key": os.environ.get("OPENAI_API_KEY")
                }
            ]
        }



        
