import redis
r_server = redis.Redis("localhost")

from timeit import Timer

def do_intersection():
  r_server.sinter("group_1", "group_2")

import time

start = time.time()
do_intersection()
end = time.time()
print end - start
