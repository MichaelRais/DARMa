# Local client usage

#from ConfigurationAbstract import ConfigurationAbstract
#from DarmaRecordDaoAbstract import DarmaRecordDaoAbstract
from DarmaDao import DarmaDao

def main(): 
    #oc = ConfigurationAbstract()
    od = DarmaDao()
    v = od.get_configuration_info()
    print(v)
    w = od.initialize_record_array()
    
    # It's unclear if you ever directly access base class. (e.g. interface)

if __name__ == '__main__':
    main()



"""
----->> TODO LIST <<-----
Batch 1)
Placement of DarmaDao call of Record class.
Time to implement singleton for initialization logic and factory for the rest?
Placement of DarmaDao constructor "self.configJson = ConfigurationAbstract.get_configuration_info(self)"

Batch 2) 
Thread spin-off of service & checking for instantiated data
"""
