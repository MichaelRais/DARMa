# In Java-land this would be the interface.  As this is Python, it's an abstract class since Python support multiple inheritence.

import abc


class DarmaRecordDAO(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_info(self):
        """Method that gets configuration info."""
        return

    @abc.abstractmethod
    def add_value_map(self, source, target):
    	"""Method that adds value map per configuration options"""
    	return

    @abc.abstractmethod
    def get_value_map(self, source, target):
    	"""Method that gets value map(s) per configuration options, if it/they exist(s)"""

    @abc.abstractmethod
    def del_value_map(self, source, target):
    	"""Method that deletes value map(s) per configuration options, if it/they exist(s)"""

    @abc.abstractmethod
    def get_values(self, source):
    	"""Method that gets all values associated/mapped with/to a source key