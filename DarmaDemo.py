# Local client usage

from Configuration import Configuration
from RecordDaoImpl import RecordDaoImpl

def main(): 
    oc = Configuration()
    od = RecordDaoImpl()
    # It's unclear if you ever directly access base class. (e.g. interface)

if __name__ == '__main__':
    main()