from autogen import ConversableAgent

from configs import CodeExecutionConfig


class Agent:
    DockerCodeExecutor = ConversableAgent(
        "code_executor_agent_docker",
        llm_config=False,
        code_execution_config=CodeExecutionConfig.docker,
        human_input_mode="ALWAYS",
    ),
    LocalCodeExecutor = ConversableAgent(
        "code_executor_agent_docker",
        llm_config=False,
        code_execution_config=CodeExecutionConfig.local,
        human_input_mode="ALWAYS",
    )