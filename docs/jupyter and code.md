There are several ways for a Jupyter notebook to import modules or packages developed in the same folder or in subfolders. Here are some common approaches: [1]

### Direct or relative import

1. Direct import (same folder):
  If your module is in the same folder as the notebook, you can import it directly: [2]

```python
import my_module
```

2. Relative import (subfolders):
  For modules in subfolders, use relative imports: [3]
```python
from .subfolder import my_module
```

3. Add parent directory to sys.path:
  If your module is in a parent directory, you can add it to the Python path:
  
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(''))))
import my_module
```

### USE environment variable
4. Use PYTHONPATH:
  Set the PYTHONPATH environment variable before starting Jupyter:

```sh
> export PYTHONPATH="/path/to/your/module:$PYTHONPATH"
> jupyter notebook
```
   
### Create a package
5. Create a package:
  Turn your folder into a package by adding an __init__.py file, then import it:

```python
from my_package import my_module
```

make sure to restart the kernel if the new module is available

6. Install as editable package:
  If you're developing a package, install it in editable mode:

```sh
> pip install -e /path/to/your/package
```

Then import normally in your notebook.

### %run to run a python directly in the notebook
7. Use %run magic:
  You can run a Python file directly in the notebook:

```jupyter
%run ./my_module.py
```

### Use importlib
7. Use importlib:
Dynamically import modules:

```python
import importlib.util
spec = importlib.util.spec_from_file_location("module_name", "/path/to/file.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
```
---

Remember to restart the kernel after making changes to imported modules to ensure you're using the latest version. Also, be cautious with modifying `sys.path` as it can lead to naming conflicts or unexpected behavior.

When developing modules for use in Jupyter notebooks, it's often helpful to structure your project as a package with a proper `setup.py` or `pyproject.toml` file. This allows for easier management and distribution of your code.

1 https://stackoverflow.com/questions/55443861
2 https://danny.fyi/embedding-jupyter-notebooks-into-your-python-application-bfee5d50e4f8
3 https://medium.com/@rodrigobc10/custom-packages-and-modules-in-python-688547c4f3f6