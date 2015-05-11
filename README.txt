DARMa

Distributed
 Adaptive
  Relationship
    Mapper


20150505 (Mike Rais)  Started


SUMMARY
Think of DARMa as a locally hosted memcached or Redis service.    It's written in Python, and it just takes some of complexity out of managing Python data structures, for the 99% of websites that don't need Redis or Memcached, where the web developer may feel NoSQL is warranted.   It provides an abstraction layer that allows for both NoSQL via DARMa and future usage of Redis or Memcached.

The data itself is partitioned by DARMa's config, which would indicate whether to partition on alpha or on ranges of id's - that's just for some simplistic optimization of data structure usage.    It also allows for the NoSQL backend to get swapped, so if the user wants to install Redis or Memcached at a future date, they can just swap it in via DARMa config and then on the backend DARMa just routes the requests to the configured service.   (This is currently implicit in design - not explicit)