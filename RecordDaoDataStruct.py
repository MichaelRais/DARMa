# This is a/the concrete class implementing the interface/abstract class

import abc
from DarmaRecordDAO import DarmaRecordDAO


class RecordDaoDataStruct(DarmaRecordDAO):
    def RecordDaoDataStruct(self,Configuration):
    	"""Constructor that should do something"""
    	return

    def initialize_record_array(self, controlMode, initRule):
    	"""Method that should do something."""
        return

    def get_configuration_info_X(self):
        """Method that should do something."""
        # If abstract method not in concrete class, should throw warning.
        # I misnamed _X to trigger warning, but not seeing it.
        return

    def get_configuration_info(self):
        """Method that should do something."""
        return

    def get_range_info(self):
    	"""Method that should do something."""
        return

    def add_value_map(self, source, target):
    	"""Method that should do something."""
        return

    def get_value_map(self, source, target):
    	"""Method that should do something."""
        return

    def del_value_map(self, source, target):
    	"""Method that should do something."""
        return

    def get_values(self, source):
    	"""Method that should do something."""
        return

if __name__ == '__main__':
    print('Subclass:', issubclass(RecordDaoDataStruct, DarmaRecordDAO))
    print('Instance:', isinstance(RecordDaoDataStruct(), DarmaRecordDAO))
