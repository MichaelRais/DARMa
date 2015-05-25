# Data structure object

class Record():
    def __init__(self):
        """Constructor."""
        self.range = ''
        self.data = {}

    def get_key_exists(self, key):
        """Method that should do something."""
        return

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

    def del_value(self, key, value):
        """Method that should do something."""
        return
