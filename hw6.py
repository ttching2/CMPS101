"""
	Author: Trevor Ching and Sean Torres
	UCSC ID: ttching and semtorre
"""
import heapq
"""
	Binary search tree implementation
"""
class BSTree:
	#Node class - holds all the words from the reviews and their frequency
	class Node:
		left = None									#The left child node
		right = None								#The right child node
		parent = None								#The parent node that connects to this node
		def __init__(self, key, value = 0):
			self.key = key
			self.value = value
			
	def __init__(self, root = None):
		self.root = root							#Initialize empty root for an empty tree
		self.heap = [(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,'')]
		
		
	#Function to insert a key into the tree or increment a words frequency
	def insert(self,key,value):
		node = self.Node(key,value)					#Creates a node with the word as the key and a value of 1 to increment the frequency
		#If the tree is empty set the node to be the root node
		if self.root == None:
			self.root = node
		#Else the tree isnt empty find where to place the node in the tree
		else:
			current = self.root						#Start at the root node 
			#Goes down the tree to where the new node should belong in this tree
			while True:
				parent = current					#The parent node of the next node we are going to
				#If the current node we are at has the same key as the one we have increment the frequency value by 1
				if current.key == key:
					current.value += value
					break
				#If the key we have comes after the current key Alphabetically then we go to the right node
				elif node.key > current.key:
					current = current.right			#Changes the current node to the right child node
					#If there is no right child node then we set this to be the right child node
					if current is None:
						parent.right = node
						node.parent = parent
						break
				#The key comes before the current key alphabetically we go to the left node
				else:
					current = current.left
					if current is None:
						parent.left = node
						node.parent = parent
						break
						
	#Delete a specific node from the tree, there are 3 cases to consider when deleting a node
	#When the node has no children, when the node has one child node and when the node
	#has two children node
	def delete(self,key):
		current = self.find(key)					#Gets the node we want to delete
		#If the node can not be found just return
		if current is None:
			return
		#If the node has 2 children nodes
		if current.left is not None and current.right is not None:
			swap = self.successor(key)				#Find the node that can replace the current node to delete
			#If the node to delete is the root node
			if(key == self.root.key):
				self.root = swap					#Set the root node to the successor node
				#Remove the refernce to the successor by going to its parent node
				#and removing it from the parents child
				if swap.key > swap.parent.key:
					swap.parent.right = None		#If the successor node is greater than the parent node then remove the parents right child node
				else:
					swap.parent.left = None			#If the successor node is less than the parent node then remove the parents left child node
				swap.parent = None					#The successor node is now the root and so it has no parent node
				swap.left = current.left			#Swap the roots left child to the successor
				swap.right = current.right			#Swap the roots right child to the successor
				return
			#If the key is greater than the parents key
			elif current.key > current.parent.key:
				current.parent.right = swap			#Switch the parent, of the node to delete, right child to the successor
			#If the key is less than the parents key
			else:
				current.parent.left = swap			#Switch the parent, of the node to delete, left child to the successor
			#Remove the reference to the successor node from the parent node
			if swap.parent.left == swap:
				swap.parent.left = None
			else:
				swap.parent.right = None
			swap.parent = current.parent			#Change the successor's parent node to the current node's parent node
			swap.left = current.left				#Change the successors left child to the current nodes left child
		#If the node only has one child
		elif current.left is not None or current.right is not None:
			#If the current node is a right child of the parent and the current node has a left child
			if current.parent.key < current.key and current.left is not None:
				current.parent.right = current.left	#Set the parents right node to the current node's left child
			#If the current node is a right child of the parent and the current node has a right child
			elif current.parent.key < current.key and current.right is not None:
				current.parent.right = current.right#Set the parents right node to the current node's right child
			#If the current node is a left child of the parent and the curent node has a left child
			elif current.parent.key > current.key and current.left is not None:
				current.parent.left = current.left	#Set the parents left node to the current node's left child
			#If the current node is a left child of the parent and the currentnode has a right child
			else:
				current.parent.left = current.right	#Set the parents left node to the current node's right child
		#If the node has no children
		else:
			#If the current node is a right child of the parent node
			if current.parent.key < current.key:
				current.parent.right = None			#Remove refernce to the current node
			#If the current node is a left child of the parent node
			else:
				current.parent.left = None			#Remove refernce to the current node
			
	#Finds a node with the key and returns it
	def find(self,key):
		current = self.root							#Start at the root node
		#While the current node's key is not what we wnt
		while key != current.key:
			#If the key is before the current node's key go to the left node
			if key < current.key:
				current = current.left
			#If the key is after the current node's key go to the right now
			else:
				#print(current.key)
				current = current.right
			#If we have reached the bottom of the tree and haven't found the node
			if current is None:
				break
		return current

	#Finds the successor node to a node with the key
	def successor(self,key):
		current = self.find(key)					#Finds the key we are searching a successor for first
		#Start by going to the right child first because it comes after the current node's key
		if current.right is not None:
			current = current.right
		#Then look for the node with the smallest key in the right subtree by going all the way down left
		while current.left is not None:
			current = current.left
		return current
		
	#Performs the inordertraversal through recursion
	def inOrder(self,node):
		#Base case if we reach to the bottom of the tree
		if node is None:
			return
		self.inOrder(node.left)						#Visit the left node first
		print(node.key," ",node.value)				#Prints out the info for the current node
		self.inOrder(node.right)					#Visits the right node
		
	#Calls inordertraversal
	def inOrderTraversal(self):
		self.inOrder(self.root)
	######################################
	x = []
	def thing(self,node):
		if node is None:
			return
		self.x.append(node.key)
		self.thing(node.left)
		self.thing(node.right)
		
	def get(self):
		self.thing(self.root)
		return self.x
	def freq(self):
		return self.findFreq(self.root)
		
	#i = 0
	min = 0
	size = 0
	#Finds the top 20 frequency
	def findFreq(self,node):
		if node is None:
			return
		if node.value > self.min:
			heapq.heapreplace(self.heap,(node.value,node.key))
			heapq.heapify(self.heap)
			self.min = self.heap[0][0]
		self.size += 1
		self.findFreq(node.left)
		self.findFreq(node.right)
		
	def getSize(self):
		return self.size
		
	def getHeap(self):
		#self.i = 0
		return self.heap
		
	def clear(self):
		self.size = 0
		self.heap = [(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,''),(0,'')]
					
