"""
Summary:            DARMa abstract DAO (data access object) class

Purpose:            This abstract base class contains DAO logic

Python Version:     QA'd on Python 3.4.1

Note:               In Java-land this would be the interface.  
                    As this is Python, it's an abstract class since Python support multiple inheritence.
"""

import abc

__author__ = "Michael Rais"
__version__ = "0.7-beta"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


class DarmaRecordDaoAbstract(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def initialize_record_array(self, loadFrom=None):
        """Method to initialize record array from a source datastore configured in "config.json".  
           The optional loadFrom parameter handles generic info for real-time user options to controlMode
           The use-case allows loading from a different file or repeating command for multiple files."""
        return

    @abc.abstractmethod
    def add_value_map(self, source, target):
    	"""Method that adds value map per configuration options"""
    	return

    @abc.abstractmethod
    def get_value_map(self, source, target):
        """Method that gets value map(s) per configuration options, if it/they exist(s)"""
        return

    @abc.abstractmethod
    def del_value_map(self, source, target):
        """Method that deletes value map(s) per configuration options, if it/they exist(s)"""
        return

    @abc.abstractmethod
    def get_values(self, source):
        """Method that gets all values associated/mapped with/to a source key"""
        return
