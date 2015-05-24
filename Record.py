# Data structure object

class Record():

    # For demonstrator these are class variables.  Should change to one instance per group.
    groupMap = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9'.split(sep=",")
    groupMap = dict(zip(range(len(groupMap)), groupMap))
    groupObjs = [] # Object container
    """The groupMap map must not change without corresponding object management update
    to captured chars (e.g. friend1[0:1], friend2[0:1] becomes friend1[0:2],
    friend2[0:2] when you update alphabetMap to AA, AB, AC, AD, ...)"""

    def __init__(self):
        """Constructor."""
        #self.range ''
        #self.data = {}


    def create_record_array(self, dataMode, rangeRule):
        """Create one alpha object per alpha, for data structures.  Conceptually for
        parallelization & scalability, though data spread is unbalanced.  Ranges
        can be partitioned further and made smarter."""
        for key, value in groupMap.items():
            groupObjs.append(Record())
            groupObjs[key].range = value
        return

    def get_key_exists(self, key):
        """Method that should do something."""
        return

    def get_value_map(self, key, value):
        """Method that should do something."""
        return

    def set_value_map(self, key, value):
        """Method that should do something."""
        return

    def del_value_map(self, key, value):
        """Method that should do something."""
        return
