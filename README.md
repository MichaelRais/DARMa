# DARMa
Delegated
 Active
  Relationship
    Mapper

# Summary
This is a technology demonstrator of a Python NoSQL service I wrote.  Goals for project;
<ul>
<li>Use Python abstraction for interfaces
<li>Use DAO pattern
<li>Consider OO design
<li>Release functional prototype
</ul>
<i>Documentation is still being worked on. The first stable demonstrator was wrapped on 5/25, so the documentation in this file is just a start point.

# Overview
Think of DARMa as a locally hosted memcached service.   It's written in Python, and it just takes some of complexity out of managing Python data structures.   The use-case is for the 99% of websites that don't need Redis or Memcached, where the web developer may feel NoSQL is warranted.   It provides an abstraction layer that allows for both NoSQL via DARMa and future usage of Redis or Memcached.
<ul>
<li>The data itself is partitioned by DARMa's config, which would indicate whether to partition on alphanumeric or on ranges of id's - that's just for some simplistic optimization of data structure usage.    It also allows for the NoSQL backend to get swapped, so if the user wants to install Redis or Memcached at a future date, they can just swap it in via DARMa config and then on the backend DARMa just routes the requests to the configured service.   (This is currently implicit in design - not explicit)
</ul>

Anyone with design feedback please reach out to me and let me hear it through Github or LinkedIn:<br>
        https://www.linkedin.com/in/michaelrais/
I'd like to get an architect involved.

# Main Components
<ul>
<li>Demonstrator script:  DarmaDemo.py
<li>Interface (API): DarmaDao.py
<li>Configuration file: config.json
<li>Data file: mappings.txt
</ul>

# Requirements
<ul>
<li> Tested on Python 3.4.1
</ul>

# Usage
Demo Script Usage:  python DarmaDemo.py <filename>
                        The <filename> contains pipe delimited mapping pairs to be loaded on start-up.
                        The example file is:  "mappings.txt"

Inline Example:     Initialization (run once);
                        dd = DarmaDao()
                        show_cfg_dd = dd.get_configuration_info()
                        init_dd = dd.initialize_record_array()
                    Application usage (run often);
                        dd.set_value_map("mapping A", "mapping B")
                        dd.get_value_map("mapping A", "mapping B")

# Reference Documents
<ul>
<li>Class Diagram:  DARMa Class Diagram-v2.1.jpg
<li>Benchmark Results:  20150525_benchmark_results.txt
</ul>

# Configuration Details
Config file:        ./config.json
Contents Example:
                    {
                        "initRule": "file",
                        "rangeRule": "alphanum",
                        "controlMode": "localhost",
                        "dataMode": "bid"
                    }

Init file:          ./mappings.txt
Contents Example:   The file format is a text file with pipe delimited mapping pairs.  
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

Options Description:
    Init Rule:      This rule indicates where data is loaded from on initialization.
                    Currently the only accepted value for the demonstrator is "file".
                        file = load data from pipe-delimited text file.
                    Future values will be:  file, cold, dbase
                        file = file, cold = without data load, dbase = database, api = api

    Range Rule:     This rule indicates how the data model is sub-divided.
                    Currently the only accepted value for the demonstrator is "alphanum".
                        This divides the data model into 36 objects, by both;
                            alphabet = 26 groups  (for grouping by alpha)
                            first number = 10 groups  (for unordered primary keys)
                    Future values will be: range
                            range = sub-division by primary key ranges

    Control Mode:   This mode indicates where the controlling NoSQL abstraction layer is running.
                    Currently the only accepted value for the demonstrator is "localhost" or "interface".
                        localhost = The DARMa service runs locally and data managed locally after start-up
                        interface = special local benchmarking mode
                    Future values will be: cluster
                        cluster = A remote service is being used to manage data after start-up.  Could be anything that gets plugged in.

    Data Mode:      This mode indicates if key/value sets/gets are unidirectional or bi-directional.
                    Currently this setting is fully functional.
                        uni = Sets and gets are one-way.  (e.g. loading a map of "Ian Frei | Joe Yup" only matches "Ian Frei | Joe Yup", but not "Joe Yup | Ian Frei")
                        bid = Sets and gets are two-way.  (e.g. loading a map of "Ian|Joe" matches either "Ian|Joe" or "Joe|Ian")


# Release History: 
   -20150525(M. Rais):  v0.5.0 - First stable demonstrator. Cleaned up files/headers. Updated class diagram.  SIF5 becoming v0.5.0-alpha.  
