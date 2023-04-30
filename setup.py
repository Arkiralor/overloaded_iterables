from setuptools import setup, find_packages


setup(
    name='overloaded-iterables',
    version='0.5.3',
    description="Overloaded version of the built-in python classes: <list> and <set> to include some extra functionalities.",
    long_description="Overloaded version of the built-in python classes: <list> and <set> to include some extra functionalities such as"\
        "<class>.mean(), <class>.rms(), <class>.raise_to(), etc.",
    license='MIT',
    author="Prithoo Medhi",
    author_email='prithoo11335@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Arkiralor/overloaded_iterables',
    keywords= [
        'python',
        'sequence',
        'overloading',
        'median',
        'rms',
        'root-mean-square',
        'mean',
        'sort'
    ],
    install_requires=[],
)