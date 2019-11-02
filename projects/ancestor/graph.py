"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices.keys():
          self.vertices[vertex] = set()
        else:
          pass
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices.keys():
          #self.vertices[v2].add(v1)  #graph is directed so removed
          self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        if starting_vertex is None:
          return None
        my_q = Queue()
        visited = [starting_vertex]
        my_q.enqueue(starting_vertex)
        while len(my_q.queue) > 0:
          point = my_q.queue[0]
          joins = self.vertices[point]
          for j in joins:
            if j not in visited:
              my_q.enqueue(j)
              visited.append(j)
          print(my_q.dequeue())


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if starting_vertex is None:
          return None
        my_s = Stack()
        visited = [starting_vertex]
        my_s.push(starting_vertex)
        while len(my_s.stack) > 0:
          point = my_s.stack[-1]
          joins = self.vertices[point]
          print(my_s.pop())
          for j in joins:
            if j not in visited:
              my_s.push(j)
              visited.append(j)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        visited.append(starting_vertex)
        joins = self.vertices[starting_vertex]
        if joins is None:
          return None
        for j in joins:
          if j in visited:
            pass
          else:
            self.dft_recursive(j,visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        
        while destination_vertex not in q.queue[0]:
          current_point = q.queue[0][-1]
          joins = self.vertices[current_point]
          for j in joins:
            _ = [x for x in q.queue[0]]
            _.append(j)
            q.enqueue(_)
          q.dequeue()

        return q.queue[0]


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        
        while destination_vertex not in s.stack[-1]:
          current_point = s.stack[-1][-1]
          
          joins = self.vertices[current_point]
          if joins is None:
            s.pop()
          else:
            temp_list = []
            for j in joins:
              _ = [x for x in s.stack[-1]]
              _.append(j)
              temp_list.append(_)
            for tl in temp_list:
              s.push(tl)
          #s.pop()

        return s.stack[-1]





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
