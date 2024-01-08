import os
import openpyxl as xl
import pandas as pd
from pathlib import Path


def list_dir_content(dirname):
    with os.scandir(dirname) as entries:
        for entry in entries:
            print(entry.name)


def check_dir_exist(dirname):
        pathobject3 = Path(dirname)
        if pathobject3.exists():
            return True
        else:
            return False


def check_file_exist(filenamewithpath):
    return(os.path.exists(filenamewithpath))


def fix_dir_path_name(dirname):
    if dirname[-1] != '\\':
        return dirname + '\\'
    else:
        return dirname

