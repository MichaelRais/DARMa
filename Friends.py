""" Summary:            Friends is question #3 from the Reelio test.

    P-Version:          QA'd on Python 3.4.1	

    Knowledge domains:  Relationship networks, performance profiling
   						(e.g. import cProfile|profile, profile.run('main()' -or-
   						python -m cProfile [-o output_file] [-s sort_order] myscript.py)

    Candidates Eval'd:	Data model, map/reduce (functools module), OOD
   						    

    Considerations:		Short on time so trading off succinct requirement for functional requirement.
                        Intended usage of the system implies need for conceptual parallelization being designed in.  As implemented, there's still some blocking, but it's better than a monolithic container object.  With this design, full logical & Physical parallization is easier done later.
 

    Decision History:   Going OO, but not creating multi-threading per the alpha containers.  Also, getting user file data persistent in memory would be key for a real performance test.
                        As-is the object routing per alpha prefix is effectively an unbalanced/simplistic routing option that allows for parallelization, and implies built-in option for ranges with more granularity.
                        I naively applied the data model used in the data dictionary per reading I did on Hadoop a while back - could use a 2nd pass.
                        It was suggested I use sets inside dictionary, instead of lists.
                            (implies coming up with a naming key of some kind (e.g. Name::email@)) or embedding single-user data structures in set positions.


    Data Format:		Friend records --  {'Bob Brown': ['Sam Smith', 'Joe Shepard']}
                        Alpha lookup for object routing --  {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}


    Script Usage:       python Friends.py <filename> <name1> <name2>
   					

    Note:               There is gratuitous overdesign here but it was more natural to me than code shaving the test so I went for the exercise as relevant to production environments.
"""


import itertools
import sys


__author__ = "Michael Rais"
__version__ = "0.1-alpha"
__maintainer__ = "Michael Rais"
__email__ = "mrais@inbox.com"
__status__ = "Development"


class FriendMap():

    def __init__(self):
        self.range, self.data = '', {}

    def get_friends(self, source):
        source = source.title()  # Titlecase everything
        return self.data.get(source)

    def add_friend_map(self, source, target):
        source, target = source.title(), target.title()  # Titlecase everything      
        # If source already exists, check if target associated or not
        sourceGet = self.data.get(source)
        if sourceGet:
            # Target not already associated - if it is do nothing.
            if target in sourceGet:
                oldValue = sourceGet
                oldValue.add(target)
                # This can't be combined with above statement
                newValue = oldValue
                self.data[source] = newValue
        else:
            item = set()
            item.add(target)
            self.data[source] = item

    def get_friend_map(self, source, target):
        source, target = source.title(), target.title()  # Titlecase everything
        returnval = False
        # Determine if relationship exists (target in source value list)
        sourceGet = self.data.get(source)
        if sourceGet:
            if target in sourceGet:
                returnval = True
        return returnval


# method with object routing for performance - these would never be in class of data structure object itself.
def add_friendship(alphabetMap, alphaObjs, friend1, friend2):
    friend1, friend2 = friend1.title(), friend2.title()
    fRoute1, fRoute2 = friend1[0:1], friend2[0:1]
    objectLookup = dict(map(reversed, alphabetMap.items()))
    fRoute1, fRoute2 = objectLookup.get(fRoute1), objectLookup.get(fRoute2)
    alphaObjs[fRoute1].add_friend_map(friend1, friend2)
    alphaObjs[fRoute2].add_friend_map(friend2, friend1)


# method with object routing for performance
def get_friendship(alphabetMap, alphaObjs, friend1, friend2):
    friend1, friend2 = friend1.title(), friend2.title()
    fRoute1, fRoute2 = friend1[0:1], friend2[0:1]
    objectLookup = dict(map(reversed, alphabetMap.items()))
    fRoute1, fRoute2 = objectLookup.get(fRoute1), objectLookup.get(fRoute2)
    if (alphaObjs[fRoute1].get_friend_map(friend1, friend2) or alphaObjs[fRoute2].get_friend_map(friend2, friend1)):
        # First positive in conditional exits conditional and return True.   
        return True
    else:
        return False


def main():
    # This map must not change without corresponding object management update
    # to captured chars (e.g. friend1[0:1], friend2[0:1] becomes friend1[0:2],
    # friend2[0:2] when you update alphabetMap to AA, AB, AC, AD, ...)
    alphabetMap = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(
        sep=",")
    alphabetMap = dict(zip(range(len(alphabetMap)), alphabetMap))
    alphaObjs = []  # Object container

    # Create one alpha object per alpha, for data structures.  Thinking future
    # parallelization & scalability, though data spread is unbalanced.  Ranges
    # can be partitioned further.
    for x, y in alphabetMap.items():
        alphaObjs.append(FriendMap())
        alphaObjs[x].range = y

    # Security considerations for argument capture beyond scope of example.
    if len(sys.argv) != 4:
        print("Script usage is: " +
              sys.argv[0] + " 'filename' 'fname lname' 'fname lname'")
        exit(0)

    oFile = open(sys.argv[1], 'r')
    try:
        fileArray = list(oFile.readlines())
        for line in fileArray:
            lineArray = [x for x in line.replace('\n', '').split(sep=",")]
            add_friendship(
                alphabetMap, alphaObjs, lineArray[0].strip(), lineArray[1].strip())
    finally:
        oFile.close()

    if get_friendship(alphabetMap, alphaObjs, sys.argv[2].strip(), sys.argv[3].strip()):
        print("yes")
    else:
        print("no")

    qaCheck = add_friendship(alphabetMap, alphaObjs, 'John Doe', 'Lady Jane')
    #assert (get_friendship(alphabetMap, alphaObjs, 'Lady jane', 'John Doe')
            #) == True, "ERROR:  Simple constrained validation failed.  Answer may not be accurate."


if __name__ == '__main__':
    main()
