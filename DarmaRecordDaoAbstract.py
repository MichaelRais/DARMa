"""
Summary:            DARMa abstract DAO (data access object) class

Purpose:            This abstract base class contains DAO logic

Python Version:     QA'd on Python 3.4.1

Note:               In Java-land this would be the interface.  
                    As this is Python, it's an abstract class since Python support multiple inheritence.
"""

import abc

__author__ = "Michael Rais"
__version__ = "0.5-alpha"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


class DarmaRecordDaoAbstract(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def initialize_record_array(self, controlMode, initRule):
        print("PASS: " + controlMode + " | " + initRule)
        """The controlMode/initRule defaults should come in this way, so these defaults are possibly over-conservative"""
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
