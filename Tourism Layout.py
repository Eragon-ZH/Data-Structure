'''
https://pintia.cn/problem-sets/951072707007700992/problems/985411926680264704
最大N和M超时，复杂度为O(V**2+E),可以在找未收录顶点的最小dist时采用最小堆
'''

def Dijkstra(G,S,dist,cost,collected):
	# 初始化，dist和cost都为0，第一个结点的collected为True
	# 更新第一个结点的相邻结点的dist和cost，进入循环
	dist[S] = 0
	cost[S] = 0
	collected[S] = True	
	for i in range(len(G[S])):
		if G[S][i] != float('inf'):
			dist[i] = G[S][i][0]
			cost[i] = G[S][i][1]
	while True:
		V = float('inf')
		min = float('inf')
		# 找到为收录结点中dist最小的元素V
		for i in range(len(dist)):
			if collected[i]==False and dist[i]<min and dist[i]!=0:
				min = dist[i]
				V = i 
		if min == float('inf'):
			break
		collected[V] = True
		# 对于V的每一个邻接点w
		for w in range(len(G[V])):
			if G[V][w] != float('inf'):
				# 如果V的距离加上V到w的距离小于w的距离 说明经过V到w更近
				# 此时V和w一定紧邻
				# 更新w的距离 同时更新cost
				if collected[w] == False:
					if (dist[V]+G[V][w][0] < dist[w]):
						dist[w] = dist[V] + G[V][w][0]
						cost[w] = cost[V] + G[V][w][1]
					# 题目要求相同距离输出花费最少的
					elif (dist[V]+G[V][w][0]==dist[w]) and (cost[V]+G[V][w][1]<cost[w]):
						cost[w] = cost[V] + G[V][w][1]
	return dist,cost
		

def main():
	tep = input().split()
	N = int(tep[0])
	M = int(tep[1])
	S = int(tep[2])
	D = int(tep[3])
	G = [[float('inf')]*N for x in range(N)]
	for i in range(M):
		tep = input().split()
		a = int(tep[0])
		b = int(tep[1])
		distance = int(tep[2])
		cost = int(tep[3])
		# 邻接矩阵的每一个元素存储距离和花费
		G[a][b] = [distance,cost]
		G[b][a] = [distance,cost]
	collected = [False] * N
	dist = [float('inf')] * N
	cost = [float('inf')] * N
	dist,cost = Dijkstra(G,S,dist,cost,collected)
	print(dist[D],cost[D])
	
if __name__ == '__main__':
	main()