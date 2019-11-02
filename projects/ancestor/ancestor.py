
def earliest_ancestor(ancestors, starting_node):
    from graph import Graph
    from graph import Stack, Queue
    g = Graph()
    for ta in ancestors:
      g.add_vertex(ta[0])
      g.add_vertex(ta[1])
      g.add_edge(ta[1],ta[0])

    trees = []
    s = Stack()
    s.push([starting_node])
    
    while s.size()>0:
      current_point = s.stack[-1][-1]
      
      joins = g.vertices[current_point]
      if joins == set():
        trees.append(s.pop())
      else:
        temp_list = []
        for j in joins:
          _ = [x for x in s.stack[-1]]
          _.append(j)
          temp_list.append(_)
        s.pop()
        for tl in temp_list:
          s.push(tl)
      #s.pop()
    tree_dict = {}
    for t in trees:
        if len(t) not in tree_dict.keys():
            tree_dict[len(t)] = t
        else:
            last_new = t[-1]
            last_old = tree_dict[len(t)][-1]
            if last_new<last_old:
                tree_dict[len(t)] = t
            else:
                pass
    ret = tree_dict[max(tree_dict.keys())][-1]
    if ret == starting_node:
        return -1
    else:
        return ret