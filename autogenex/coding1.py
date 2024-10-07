import os
from autogen import ConversableAgent
from agents.CodingAgents import Agent
from prompts import SystemMessages
from dotenv import load_dotenv

load_dotenv()

code_executor_agent = Agent.DockerCodeExecutor
code_writer_agent = ConversableAgent(
    "code_writer_agent",
    system_message=SystemMessages.codingAssistant,
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
    code_execution_config=False,  # Turn off code execution for this agent.
)
chat_result = code_executor_agent.initiate_chat(
    code_writer_agent,
    message="Write Python code to calculate the 14th Fibonacci number.",
)

