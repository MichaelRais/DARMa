"""
Summary:            This is the Loader class used by DarmaDao interface

Purpose:            This class handles initialization data load based on configuration values

Python Version:     QA'd on Python 3.4.1

Note:               Options based on controlMode and initRule
                        Demonstrator:  Currently only localhost/file supported

File Format:        The file format is a text file with pipe delimited mapping pairs.  
                    Outer spaces stripped - Outer quotes are ignored - Inner quotes/apostrophes preserved.
                    (Exporting two columns from Excel with a pipe delimiter is one way to build your own file.)
                    Examples;
                        Ian|Jim
                        JOE SHEPARD|Bob Brown
                        Jim|Mark
                        "John Doe"|'Lady Jane's'
                        Bob Brown|Baron Python
                        Dr. Seuss|Dr. Oz
                        Cole Sterling, 3rd|Winston Sterling

"""

import sys
import re
import traceback
#from DarmaDao import DarmaDao # QUESTION: To avoid briefly using excess memory in production, I could call add_value_map from here, instead of passing back file contents.  Convention?

__author__ = "Michael Rais"
__version__ = "0.7-beta"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


class Loader():
    def __init__(self):
        pass
 
    def load_records(self, controlModeValue, initRuleValue, loadFrom=None):
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
            returnData = self.load_from_file(controlModeValue, loadFrom)
        print("INFORMATION: Data loaded from source per 'initRule' and 'controlMode' settings.")
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

    def load_from_file(self, controlModeValue, loadFrom=None):
        returnData = []
        if loadFrom is None:
            mappingFile = 'mappings.txt' # Default catch-all
        else:
            mappingFile = loadFrom

        if controlModeValue == "production" or controlModeValue == "interactive":
            if controlModeValue == "interactive":
                # For interactive run mode file delivered in argument. 
                if len(sys.argv) != 2:
                    # Security considerations for argument capture affect demonstrator only, so not real-world.
                    print("Script usage is: " +
                        sys.argv[0] + " 'filename'\n" +
                        " After that, only provide map pairs: 'any mapping | any mapping'  \n"
                    )
                    exit(1)
                mappingFile = sys.argv[1]

            try:
                # Regardless of mode, open file and load data
                with open(mappingFile, 'r') as fileArray:
                    for line in fileArray:
                        line = [x for x in line.replace('\n', '').split(sep="|")]
                        for n in range(0, len(line)):
                            line[n] = line[n].strip()
                            line[n] = re.sub(r'^"|"$|^\'|\'$', '', line[n]) # Remove leading/trailing quotes only (allow O'Reilly, etc. of the world)
                        returnData.append(line)
            except FileNotFoundError:
                print("\nERROR: File load failed.  Halting. \n")
                traceback.print_exc()
                exit(1)
            except:
                print("\nERROR: Unknown error.  Halting. \n")
                traceback.print_exc()
                exit(1)
        else:
            print(
            "\nERROR: File load method not properly declared|caught.  Halting. \n")
            exit(1)
        return returnData
