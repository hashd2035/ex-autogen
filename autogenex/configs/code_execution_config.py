import os
from autogen.coding import DockerCommandLineCodeExecutor, LocalCommandLineCodeExecutor
from dotenv import load_dotenv
load_dotenv()


class CodeExecutionConfig:
    local = {
        "executor": LocalCommandLineCodeExecutor(
            timeout=10,  # Timeout for each code execution in seconds.
            work_dir="artifacts",  # Use the temporary directory to store the code files.
        )
    },
    docker = {
         "executor": DockerCommandLineCodeExecutor(
                image="python:3.12-slim",  # Execute code using the given docker image name.
                timeout=10,  # Timeout for each code execution in seconds.
                work_dir="artifacts",  # Use the temporary directory to store the code files.
         )
    }