"""Organize the files in folders following the order of FileInfo.com"""

import os

from .datashelf import FileExtensions


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
        directory = input("Please type the directory you want to sort: ")
        file_in_dir = os.listdir(directory)
        for file in file_in_dir:
            file_ext = os.path.splitext(file)[-1]
            if file_ext in list(FileExtensions().file_types().keys()):
                folder = FileExtensions().file_types()[file_ext]
                # TODO: Implement logic to check if the folder exist
                # TODO: Implement logic to move files
