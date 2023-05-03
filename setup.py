from os import path, getenv, environ

from dotenv import load_dotenv
from setuptools import setup, find_packages

_ = load_dotenv(dotenv_path='.env', verbose=True, override=True)


def read(fname: str = 'README.md'):
    file_path = path.join(path.dirname(__file__), fname)
    with open(
        file=file_path,
        mode="rt",
        encoding="utf-8"
    )as file_obj:
        data = file_obj.read()
    return data

setup(
    name='overloaded-iterables',
    version='0.7.34',
    description='Overloaded version of the built-in python classes: list and set, to include some extra functionalities.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Prithoo Medhi',
    author_email='prithoo11335@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    url='https://github.com/Arkiralor/overloaded_iterables',
    keywords=[
        "python",
        "built-in overloading",
        "sequence",
        "overloading",
        "median",
        "rms",
        "root-mean-square",
        "mean",
        "sort",
        "graph",
        "histogram",
        "scatterplot",
        "line-plot",
        "queue",
        "stack"
    ],
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    platforms=[
        "windows",
        "ubuntu-linux",
        "mac-os"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License"
    ],
)

if __name__ == "__main__":
    pass
