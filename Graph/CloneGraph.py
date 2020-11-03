class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

#                   1-------------2
#                   |             |
#                   |             |
#                   |             |
#                   4-------------3
#

#define nodes of the graph
node1= Node(1)
node2= Node(2)
node3= Node(3)
node4= Node(4)

#set its neighbors
node1.neighbors= [node2, node4]
node2.neighbors= [node3, node1]
node3.neighbors= [node2, node4]
node4.neighbors= [node3, node1]

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        else:
            hash={}
            hold_node=[]
            queue=[node]
            #make copy and store it in the hash map
            while len(queue) !=0:
                get_node= queue.pop()
                if len(get_node.neighbors) !=0:
                    for neigh in get_node.neighbors:
                        if neigh not in hash:
                            queue.append(neigh)

                # remove all the connections
                hold_neigh= get_node.neighbors
                #set neighbors as empty list
                get_node.neighbors=[]

                # make deep copy of the node
                newnode= Node(get_node.val)

                #restore connection
                get_node.neighbors= hold_neigh

                #make entry in the hash
                hash[get_node]= newnode
                if get_node not in hold_node:
                    hold_node.append(get_node)

            # make all the connections for the copied nodes
            for orinode in hold_node:
                get_deepcopy= hash[orinode]
                neighbors=[]

                #create neighbors
                if len(orinode.neighbors)!=0:
                    for neigh in orinode.neighbors:
                        #get copy of the neighbors from the hash map
                        get_copy= hash[neigh]
                        neighbors.append(get_copy)
                get_deepcopy.neighbors=neighbors.copy()

            return hash[node]















obj=Solution()
obj.cloneGraph(node1)
