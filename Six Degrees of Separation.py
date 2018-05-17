'''
https://pintia.cn/problem-sets/951072707007700992/problems/982816837709590528
最大N最大M超时
'''
# 结点，用列表存储与该结点相连的结点
class Vertex():
	def __init__(self,key):
		self.id = key
		self.connections = []
		
	def addNeighbor(self,nbr):
		self.connections.append(nbr)
	
	# def __str__(self):
		# return str(self.id) + 'connectedTo' + str([x.id for x in self.connections])

# 图，用字典存储所有节点	
class Graph():
	def __init__(self):
		self.vertList = {}
	
	def addVertex(self,key):
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex
	
	# 添加边，若是新的结点先添加结点
	def addEdge(self,a,b):
		if a not in self.vertList:
			aVertex = self.addVertex(a)
		else:
			aVertex = self.vertList[a]
		if b not in self.vertList:
			bVertex = self.addVertex(b)
		else:
			bVertex = self.vertList[b]
		self.vertList[a].addNeighbor(bVertex)
		self.vertList[b].addNeighbor(aVertex)

# 广度优先		
def BFS(vertex,visit,queue,G):
	visit[vertex.id-1] = True
	count = 1
	# level表示遍历的深度
	level = 0
	last = vertex.id
	queue.append(vertex)
	while len(queue) != 0:
		V = queue.pop(0)
		for i in V.connections:
			if visit[i.id-1] != True:
				visit[i.id-1] = True
				queue.append(i)
				count += 1
				tail = i.id
		# last表示当前层的最后一个结点
		# 用tail进行跟踪，如果pop出来的V等于last的话，用tail来更新last并使层数加1
		if V.id == last:
			level += 1
			last = tail	
		if level == 6:
			break
	return count

def main():
	tep = input().split()
	N = int(tep[0])
	M = int(tep[1])
	G = Graph()
	for i in range(M):
		tep = input().split()
		a = int(tep[0])
		b = int(tep[1])
		G.addEdge(a,b)
	
	for i in range(1,N+1):
		visit = [False] * N
		queue = []
		count = BFS(G.vertList[i],visit,queue,G)
		print("{}: {:.2%}".format(i,count/N))
		
if __name__ == '__main__':
	main()