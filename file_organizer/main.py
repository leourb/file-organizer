"""Main entry file when using directly from commandline"""

import argparse
import os
from .organizer import Organizer


def organize():
    parser = argparse.ArgumentParser()  # let users pass in the directory to organize
    cwd = os.getcwd() 
    # if no args passed in, use current working directory
    parser.add_argument('--dir', type=str, default=cwd, help='Directory to be organised')
    args = parser.parse_args()


    organizer = Organizer(args.dir)

    try:
        organizer.organize_files()
        print("Files are now organised.")
    except Exception as e:
        print(e)
