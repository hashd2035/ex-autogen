# Poetry project

## If poetry or pyenv aren't installed

1. Install pipx: `python3 -m pip install --user pipx`
2. Install poetry and pyenv using pipx: `pipx install poetry pyenv`
   - pipx is used because it creates isolated environments for each package, preventing conflicts and ensuring a clean setup.
3. Verify installations:
```
    poetry --version
    pyenv --version
```
4. Shell integration:
- Poetry: `poetry config virtualenvs.in-project true`
- pyenv: `echo 'eval "$(pyenv init --path)"' >> ~/.zshrc` (or ~/.bashrc for bash)`

## If poetry project isn't created

1. Set up pyenv: `pyenv install 3.10.6` (or desired Python version)
2. Create project: `poetry new my-project`
3. Change Python version: `pyenv local 3.10.6` (or desired version)
4. Activate environment: `poetry shell`

An environment is an isolated Python installation, managed by poetry. 
Activating it ensures the correct dependencies and Python version are used.

5. To activate the environment automatically: 
   `echo 'eval "$(poetry env install --quiet)"' >> ~/.zshrc` (or ~/.bashrc for zsh)

## If poetry project is already there

Check if `pyproject.toml` exists in the project directory. If so, it's a poetry project.

# Conda and Poetry

1. Create a conda environment: `conda create -n my-env python=3.10`
2. Activate the environment: `conda activate my-env`
3. Install poetry: `pip install poetry`
4. Create a poetry project: `poetry new my-project`
5. Activate the poetry environment: `poetry shell`

Now, you can use both conda and poetry within the same environment. 
- Conda manages the base Python installation, while poetry handles project dependencies and virtual environments.

Refer to the provided link for more detailed information and best practices.
https://blog.stackademic.com/conda-and-poetry-a-harmonious-fusion-8116895b6380&ved=2ahUKEwibju7Qw-aIAxVQJTQIHZ_zNZYQFnoECBUQAw&usg=AOvVaw3logA45pe-81QyFZMrThKr


## Poetry Shell and Poetry Run
In a Poetry project, the first thing you typically need to do is install the project dependencies. You don't necessarily have to run poetry shell first. Here's a breakdown:

    First step: Install dependencies Run: poetry install This command reads your pyproject.toml file and installs all specified dependencies into the project's virtual environment.

    About poetry shell:
        poetry shell activates the project's virtual environment in a new shell session.
        It's not mandatory to run this before working on your project.

    If you forget to run poetry shell:
        You can still use poetry run to run commands within the project's virtual environment.
        For example: poetry run python your_script.py

    Alternatives to poetry shell:
        Use poetry run before each command.
        Or, activate the virtual environment manually:

        source $(poetry env info --path)/bin/activate

        (On Windows, use Scripts\activate.bat instead of bin/activate)

    Best practice:
        Run poetry install when you first clone the project or after updating pyproject.toml.
        Use poetry shell or poetry run when working on the project to ensure you're using the correct environment.

Remember, if you're not in the poetry shell or using poetry run, you might accidentally use system-wide Python and packages instead of your project's isolated environment.

