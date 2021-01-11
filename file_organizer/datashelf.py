"""Scrape data from FileInfo.com to get file extensions"""

import platform
import requests

from bs4 import BeautifulSoup


class DataShelf:
    """Class to store static data"""

    URLS = {
        "categories": "https://fileinfo.com/browse/",
        "root": "https://fileinfo.com%s"
    }

    def __init__(self):
        """Initialize the class"""
        self.__urls = DataShelf.URLS
        self.__os = platform.system()

    def urls(self):
        """
        Returns the urls in stored in the class
        :return: a dictionary of urls
        :rtype: dict
        """
        return self.__urls


class FileExtensions:
    """Get the file extensions from FileInfo.com"""

    def __init__(self):
        self.__collections = self.__get_collections()
        self.__file_extensions = self.__get_file_extensions()

    def __get_collections(self):
        """
        Parse the page to gather the collections
        :return: the collections on FileInfo.com
        :rtype: dict
        """
        collections = requests.get(DataShelf().urls().get("categories")).text
        parsed_page = BeautifulSoup(collections, "html.parser")
        tags = parsed_page.find("div", {"class": "category"}).findAll("a")
        categories = dict()
        for element in tags:
            category = element.get_text()
            link = element.get("href")
            categories[category] = link
        return categories

    def __get_file_extensions(self):
        """
        Build a data structure with the file types stored inside each category
        :return: a dictionary with the pair ["file_type": "category"]
        :rtype: dict
        """
        results = dict()
        for category in list(self.__collections.keys()):
            url = DataShelf().urls().get("root") % self.__collections[category]
            page = requests.get(url).text
            parsed_page = BeautifulSoup(page, "html.parser")
            rows = parsed_page.findAll("td")
            for row in rows:
                if row.find("a"):
                    results[row.find("a").get_text().lower()] = category
        return results

    def file_types(self):
        """
        Return the file types scraped from FileInfo.com
        :return: a dictionary with all the data types and categories
        :rtype: dict
        """
        return self.__file_extensions
