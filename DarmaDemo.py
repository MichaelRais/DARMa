# Local client usage

import sys
import re
from DarmaDao import DarmaDao

def main(): 
    scriptWrapCache = None
    
    # BEGIN: Indefinite user prompt
    while True:
            if not scriptWrapCache:
                dd = DarmaDao()
                show_cfg_dd = dd.get_configuration_info()
                print("\n>Configuration Information: \n" + show_cfg_dd + "\n")
                init_dd = dd.initialize_record_array()
                scriptWrapCache = init_dd
            try:
                print(">Please enter map pair to evaluate (i.e. 'any mapping | any mapping'), or CTRL-C to exit.")
                lineread = sys.stdin.readline()
            except KeyboardInterrupt:
                exit(1)

            #lineread = [x for x in lineread.replace('\n', '').replace('\'', '').replace('\"', '').split(sep="|")]
            lineread = [x for x in lineread.replace('\n', '').split(sep="|")]
            for n in range(0, len(lineread)):
                lineread[n] = lineread[n].strip()
                lineread[n] = re.sub(r'^"|"$|^\'|\'$', '', lineread[n]) # Remove leading/trailing quotes only (allow O'Reilly, etc. of the world)

            #print(lineread)            
            if len(lineread) != 2:
                print("\nSYNTAX WARNING: Two mapping not detected, or input couldn't be read." +
                      "\nExpected format: mapping | mapping with space ok"
                )
            else:
                if dd.get_value_map(lineread[0].strip(), lineread[1].strip()):
                    print("\n RESULT: Mapping found.\n")
                else:
                    print("\n RESULT: No mapping for input.\n")

if __name__ == '__main__':
    main()

"""
print("VALUE LIST: " + str(od.get_values(sys.argv[2].strip())))

od.del_value_map(sys.argv[2].strip(), sys.argv[3].strip())
print("VALUE LIST (post-del): " + str(od.get_values(sys.argv[2].strip())))

print("Range Info: " + str(od.get_range_info()))
"""