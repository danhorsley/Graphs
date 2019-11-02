from util import Stack

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        variability = avgFriendships//2

        import random
        for n in range(numUsers):
          self.addUser(n)
        for user in self.users:
            #using adjustment factor to bring average back into line
          num_friends = random.choice(range(avgFriendships-variability,avgFriendships+variability)) - (2*avgFriendships//10)
          if user in self.friendships.keys():
            existing_friends_len = len(self.friendships[user])
            existing_friends = set(self.friendships[user])
          else:
            existing_friends_len = 0
            existing_friends = set()
          
          num_friends = max(0,num_friends-existing_friends_len)
          users_ex_user = set(self.users.keys())
          users_ex_user.remove(user)
          for ef in existing_friends:
            users_ex_user.remove(ef)
          user_friends = set(random.sample(users_ex_user,num_friends))
          for friend in user_friends:
            self.addFriendship(user,friend)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {} 
        current_point = userID
        s = Stack()
        s.push([userID])
        while s.size()>0:
          current_point = s.stack[-1][-1]
          joins = self.friendships[current_point]
          new_paths = []
          for j in joins:
            if j not in visited.keys():
                _ = [x for x in s.stack[-1]]
                _.append(j)
                new_paths.append(_)
            else:
                _ = [x for x in s.stack[-1]]
                _.append(j)
                if len(_)<len(visited[j]):
                    visited[j]=_
                else:
                    pass
          placeholder = s.pop()
          if current_point not in visited.keys():
            visited[current_point] = placeholder
          else:
            if len(visited[current_point])> len(placeholder):
              visited[current_point] = placeholder
            else:
              pass
          for np in new_paths:
            s.push(np)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
