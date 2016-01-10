# Contributing

## Releasing to PyPi
Follow the guide on https://packaging.python.org/en/latest/distributing/
release ideas: https://gist.github.com/audreyr/5990987

```bash
# ensure twine is installed
$ pip install --upgrade twine bumpversion
# remove previous build
$ rm -rf build dist *.egg-info
# Update changelog
$ git add CHANGELOG.md
$ git commit -m "docs(changelog): Prepare changelog for upcoming release"
# increase the version number
$ bumpversion --commit --tag (major|minor|patch)
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


## TODOs
 - [ ] Handle Docker run errors (see screenshot from 2016-01-10 8:22)
