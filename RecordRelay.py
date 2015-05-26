# Data structure relay object

from Record import Record

class RecordRelay(object):

    def __init__(self, dataModeValue):
        """Constructor."""
        # For demonstrator these are class variables.  Possibly change to one instance per group.
        self.groupMap = '0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(sep=",")
        self.groupMap = dict(zip(range(len(self.groupMap)), self.groupMap))
        self.groupObjs = [] # Object container
        """The groupMap map must not change without corresponding object management update
        to captured chars (e.g. friend1[0:1], friend2[0:1] becomes friend1[0:2],
        friend2[0:2] when you update alphabetMap to AA, AB, AC, AD, ...)"""    
        self.create_record_array(dataModeValue)

    def create_record_array(self, dataMode):
        """Create one alphanum object per alphanum for data structures.  Conceptually for
        naive parallelization & scalability, though data spread is unbalanced.  Ranges
        can be partitioned further and made smarter."""
        for key, value in self.groupMap.items():
            self.groupObjs.append(Record())
            self.groupObjs[key].range = value
        return

    def get_value(self, source, target):
        source, target = source.title(), target.title()
        fRoute = self.__find_route(source)
        if self.groupObjs[fRoute].get_value(source, target):
            return True
        else:
            return False

    def set_value(self, source, target):
        source, target = source.title(), target.title()
        fRoute = self.__find_route(source)
        if self.groupObjs[fRoute].set_value(source, target):
            return True
        else:
            return False

    def get_values_list(self, source):
        returnval = ''
        source = source.title()
        fRoute = self.__find_route(source)
        if self.groupObjs[fRoute].get_values_list(source):
            returnval = self.groupObjs[fRoute].get_values_list(source)
        return returnval

    def del_value(self, source, target):
        source, target = source.title(), target.title()
        fRoute = self.__find_route(source)
        if self.groupObjs[fRoute].del_value(source, target):
            return True
        else:
            return False

    def get_range_info(self):
        return self.groupMap

    def __find_route(self, source):
        fRoute = source[0:1]
        objectLookup = dict(map(reversed, self.groupMap.items()))
        fRoute = objectLookup.get(fRoute)
        return fRoute

    #def get_key_exists(self, key):
    #    """Method that should do something."""
    #    return