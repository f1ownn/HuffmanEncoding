import heapq
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None            # Node class having a data and two pointers towards left and right
        self.right = None
    def __gt__(self,other):
        return self.data > other.data
    def __lt__(self,other):             # Implementing comparable in order to compare two nodes by their data when 
                                        # put inside a min heap.
        return self.data < other.data
    def __eq__ (self,other):
        return self.data == other.data



def huffmanCodes(S,f,N):
    f = sorted(f)
                    # S = String to compress,  f = Frequency of all the letters occuring in the string, N = Length of String
    heap = []
    for freq in f:                      
        heapq.heappush(heap,Node(freq)) 
        
        
    while len(heap)>= 2:
        x1 = heapq.heappop(heap)
        x2 = heapq.heappop(heap)
                                            # Huffman Algorithm Implemented to construct the tree, 
                                            # Then the codes returned in a pre order fashion.
        mergednode = Node(x1.data + x2.data)
        mergednode.left = x1
        mergednode.right = x2
        heapq.heappush(heap,mergednode)
        
    rootnode = heap[0]
    ans = []
    def preorder(root,s):
        if not root.left and not root.right:
            ans.append(s)
            return
        else:
                
            preorder(root.left, s + '0')
                
                
            preorder(root.right, s + '1')
                
    preorder(rootnode,'')
    return ans

#------------------------------------------------------------------OVER-----------------------------------------------------------------------------------------------#