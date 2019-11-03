class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def traverse_cliques(cliques, parent_world, starting_point = 0):
  traverses = []
  for clique in cliques:
    my_room_graph = {}
    for item in clique:
      my_room_graph[item] = parent_world.rg[item]
    
    for key in my_room_graph:
      clean_dict = {}
      directions = my_room_graph[key][1]
      #print(directions)
      for d in directions.keys():
        if directions[d] in clique:
          #print(directions[d])
          clean_dict[d] = directions[d]
        else:
          pass
      my_room_graph[key] = [my_room_graph[key][0],clean_dict]
    #print(my_room_graph)
    clique_world = World()
    clique_world.loadGraph(my_room_graph,start_room = min(list(my_room_graph.keys())))
    #clique_world.printRooms
    a,b = traverse(clique_world, starting_point = starting_point)
    _ = [a,b,clique_world]
    traverses.append(_)
  for trav in traverses:
    #print(trav[0][-1],trav[0][0])
    _ = backtrack(trav[2],trav[0][-1],trav[0][0])
    __ = dirs_for_path(_,trav[2])
    trav[0] += _[1:-1]
    trav[1] += __[1:-1]
    
  return traverses

def backtrack(world, starting_vertex, destination_vertex):
        """breadth firsf search to find shortest way"""
        q = Queue()
        q.enqueue([starting_vertex])
        
        while destination_vertex not in q.queue[0]:
          current_point = q.queue[0][-1]
          joins = world.rg[current_point][1].values() #self.vertices[current_point]
          for j in joins:
            _ = [x for x in q.queue[0]]
            _.append(j)
            q.enqueue(_)
          q.dequeue()

        return q.queue[0]

def dirs_for_path(my_list,world):
  point = my_list[0]
  dirs = []
  for i in range(1,len(my_list)):
    for d in world.rg[point][1]:
      if world.rg[point][1][d]==my_list[i]:
        dirs.append(d)
  return dirs

def de_looper(trav, world, max_depth = 15 ):
  better_list = [None] * len(trav)
  index = 0
  while index < len(trav):
    point = trav[index]
    print(' pt ',point, end='')
    i = index + 1
    while i < len(trav) and point != trav[i] and (i-index)<max_depth:
      i +=1
    if i  < len(trav):
      my_slice = trav[index : i+1]
      tt = traverse_cliques([set(my_slice)],world, starting_point = point)
      if (len(tt[0][0]) + 1 )< i - index:
        print('tt0',tt[0][0], 'i - index is', i - index)
        better_list[index:index+len(tt[0][0])] = tt[0][0] + [point]
        index = i
      else:
        better_list[index:index+i] = trav[index:index+i]
        index +=1
    elif (index == len(trav)-1) and (i==len(trav)):
      better_list[index-1:] = trav[index-1:]
      index +=1
    else:
      index +=1
  better_list = [x for x in better_list if x is not None]
  return better_list