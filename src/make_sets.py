import redis
import random

r_server = redis.Redis("localhost")

for x in xrange(10000000):
  val = random.randrange(5)
  if val < 4:
    r_server.sadd("group_1", x)
  if val > 2:
    r_server.sadd("group_2", x)
  