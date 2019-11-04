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
# Fill this out
import random
def traverse(world):
  reverser = {'n':'s','s':'n','e':'w','w':'e'}
  traversal = []
  traversal_direction=[]
  visited = []
  s = Stack()
  p = Player('p',world.rooms[0])
  while len(visited) < len (roomGraph):
    current_room = p.currentRoom.id
    traversal.append(current_room)
    if current_room not in visited:
      visited.append(current_room)
    neighbors = roomGraph[current_room][1]
    neighbors = [x for x in neighbors if neighbors[x] not in visited]
    
    if neighbors !=[]:
        s.push(current_room)
        move = random.choice(neighbors)
        traversal_direction.append(move)
        p.travel(move)
    else:
        print('back')
        last_room = roomGraph[s.pop()][1]
        #print(last_room)
        last_move = [x for x in last_room if last_room[x]==p.currentRoom.id][0]
        move = reverser[last_move]
        traversal_direction.append(move)
        p.travel(move)
  
  return traversal, traversal_direction
