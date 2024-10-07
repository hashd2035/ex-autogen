import os

from autogen import config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent

assistant_id = os.environ.get("ASSISTANT_ID", None)
config_list = config_list_from_json("OAI_CONFIG_LIST")
llm_config = {
    "config_list": config_list,
}
assistant_config = {
    "tools": [
        {"type": "code_interpreter"},
    ],
    "tool_resources": {
        "code_interpreter": {
            "file_ids": ["$file.id"]  # optional. Files that are passed at the Assistant level are accessible by all Runs with this Assistant.
        }
    }
}
oai_agent = GPTAssistantAgent(
    name="oai_agent",
    instructions="I'm an openai assistant running in autogen",
    llm_config=llm_config,
    assistant_config=assistant_config,
)