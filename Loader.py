# This is the Loader class used DarmaDao
# Options based on controlMode and initRule
# DEMONSTRATOR IMPLEMENTATION:  Currently only localhost/file supported

import sys
import traceback
#from DarmaDao import DarmaDao # QUESTION: To avoid using excess memory, I call add_value_map from here, instead of passing back file contents.   Convention?

class Loader():
    def __init__(self):
        pass
 
    def load_records(self, controlModeValue, initRuleValue):
        returnData = []
        if initRuleValue == "mysql":
            pass
            # To be implemented
        elif initRuleValue == "memcached":
            pass
            # To be implemented
        elif initRuleValue == "redis":
            pass
        elif initRuleValue == "file":
            returnData = self.load_from_file(controlModeValue)
        return returnData

    def load_from_mysql(self, controlModeValue):
        # Placeholder
        pass

    def load_from_memcached(self, controlModeValue): 
        # Placeholder
        pass

    def load_from_redis(self, controlModeValue):
        pass
        # Implementation TBD as REDIS usage has a large superset of functionality and implies different user / Not sure Redis use-case likely

    def load_from_file(self, controlModeValue):
        returnData = []
        if controlModeValue == "remote":
            # Logic for remote file load TBD
            pass
        elif controlModeValue == "interface":
            # This is a benchmarking mode so file hardcoded
            mappingFile = 'mappings.txt'
            with open(mappingFile, 'r') as fileArray:
                for line in fileArray:
                    line = [x for x in line.replace('\n', '').split(sep="|")]
                    returnData.append(line)
        elif controlModeValue == "localhost":
            # This is a run mode so file delivered in argument
            if len(sys.argv) != 2:
                # Security considerations for argument capture affect demonstrator only, so not real-world.
                print("Script usage is: " +
                    sys.argv[0] + " 'filename'\n" +
                    " After that, only provide map pairs: 'any mapping | any mapping'  \n"
                )
                exit(1)

            try:
                with open(sys.argv[1], 'r') as fileArray:
                    for line in fileArray:
                        line = [x for x in line.replace('\n', '').split(sep="|")]
                        returnData.append(line)
            except FileNotFoundError:
                print("\nERROR: File load failed.  Halting. \n")
                traceback.print_exc()
                exit(1)
            except:
                print("\nERROR: Unknown error.  Halting. \n")
                traceback.print_exc()
                exit(1)

                        #dd = DarmaDao()
                        #dd.add_value_map(
                        #    alphabetMap, alphaObjs, lineArray[0].strip(), lineArray[1].strip())
        else:
            print(
            "\nERROR: File load method not properly declared|caught.  Halting. \n")
            exit(1)
        return returnData