"""	
lowtree = RBTree()	
treedata = [("Foxtrot",20), ("Delta",15), ("Echo",17),
                         ("Alpha",5), ("Bravo",10), ("Charlie",12),
                         ("Golf",22), ("Hotel",25), ("India",27)]
x = []
for element in treedata:
	lowtree.insert(key=element[0], value=element[1])
	x.append(element[0])

hightree = RBTree()
hightree.insert("Foxtrot",43)
hightree.insert("Dog",32)
hightree.insert("Chocolate",42)
hightree.insert("Mackeral",54)
hightree.insert("Zoo",23)
hightree.insert("Alpha",54)
hightree.insert("Nope",23)
hightree.insert("Bad",12)
hightree.insert("Pink",54)
hightree.insert("Golf",34)
"""
lowtree = BSTree()
hightree = BSTree()
stopwords = set()
stoptext = 'stopwords.txt'
#Reads in stopwords
with open(stoptext,'r') as f:
	for line in f:
		line = line.rstrip('\n')
		stopwords.add(line)
#Inserts stopwords
def insert(tree = BSTree(),lines = []):
	lines = lines.split()
	for i in range(len(lines)):
		if lines[i] not in stopwords:
			tree.insert(lines[i],1)
	
#Reads in the reviewsresults	
#reviews = 'finefoods_cleaned.txt'
reviews = 'test.txt'
with open(reviews,'r') as f:
	for line in f:
		#1-3 star rating
		if int(line.split(":")[0]) <= 3:
			insert(lowtree,line.split(':')[1])
		#4-5 star rating
		else:
			insert(hightree,line.split(':')[1])		
			
f = open('frequent.txt','w')
lowtree.freq()
hightree.freq()
f.write("Size "+str(hightree.size))
l = lowtree.getHeap()
h = hightree.getHeap()
#Top 20 words from both trees

f.write("\nHigh tree          Low tree\n")
for i in range(len(l)):
	print(h[i][0]," ",h[i][1],"          ",l[i][0]," ",l[i][1])
	input = str(str(h[i][0])+" "+str(h[i][1])+"          "+str(l[i][0])+" "+str(l[i][1])+"\n")
	f.write(input)

hightree.clear()
x = []
x = lowtree.get()
for i in range(len(x)):
	hightree.delete(x[i])
hightree.freq()
size = hightree.size
print("\nThere are now ",size," distinct words left in high ratings")
input = str("\nThere are now "+str(size)+" distinct words left in high ratings")
f.write(input)
h = hightree.getHeap()
print("\nNew High tree")
f.write("\nNew High tree\n")
for i in range(len(h)):
	print(h[i][0]," ",h[i][1])
	input = str(str(h[i][0])+" "+str(h[i][1])+"\n")
	f.write(input)

