"""Organize the files in folders following the order of FileInfo.com"""

import os

FILE_TYPE = {
    "text_files": [""]
}


class Organizer:
    """Class to organize the files in folders according to their extension"""

    def __init__(self):
        """Run the functions when the class is constructed"""
        self.__organize_files()

    def __organize_files(self):
        """
        Organize the files according to the their extension
        :return: a list of folders with the files in it
        :rtype: None
        """
