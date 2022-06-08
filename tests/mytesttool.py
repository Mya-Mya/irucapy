import os
import sys
from pathlib import Path
from typing import Callable

current_directory = Path(os.path.dirname(os.path.abspath(__file__)))
project_directory = current_directory.parent
project_directory_str = str(project_directory)
sys.path.insert(0, project_directory_str)

def testerfunc(tester_function:Callable):
    """
    A decorator for the test function.
    """
    name:str = tester_function.__name__
    def wrapper(*args, **kwargs):
        print()
        print(f"{name:-^20}")
        tester_function(*args, **kwargs)
        print(f"{name:-^20}")
    return wrapper