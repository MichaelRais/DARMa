"""
Summary:            Data Synchronization class.

Purpose:            This class spins off a thread which synchronizes updates applied on the data models in memory, to the configured destination
                    Action per config.json 'syncRule' (indicates location) and 'syncSchedule' (time in minutes)

Python Version:     QA'd on Python 3.4.1
"""

import threading
import atexit
import time
import logging

__author__ = "Michael Rais"
__version__ = "0.7-beta"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


class Synchronizer():
    def __init__(self):
        pass
 
    def start(self, syncRuleValue, syncScheduleValue, controlModeValue, logDirectoryValue):
        # Start synchronizer thread
        _t = threading.Thread(target=self.monitor_schedule, args=(syncRuleValue, syncScheduleValue,logDirectoryValue))
        _t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
        _t.start()

        # Provide cache
        self.cache=[]

        # Register action to run at exit. 
        atexit.register(self.on_exit, syncRuleValue, syncScheduleValue, controlModeValue, logDirectoryValue)
        if controlModeValue == "interactive":
            print("INFORMATION: Synchronizer started per 'syncRule' and 'syncSchedule' setting.\n")
        return

    def on_exit(self, syncRuleValue, syncScheduleValue, controlModeValue, logDirectoryValue):
        self.execute_sync(syncRuleValue, logDirectoryValue)
        if controlModeValue == "interactive":
            print("\nINFORMATION: Shutdown detected. Executed sync of any cached activity.")
        return

    def monitor_schedule(self, syncRuleValue, syncScheduleValue, logDirectoryValue):
        while True:
            time_in_seconds = int(syncScheduleValue)*60
            time.sleep(time_in_seconds) # Minutes translated to seconds
            #self.sync_to_file(syncScheduleValue, logDirectoryValue)
            self.execute_sync(syncRuleValue, logDirectoryValue)
        return

    def get_schedule():
        pass

    def execute_sync(self, syncRuleValue, logDirectoryValue):
        if syncRuleValue == "mysql":
            pass
            # To be implemented
        elif syncRuleValue == "memcached":
            pass
            # To be implemented
        elif syncRuleValue == "redis":
            pass
        elif syncRuleValue == "file":
            self.sync_to_file(logDirectoryValue)
        return

    def sync_to_mysql(self, syncScheduleValue, logDirectoryValue):
        # Placeholder
        pass

    def sync_to_memcached(self, syncScheduleValue, logDirectoryValue): 
        # Placeholder
        pass

    def sync_to_redis(self, syncScheduleValue, logDirectoryValue):
        pass
        # Implementation TBD as REDIS usage has a large superset of functionality and implies different user / Not sure Redis use-case likely

    def sync_to_file(self, logDirectoryValue):
        """ LOGIC WILL BE BUILT IN: Currently a placeholder """
        #print(self.cache)
        
        # determine section of cache that will be operated on. This accounts for continual appends that may be occurring.
        cache_length = len(self.cache)
        
        # perform log action

        # delete array items through cache_length
        for i in range(cache_length):
            self.cache.pop(0) # pop from the front per cache_length.
        returnData = ''

    
