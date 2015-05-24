# This is a/the concrete class implementing the interface/abstract class (actually two)

import abc
from ConfigurationAbstract import ConfigurationAbstract
from DarmaRecordDaoAbstract import DarmaRecordDaoAbstract
from DarmaDaoUtils import DarmaDaoUtils
from Record import Record

class DarmaDao(DarmaRecordDaoAbstract, ConfigurationAbstract):
    def __init__(self):
        """Constructor: Calling abstract base class constructors with super"""
        #super().__init__() #Not useful in this case
        ConfigurationAbstract.__init__(self)
        DarmaRecordDaoAbstract.__init__(self)
        self.configJson = ConfigurationAbstract.get_configuration_info(self)
        """def load_configuration_file(self):
        #TBD if this is implemented here.  Consistent with interface, but not required.
        return ConfigurationAbstract.load_configuration_file(self)
        """

    def get_configuration_info(self):
        #return super(DarmaDao,self).get_configuration_info()
        return self.configJson

    def get_range_info(self):
        """Method that should do something."""
        return

    def initialize_record_array(self):
        """Gets Configuration information and loads array accordingly
        This could probably reference another method or object "fileloader"."""
        # return DarmaRecordDaoAbstract.initialize_record_array(self, controlModeValue, initRuleValue)
        controlModeValue = ConfigurationAbstract.get_config_value(self, self.configJson, 'controlMode')
        initRuleValue = ConfigurationAbstract.get_config_value(self, self.configJson, 'initRule')
        ddUtils = DarmaDaoUtils()
        ddUtilsData = ddUtils.load_records(controlModeValue, initRuleValue)
        for source,target in ddUtilsData:
            self.add_value_map(source,target)

    def add_value_map(self, source, target):
        dRecord = Record() # >>> Determine best placement - needs singleton or factory??? <<<
        dRecord.set_value_map(source.strip(), target.strip())
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
    print('Subclass (of DarmaRecordDaoAbstract):', issubclass(DarmaDao, DarmaRecordDaoAbstract))
    print('Instance (of DarmaRecordDaoAbstract):', isinstance(DarmaDao(), DarmaRecordDaoAbstract))
    print('Subclass (of ConfigurationAbstract):', issubclass(DarmaDao, ConfigurationAbstract))
    print('Instance (of ConfigurationAbstract):', isinstance(DarmaDao(), ConfigurationAbstract))
