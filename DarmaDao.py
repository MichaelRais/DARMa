# This is a/the concrete class implementing the interface/abstract class (actually two)

import abc
from ConfigurationAbstract import ConfigurationAbstract
from DarmaRecordDaoAbstract import DarmaRecordDaoAbstract
from Loader import Loader
from RecordRelay import RecordRelay

class DarmaDao(DarmaRecordDaoAbstract, ConfigurationAbstract):
    def __init__(self):
        """Constructor: Calling abstract base class constructors with super"""
        # Super execution: super().__init__() #Not useful in this case
        ConfigurationAbstract.__init__(self)
        DarmaRecordDaoAbstract.__init__(self)
        # Configs to pass
        self.configJson = ConfigurationAbstract.get_configuration_info(self)
        self.controlModeValue = ConfigurationAbstract.get_configuration_value(self, self.configJson, 'controlMode')
        self.initRuleValue = ConfigurationAbstract.get_configuration_value(self, self.configJson, 'initRule')
        self.dataModeValue = ConfigurationAbstract.get_configuration_value(self, self.configJson, 'dataMode')
        """def load_configuration_file(self):
        #TBD if this is implemented here.  Consistent with interface, but not required.
        return ConfigurationAbstract.load_configuration_file(self)
        """
        # Instantiation
        self.rRelay = RecordRelay(self.dataModeValue) # >>> Determine best placement - needs singleton or factory??? <<<

    def get_configuration_info(self):
        #return super(DarmaDao,self).get_configuration_info()
        return self.configJson

    def get_configuration_value(self):
        return ConfigurationAbstract.get_configuration_value(self)

    def get_range_info(self):
        return self.rRelay.get_range_info()

    def load_configuration_file(self):
        return ConfigurationAbstract.load_configuration_file(self)

    def initialize_record_array(self):
        # Gets Configuration information and loads array accordingly
        ddLoader = Loader()
        ddLoaderData = ddLoader.load_records(self.controlModeValue, self.initRuleValue)
        for source,target in ddLoaderData:
            self.add_value_map(source,target)
        return True

    def add_value_map(self, source, target):     
        returnval = False
        if self.dataModeValue == "uni":
            self.rRelay.set_value(source.strip(), target.strip())
            returnval = True
        elif self.dataModeValue == "bid":
            self.rRelay.set_value(source.strip(), target.strip())
            self.rRelay.set_value(target.strip(), source.strip())
            returnval = True
        return returnval

    def get_value_map(self, source, target):
        returnval = False
        if self.dataModeValue == "uni":
            if self.rRelay.get_value(source.strip(), target.strip()):
                returnval = True
        elif self.dataModeValue == "bid":
            if (self.rRelay.get_value(source.strip(), target.strip()) or self.rRelay.get_value(target.strip(), source.strip())):
                returnval = True
        else:
            # If we can't determine the dataModeValue, set it.  Overly cautious, drops first request, and provisionally allows for functionality if no other unexpected settings.
            self.dataModeValue = "bid"
        return returnval

    def del_value_map(self, source, target):
        returnval = False
        if self.dataModeValue == "uni":
            if self.rRelay.del_value(source.strip(), target.strip()):
                returnval = True
        elif self.dataModeValue == "bid":
            if self.rRelay.del_value(target.strip(), source.strip()):
                returnval = True
        return returnval

    def get_values(self, source):
        returnval = ''
        if self.rRelay.get_values_list(source.strip()):
            returnval = self.rRelay.get_values_list(source.strip())
        return returnval


if __name__ == '__main__':
    print('Subclass (of DarmaRecordDaoAbstract):', issubclass(DarmaDao, DarmaRecordDaoAbstract))
    print('Instance (of DarmaRecordDaoAbstract):', isinstance(DarmaDao(), DarmaRecordDaoAbstract))
    print('Subclass (of ConfigurationAbstract):', issubclass(DarmaDao, ConfigurationAbstract))
    print('Instance (of ConfigurationAbstract):', isinstance(DarmaDao(), ConfigurationAbstract))
