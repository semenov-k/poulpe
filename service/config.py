import os
import pathlib


CONFIG = {
    'tasks': {
        'root': str(pathlib.Path(os.getcwd()).parent / 'tasks')
    },
    'sqlite':{
        'path': str(pathlib.Path(os.getcwd()).parent / 'db'/ 'tasks.db')
    }
}