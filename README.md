**Steps to reproduce the error**

* Install python 3.6.15
* create a virtual environment and activate it
```
    python -m venv venv
    source venv/bin/activate
```
* Upgrade pip and setuptools
```
pip install --upgrade pip setuptools
```
* install the package `mypkg`
```
pip install .
```
* run pytest with the typeguard plugin
```
pytest --typeguard-packages=mypkg
```
