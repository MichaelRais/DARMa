"""
Summary:            Data structure class

Purpose:            This class is the data model.  There is one instance per range item.

Python Version:     QA'd on Python 3.4.1
"""

__author__ = "Michael Rais"
__version__ = "0.7-beta"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"


class Record():
    def __init__(self):
        """Constructor."""
        self.range = ''
        self.data = {}

    def get_value(self, key, value):
        key, value = key.title(), value.title()  # Titlecase everything
        returnval = False
        # Determine if relationship exists (target in source value list)
        sourceGet = self.data.get(key)
        if sourceGet:
            if value in sourceGet:
                returnval = True
        return returnval

    def set_value(self, key, value):
        key, value = key.title(), value.title()  # Titlecase everything
        returnval = False
        # If source already exists, check if target associated or not
        sourceGet = self.data.get(key)
        if sourceGet:
            # Target not already associated - if it is do nothing.
            if value not in sourceGet:
                oldValue = sourceGet
                oldValue.add(value)
                # This can't be combined with above statement
                newValue = oldValue
                # del self.data[source]
                self.data[key] = newValue
            returnval = True
        else:
            item = set() # Sets more performant
            item.add(value)
            self.data[key] = item
            returnval = True
        # print("DATA(" + self.range + "-" + target + "): " + str(self.data))
        return returnval

    def get_values_list(self, key):
        key = key.title()
        returnval = ''
        # Determine if relationship exists (target in source value list)
        sourceGet = self.data.get(key)
        if sourceGet:
            returnval = sourceGet
        return returnval

    def del_value(self, key, value):
        key, value = key.title(), value.title()
        returnval = False
        # If source already exists, check if target associated or not
        sourceGet = self.data.get(key)
        if sourceGet:
            # If target there, delete it
            if value in sourceGet:
                oldValue = sourceGet
                oldValue.remove(value)
                # This can't be combined with above statement
                newValue = oldValue
                self.data[key] = newValue
            returnval = True

    #def get_key_exists(self, key):
    #    """Method that should do something."""
     #   return