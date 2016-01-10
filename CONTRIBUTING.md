# Contributing

## Releasing to PyPi
Follow the guide on https://packaging.python.org/en/latest/distributing/

```bash
# ensure twine is installed
$ pip install --upgrade twine bumpversion
# remove previous build
$ rm -rf build dist *.egg-info
# increase the version number
bumpversion --commit --tag (major|minor|patch)
# generate package info used for the upload to the PyPi registry
$ python setup.py egg_info
# build the project
$ python setup.py bdist_wheel --universal
# ensure that a ~/.pypirc file exists
$ cat ~/.pypirc
# upload
$ twine upload dist/*
```

## Symlinking cloned repository
pip install -e .
