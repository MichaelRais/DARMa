"""
PURPOSE: Configuration object

CONFIG FILE: ./config.json
CONTENTS EXAMPLE:
    {
        "initRule": "file",
        "rangeRule": "alpha",
        "controlMode": "localhost",
        "dataMode": "bid"
    }

OPTIONS DESCRIPTION:
...MR will fill in...

"""

import abc
import json

__author__ = "Michael Rais"


class ConfigurationAbstract(metaclass=abc.ABCMeta):
   #__metaclass__ = abc.ABCMeta
    
    def __init__(self):
        """Constructor."""
        # Generic defaults listed.   These settings are overridden if config file read contains override for setting.
        # Options described in header.
        self.initRule = 'file'
        self.rangeRule = 'alpha'
        self.dataMode = 'bid'
        self.controlMode = 'localhost'
        self.configJson = ''
        # Load of configuration.
        self.load_configuration_file()

    def set_config_string(self):
        configJson = (
            '{'
            '"initRule" : "' + self.initRule + '", '
            '"rangeRule" : "' + self.rangeRule + '", '
            '"dataMode" : "' + self.dataMode + '", '
            '"controlMode" : "' + self.controlMode + '"'
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
        except:  # catch any remaining/unexpected exceptions
            print(
                "\nERROR: File config.json couldn't be read due to unknown reason.   Halting. \n")
            raise
        if configUsableFlag:
            # Assign captured config settings.   Any that aren't specified use the defaults.
            for key, value in self.configJson.items():
                #print(" " + key + ": " + value)
                if key == 'initRule':
                    self.initRule = value
                elif key == 'rangeRule':
                    self.rangeRule = value
                elif key == 'dataMode':
                    self.dataMode = value
                elif key == 'controlMode':
                    self.controlMode = value
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
