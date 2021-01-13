# Abstract

The script aims to order a directory of your choosing by reading the file extensions of each file in the dir, create the
folders according to the hierarchy of [FileInfo.com](https://fileinfo.com/browse/) and moving the files in the
corresponding folder.

# Installation
 - Clone or download all the files in this repo. 
 - ```cd``` into the downloaded directory.
 - Run ``` pip install .``` in the command line, this installs the module along with all required packages.

# Usage
From commandline run ```organize``` to organize your current working directory.

If a specific directory is to be organized, ```cd``` into the directory or simply pass in the directory path
to the ```organize``` by passing in ```--dir``` argument. For example:

```organize --dir C:\Users\...\random\folder\```

As the class is built it will refresh the list of extensions and folders from FileInfo.com and then will organize the dir passed. It works on any platform as it uses agnostic conventions from the package `os`.
All the files with unrecognized extensions are placed in a folder called `Miscellaneous`.

# TODO
- [ ] Test ```organize``` command to path on all OS, testing it on virtual environment and OS X on MacOS works just fine. 