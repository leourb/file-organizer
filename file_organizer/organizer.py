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
            file_path = os.path.join(directory, file)
            file_ext = os.path.splitext(file)[-1]
            if file_ext in list(FileExtensions().file_types().keys()):
                folder = FileExtensions().file_types()[file_ext]
                folder_path = os.path.join(directory, folder)
                if not os.path.isdir(folder_path):
                    os.makedirs(folder_path)
                new_file_path = os.path.join(folder_path, file)
                os.replace(file_path, new_file_path)
                print(f"File {file} moved to folder {folder}\n")
            else:
                unrecognized_files = os.path.join(directory, "Miscellaneous")
                if not os.path.isdir(unrecognized_files):
                    os.makedirs(unrecognized_files)
                new_file_path = os.path.join(unrecognized_files, file)
                os.replace(file_path, new_file_path)
                print(f"File {file} moved to generic folder Miscellaneous\n")
