# Local client usage

#from ConfigurationAbstract import ConfigurationAbstract
#from DarmaRecordDaoAbstract import DarmaRecordDaoAbstract
import sys
from DarmaDao import DarmaDao

def main(): 
    #oc = ConfigurationAbstract()
    od = DarmaDao()
    v = od.get_configuration_info()
    print(v)
    w = od.initialize_record_array()

    if od.get_value_map(sys.argv[2].strip(), sys.argv[3].strip()):
        print("yes")
    else:
        print("no")

    print("VALUE LIST: " + str(od.get_values(sys.argv[2].strip())))

    od.del_value_map(sys.argv[2].strip(), sys.argv[3].strip())
    print("VALUE LIST (post-del): " + str(od.get_values(sys.argv[2].strip())))

    print("Range Info: " + str(od.get_range_info()))
    
    # It's unclear if you ever directly access base class. (e.g. interface)

if __name__ == '__main__':
    main()



"""
----->> TODO LIST <<-----
Batch 1)
Time to implement singleton for initialization logic and factory for the rest?


Batch 2) 
If you pass config around as a pojo, you can just access in each object.
Thread spin-off of service & checking for instantiated data
"""
