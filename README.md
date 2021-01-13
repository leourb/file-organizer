# Abstract

The script aims to order a directory of your choosing by reading the file extensions of each file in the dir, create the
folders according to the hierarchy of [FileInfo.com](https://fileinfo.com/browse/) and moving the files in the
corresponding folder.

# Installation

You need to first clone or download all the files in this repo. Once you've done that, then you need a Console to build
the `.whl` package to then simply install with `pip`.

Build the `.whl` following this command:

```commandline
pyhton setup.py bdist_wheel
```

This will create a folder called `dist`, you then need to change the path do `dist` using:

```commandline
cd dist
```

Once inside the folder you can install the package running:

```commandline
pip install file_organizer-1.0.0-py3-none-any.whl
```

# Usage

The script is extremely simple and fast. You can call in your IDE or environment by simply importing it as:

```python
from file_organizer import Organizer

Organizer()
```

As the class is built it will refresh the list of extensions and folders from FileInfo.com and then will ask you to type
a dir to sort. It works on any platform as it uses agnostic conventions from the package `os`.
All the files with unrecognized extensions are placed in a folder called `Miscellaneous`.