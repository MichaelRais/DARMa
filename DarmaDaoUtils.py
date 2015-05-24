# This is a/the utilty class for DarmaDao 

import sys
import traceback
#from DarmaDao import DarmaDao # QUESTION: To avoid using excess memory, I call add_value_map from here, instead of passing back file contents.   Convention?

class DarmaDaoUtils():
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
            pass
            # Logic for remote file load TBD
        elif controlModeValue == "localhost":
            if len(sys.argv) != 4:
                # Security considerations for argument capture beyond scope of demonstrator.
                print("Script usage is: " +
                    sys.argv[0] + " 'filename' 'any mapping' 'any mapping'\n" +
                    " Any alphanumeric with space allowed in anymapping fields. \n" + 
                    " The filename is used for both data load and to identify the \n" +
                    " namespace of the data model. First usage loads the data from \n" +
                    " the filename, and afterwards the relevant data model is used. \n"
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
            exit(0)
        return returnData
