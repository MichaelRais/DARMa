# In Java-land this would be the interface.  As this is Python, it's an abstract class

import abc


class DarmaRecordDAO(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_info(self):
        """Method that should do something."""
