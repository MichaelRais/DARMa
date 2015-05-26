""" 
Summary:            DARMa client demo script

Purpose:            This script demonstrates functionality on command-line.

Python Version:     QA'd on Python 3.4.1

Knowledge domains:  Data Access Object pattern.  Benchmarking.   Data models.  OOD

Data Format:        Mapping records --  {'Bob Brown': {'Sam Smith', 'Joe Shepard'}
                    When alpha:  grouped by first letter
                    When numeric:  Grouped by first digit.
                    Alphanumeric lookup map for object routing --  {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: ....}


Demo Script Usage:  python DarmaDemo.py <filename>
                        The <filename> contains pipe delimited mapping pairs to be loaded on start-up.
                        The example file is:  "mappings.txt"

Inline Example:     Initialization (run once);
                        dd = DarmaDao()
                        show_cfg_dd = dd.get_configuration_info()
                        init_dd = dd.initialize_record_array([loadfrom=$filename])
                    Application usage (run often);
                        dd.set_value_map("mapping A", "mapping B")
                        dd.get_value_map("mapping A", "mapping B")

"""

import sys
import re
from DarmaDao import DarmaDao

__author__ = "Michael Rais"
__version__ = "0.5-alpha"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


def main():
    scriptWrapCache = None
    # Indefinite user prompt
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

            # lineread = [x for x in lineread.replace('\n', '').replace('\'', '').replace('\"', '').split(sep="|")]
            lineread = [x for x in lineread.replace('\n', '').split(sep="|")]
            for n in range(0, len(lineread)):
                lineread[n] = lineread[n].strip()
                lineread[n] = re.sub(r'^"|"$|^\'|\'$', '', lineread[n])  # Remove leading/trailing quotes only (allow O'Reilly, etc. of the world)

            # print(lineread)
            if len(lineread) != 2:
                print("\nSYNTAX WARNING: Two mapping not detected, or input couldn't be read." +
                      "\nExpected format: mapping | mapping with space ok")
            else:
                if dd.get_value_map(lineread[0].strip(), lineread[1].strip()):
                    print("\n RESULT: Mapping found.\n")
                else:
                    print("\n RESULT: No mapping for input.\n")

if __name__ == '__main__':
    main()
