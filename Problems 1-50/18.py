# Problem 18 - 6/23/17

class Node:
	def __init__(self,val,left,right,parent,pathCost):
		self.val = val
		self.left = left
		self.right = right
		self.pathCost = pathCost
		
	def setLeftChild(self,left):
		self.left = left
		
	def setRightChild(self,right):
		self.right = right
		
	def setParent(self,parent):
		self.parent = parent
		self.pathCost = parent.pathCost + self.val
	
f = open('18_input.txt','r')

endCost = 100
end = Node(endCost,None,None,None,float('inf'))

root = Node(endCost-int(f.readline()),None,None,None,0)
root.pathCost = root.val

above,cur = [root],[]
for line in f:
	cur = [Node(endCost-int(a),None,None,None,float('inf')) for a in line.split()]
	for i in range(len(cur)):
		if i > 0:
			above[i-1].setRightChild(cur[i])
		if i < len(cur)-1:
			above[i].setLeftChild(cur[i])
	above = cur
for node in cur:
	node.setLeftChild(end)
	node.setRightChild(end)
	
inSet = [root]
while not end in inSet:
	minCost = float('inf')
	candidate,candidateP = None,None
	for node in inSet:
		for child in [node.left,node.right]:
			if not child in inSet:
				cost = node.pathCost+child.val
				if cost < minCost:
					minCost,candidate,candidateP = cost,child,node
	candidate.setParent(candidateP)
	inSet.append(candidate)
	
child = end
total = 0
while child != root:
	print(endCost-child.parent.val)
	total += endCost-child.parent.val
	child = child.parent
	
print(total)