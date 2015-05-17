# This is a/the concrete class implementing the interface/abstract class (actually two)

import abc
from ConfigurationAbstract import ConfigurationAbstract
from DarmaRecordDaoAbstract import DarmaRecordDaoAbstract

class DarmaDao(DarmaRecordDaoAbstract, ConfigurationAbstract):
    def __init__(self):
        """Constructor: Calling abstract base class constructor with super"""
        #super().__init__() #Not useful in this case
        ConfigurationAbstract.__init__(self)
        DarmaRecordDaoAbstract.__init__(self)

    #def get_configuration_info(self):
     #   import json
     #   return json.dumps(self.configJson, indent=4)
        # """Method that should do something."""
        #pass

    def initialize_record_array(self, controlMode, initRule):
        """Method that should do something."""
        # Gets Configuration information and loads array accordingly
        # This could probably reference another method or object "fileloader".
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
    print('Subclass (DarmaRecordDaoAbstract):', issubclass(DarmaDao, DarmaRecordDaoAbstract))
    print('Instance (DarmaRecordDaoAbstract):', isinstance(DarmaDao(), DarmaRecordDaoAbstract))
    print('Subclass (ConfigurationAbstract):', issubclass(DarmaDao, ConfigurationAbstract))
    print('Instance (ConfigurationAbstract):', isinstance(DarmaDao(), ConfigurationAbstract))
