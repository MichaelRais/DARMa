"""
Summary:            Data Synchronization class.

Purpose:            This class spins off a thread which synchronizes updates applied on the data models in memory, to the configured destination
                    Action per config.json 'syncRule' (indicates location) and 'syncSchedule' (time in minutes)

Python Version:     QA'd on Python 3.4.1
"""

import threading
import time
import atexit

__author__ = "Michael Rais"
__version__ = "0.7-beta"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


class Synchronizer():
    def __init__(self):
        pass
 
    def start(self, syncRuleValue, syncScheduleValue):
        _t = threading.Thread(target=self.monitor_schedule, args=(syncRuleValue, syncScheduleValue))
        _t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
        _t.start()
        # Register action to run at exit. 
        atexit.register(self.on_exit, syncRuleValue, syncScheduleValue)
        print("INFORMATION: Synchronizer started per 'syncRule' and 'syncSchedule' setting.\n")
        return

    def on_exit(self, syncRuleValue, syncScheduleValue):
        self.execute_sync(syncRuleValue, syncScheduleValue)
        print("\nINFORMATION: Shutdown detected. Executed sync of any cached activity.")
        return

    def monitor_schedule(self, syncRuleValue, syncScheduleValue):
        while True:
            time_in_seconds = int(syncScheduleValue)*60
            time.sleep(time_in_seconds) # Minutes translated to seconds
            self.sync_to_file(syncRuleValue, syncScheduleValue)
        return

    def get_schedule():
        pass

    def execute_sync(self, syncRuleValue, syncScheduleValue):
        if syncRuleValue == "mysql":
            pass
            # To be implemented
        elif syncRuleValue == "memcached":
            pass
            # To be implemented
        elif syncRuleValue == "redis":
            pass
        elif syncRuleValue == "file":
            self.sync_to_file(syncRuleValue, syncScheduleValue)
        return

    def sync_to_mysql(self, syncRuleValue, syncScheduleValue):
        # Placeholder
        pass

    def sync_to_memcached(self, syncRuleValue, syncScheduleValue): 
        # Placeholder
        pass

    def sync_to_redis(self, syncRuleValue, syncScheduleValue):
        pass
        # Implementation TBD as REDIS usage has a large superset of functionality and implies different user / Not sure Redis use-case likely

    def sync_to_file(self, syncRuleValue, syncScheduleValue):
        """ LOGIC WILL BE BUILT IN: Currently a placeholder """
        returnData = ''

        if syncRuleValue != "file":
            # Logic for other options will be filled in
            pass
        elif syncRuleValue == "file":
            pass
