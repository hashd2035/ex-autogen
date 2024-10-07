import datetime
import os
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

from prompts import SystemMessages
from dotenv import load_dotenv

load_dotenv()


# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir="artifacts",  # Use the temporary directory to store the code files.
)

# Create an agent with code executor configuration.
code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={"executor": executor},  # Use the local command line code executor.
    human_input_mode="ALWAYS",  # Always take human input for this agent for safety.
)

code_writer_agent = ConversableAgent(
    "code_writer_agent",
    system_message=SystemMessages.codingAssistant,
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
    code_execution_config=False,  # Turn off code execution for this agent.
)

today = datetime.datetime.now().strftime("%Y-%m-%d")
chat_result = code_executor_agent.initiate_chat(
    code_writer_agent,
    message=f"""Today is {today}. Write Python code to extract meta data for amazon detail page 
        (https://www.amazon.com/ELEMIS-Pro-Collagen-Oxygenating-Night-Anti-wrinkle/dp/B00175YVOS/)
        Example of metadata are
        - price: 118.98
        - Brand: Elemis
        - Premium Brand Source: True
        - Title: "ELEMIS Pro-Collagen Night Cream | Ultra Rich Daily Face Moisturizer Firms, Smoothes and Replenishes the Skin with Antioxidants", 
        Run the python code and save the results to csv
        """)