python setup.py sdist
twine check dist/*
twine upload dist/* --verbose --username=$PYPI_USERNAME --password=$PYPI_PASSWORD