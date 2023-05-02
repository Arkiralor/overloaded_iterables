from os import path
from pathlib import Path


## The path to the directory where the module is located/installed
__ROOT__ = Path(__file__).resolve().parent
__CLASSES__ = path.join(__ROOT__, 'classes.py')

if not path.exists(__ROOT__):
    raise FileNotFoundError(message='The module was not found; was `overloaded-iterables` installed properly?',path=__ROOT__)

if not path.exists(__CLASSES__) or not path.isfile(__CLASSES__):
    raise FileNotFoundError(message='<classes.py> was not found; was `overloaded-iterables` installed properly?',path=__CLASSES__)

if __name__=='__main__':
    print(f"__ROOT__: {__ROOT__}")
    print(f"__CLASSES__: {__CLASSES__}")