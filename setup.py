from os import path
from setuptools import setup, find_packages

def read(fname:str='README.md'):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='overloaded-iterables',
    version='0.6',
    description="Overloaded version of the built-in python classes: list and set to include some extra functionalities.",
    long_description=read(),
    license='MIT',
    author="Prithoo Medhi",
    author_email='prithoo11335@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Arkiralor/overloaded_iterables',
    keywords= [
        'python',
        'built-in overloading',
        'sequence',
        'overloading',
        'median',
        'rms',
        'root-mean-square',
        'mean',
        'sort',
        'graph',
        'histogram',
        'scatterplot',
        'line-plot'
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
        "License :: OSI Approved :: BSD License",
    ],
)

if __name__=="__main__":
    pass