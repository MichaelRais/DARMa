# This is a/the concrete class implementing the interface/abstract class (actually two)

import abc
from DarmaRecordDao import DarmaRecordDao
from Configuration import Configuration


class RecordDaoImpl(DarmaRecordDao, Configuration):
    def __init__(self):
    	"""Constructor that should do something"""
    	return

    def initialize_record_array(self, controlMode, initRule):
        """Method that should do something."""
        # Gets Configuration information and loads array accordingly
        # This could probably reference another method or object "fileloader".
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
    print('Subclass (DarmaRecordDao):', issubclass(RecordDaoImpl, DarmaRecordDao))
    print('Instance (DarmaRecordDao):', isinstance(RecordDaoImpl(), DarmaRecordDao))
    print('Subclass (Configuration):', issubclass(RecordDaoImpl, Configuration))
    print('Instance (Configuration):', isinstance(RecordDaoImpl(), Configuration))
