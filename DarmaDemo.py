# Local client usage

#from ConfigurationAbstract import ConfigurationAbstract
#from DarmaRecordDaoAbstract import DarmaRecordDaoAbstract
from DarmaDao import DarmaDao

def main(): 
    #oc = ConfigurationAbstract()
    od = DarmaDao()
    v = od.get_configuration_info()
    print(v)
    # It's unclear if you ever directly access base class. (e.g. interface)

if __name__ == '__main__':
    main()