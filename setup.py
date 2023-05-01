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


name = environ['NAME']
version = environ['VERSION']
description = getenv('DESCRIPTION', '')
long_description_content_type = environ['LONG_DESCRIPTION_CONTENT_TYPE']
author = getenv('AUTHOR')
author_email = environ['AUTHOR_EMAIL']
package_location = environ['FIND_PACKAGES_ARGS']
package_dir = {'': package_location}
url = getenv('URL')
keywords = getenv('KEYWORDS', '').split(',')
classifiers = getenv('CLASSIFIERS', '').split(',')

setup(
    name=name,
    version=version,
    description=description,
    long_description=read('README.md'),
    long_description_content_type=long_description_content_type,
    license='MIT',
    author=author,
    author_email=author_email,
    packages=find_packages(where=package_location),
    package_dir=package_dir,
    url=url,
    keywords=keywords,
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    platforms=[
        "windows",
        "ubuntu-linux",
        "mac-os"
    ],
    classifiers=classifiers,
)

if __name__ == "__main__":
    pass
