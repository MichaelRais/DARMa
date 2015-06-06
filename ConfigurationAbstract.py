"""
Summary:            DARMa abstract configuration class

Purpose:            This abstract base class contains configuration logic

Python Version:     QA'd on Python 3.4.1

Config file:        ./config.json
Contents Example:   Note that without config.json defaults are used, and controlMode is "interactive"
                    {
                        "controlMode": "interactive",
                        "dataMode": "uni",
                        "initRule": "file",
                        "rangeRule": "alphanum",
                        "syncRule": "file",
                        "syncSchedule": "1"
                    }

Options Description:
    Control Mode:   This mode indicates where the controlling NoSQL abstraction layer is running.
                    Currently the only accepted value for the demonstrator is: "production" or "interactive".
                        production = The DARMa service runs in production mode per settings.
                        interactive = Demo mode and default.  Not for production.  The DARMa service runs locally in interactive demo mode.

    Data Mode:      This mode indicates if key/value sets/gets are unidirectional or bi-directional.
                    Currently this setting is fully functional.
                        uni = Sets and gets are one-way.  (e.g. loading a map of "Ian Frei | Joe Yup" only matches "Ian Frei | Joe Yup", but not "Joe Yup | Ian Frei")
                        bid = Sets and gets are two-way.  (e.g. loading a map of "Ian|Joe" matches either "Ian|Joe" or "Joe|Ian")

    Init Rule:      This rule indicates where data is loaded from on initialization.
                    Currently the only accepted value for the demonstrator is: file
                        file = load data from pipe-delimited text file.
                    Future values will be:  file, cold, dbase
                        file = file, cold = without data load, dbase = database, api = api

    Range Rule:     This rule indicates how the data model is sub-divided.
                    Currently the only accepted value for the demonstrator is: alphanum
                        alphanum = Divides the data model into 36 objects, by both;
                        alphabet = 26 groups  (for grouping by alpha)
                        first number = 10 groups  (for unordered primary keys)
                    Future values will be: range
                        range = sub-division by primary key ranges

    Sync Rule:      This rule indicates where data is synchronized during runtime, after initialization.
                    Currently the only accepted value for the demonstrator is: file
                        file = Picked (TBD) data delivered to holding directory on schedule set by "syncSchedule"
                    Future values will be:  Same as "Init Rule" future values.   However, they don't require being set to the same value.

    Sync Schedule:  This rule indicates the schedule of synchronization, in minutes.
                    Currently there is no limit on accepted values, and recommended values likely between 1-10 (TBD)
"""

import abc
import json

__author__ = "Michael Rais"
__version__ = "0.7-beta"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


class ConfigurationAbstract(metaclass=abc.ABCMeta):
    # __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor."""
        # Generic defaults listed.   These settings are overridden if config file read contains override for setting.
        # Options described in header.
        self.initRule = 'file'
        self.rangeRule = 'alphanum'
        self.dataMode = 'bid'
        self.controlMode = 'interactive'
        self.syncRule = 'file'
        self.syncSchedule = '1'
        self.logDirectory = 'logs'
        self.configJson = ''
        # Load of configuration.
        self.load_configuration_file()

    def set_config_string(self):
        configJson = (
            '{'
            '"controlMode" : "' + self.controlMode + '", '
            '"dataMode" : "' + self.dataMode + '", '
            '"initRule" : "' + self.initRule + '", '
            '"rangeRule" : "' + self.rangeRule + '", '
            '"syncRule" : "' + self.syncRule + '", '
            '"syncSchedule" : "' + self.syncSchedule + '", '
            '"logDirectory" : "' + self.logDirectory + '"'
            '}'
        )  # Init of default settings
        self.configJson = json.loads(configJson)  # NOTE: "loads" is for strings.  "load" is for file.
        return self.configJson

    @abc.abstractmethod
    def load_configuration_file(self):
        configUsableFlag = False
        configJson = self.set_config_string()

        try:
            # json.dump(config, open('./config.json', 'w'), indent=4)
            self.configJson = json.load(open('./config.json'))
            configUsableFlag = True
        except FileNotFoundError:
            print(
                "WARNING: File config.json couldn't be found in directory.   Defaults used.")
            # Continuation OK if file missing, unlike readability
            # or unexpected errs
            configUsableFlag = True
        except ValueError:
            print(
                "\nERROR: File config.json didn't have readable contents.   JSON format expected.   Halting. \n")
            raise
        except:  # Catch any remaining/unexpected exceptions
            print(
                "\nERROR: File config.json couldn't be read due to unknown reason.   Halting. \n")
            raise
        if configUsableFlag:
            # Assign captured config settings.   Any that aren't specified use the defaults.
            for key, value in self.configJson.items():
                # print(" " + key + ": " + value)
                if key == 'initRule':
                    self.initRule = value
                elif key == 'rangeRule':
                    self.rangeRule = value
                elif key == 'dataMode':
                    self.dataMode = value
                elif key == 'controlMode':
                    self.controlMode = value
                elif key == 'syncRule':
                    self.syncRule = value
                elif key == 'syncSchedule':
                    self.syncSchedule = value
                elif key == 'logDirectory':
                    self.logDirectory = value
                else:
                    print("  \-> WARNING: Unexpected config key '" + key + "' can't be used.")
            configJson = self.set_config_string()
        return self.get_configuration_info()

    @abc.abstractmethod
    def get_configuration_info(self):
        return json.dumps(self.configJson, indent=4)

    @abc.abstractmethod
    def get_configuration_value(self, configJson, getKey):
        returnValue = ''
        configJson = json.loads(configJson)
        for key, value in configJson.items():
            if key.lower() == getKey.lower():
                returnValue = value.lower()
        return returnValue

    @abc.abstractmethod
    def get_range_info(self):
        """Method that should do something."""
        pass


if __name__ == '__main__':
    o = Configuration()
