# This is the concrete class imiplmenting the interface/abstract class

import abc
from DarmaRecordDAO import DarmaRecordDAO


class RecordDaoDataStruct(DarmaRecordDAO):

    def get_configuration_info_X(self):
        """Method that should do something."""
        # If abstract method not in concrete class, should throw warning.  
        # I misnamed _X to trigger warning, but not seeing it.



if __name__ == '__main__':
	print('Subclass:', issubclass(RecordDaoDataStruct, DarmaRecordDAO))
	print ('Instance:', isinstance(RecordDaoDataStruct(), DarmaRecordDAO))


 

