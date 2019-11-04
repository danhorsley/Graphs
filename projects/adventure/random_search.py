from my_utils import *
from adv import roomGraph as rg
import csv
import json

g = roomgraph_to_graph(rg)
random_paths = {}
min_hurdle = 986
k = 0
while min_hurdle > 980:
  path = g.dft(0, randomizer = True)
  wp = connect_the_dots(path,g)
  print(len(wp))
  random_paths[k] = {'length':len(wp),'path':wp}
  if len(wp) <min_hurdle:
      min_hurdle = len(wp)
  k +=1

jj = json.dumps(random_paths)
f = open("paths.txt","w")
f.write( str(random_paths) )
f.close()