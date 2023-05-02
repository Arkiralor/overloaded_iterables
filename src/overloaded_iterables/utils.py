from json import loads
from os import path, environ, getenv

from . import __ROOT__

SPECIAL_CHARS = ['?', '"', '<', '>', '|', '(', ')', '[', ']', '{', '}', '\n', '\t', '\r', '']


def write_env_to_file(file_path:str = None):
    if not file_path:
        file_path = path.join(__ROOT__, '..', '.env')

    data = environ.__dict__.get("_data", {})
    _keys = data.keys()
    lines = []
    for key in _keys:
        for item in SPECIAL_CHARS:
            if item in key:
                key = key.replace(item, '')
        value = data.get(key)
        for item in SPECIAL_CHARS:
            if value and item in value:
                value = value.replace(item, '')

        lines.append(f'{key}="{value}"\n')

    try:
        with open(file=file_path, mode='w+t', encoding='utf-8')as file_obj:
            file_obj.writelines(lines)
    except FileNotFoundError as ex:
        raise ex