# In Java-land this would be the interface.  As this is Python, it's an abstract class since Python support multiple inheritence.

import abc
#import Configuration  # Usage TBD
#import RecordDaoImpl   #Usage TBD


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
