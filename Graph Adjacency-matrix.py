'''
https://pintia.cn/problem-sets/951072707007700992/problems/982816722043277312
'''

def creatGraph(N):
	G = [ [0]*N for x in range(N) ]
	return	G
	
def appendGraph(G,v,w):
	G[v][w] = 1
	G[w][v] = 1
# 深度优先
def DFS(G,v,visit):
	visit[v] = True
	print(v,end = ' ')
	for j in range(len(G[v])):
		# 相邻结点有未访问过的就访问，没有的话原路返回再看有没有未访问过的相邻结点
		if G[v][j]==1 and visit[j] == False: 
			DFS(G,j,visit)	
# 广度优先	
def BFS(G,v,queue,visit):
	visit[v] = True
	print(v,end=' ')
	# 双端队列暂存
	queue.append(v)
	while len(queue) != 0:
		v = queue.pop(0)
		# pop出一个结点，再将所有他相邻的结点存入队列中
		for j in range(len(G[v])):
			if G[v][j]==1 and visit[j] == False:
				print(j,end=' ')
				visit[j] = True
				queue.append(j)

def main():
	tem = input().split()
	N = int(tem[0])
	E = int(tem[1])
	G = creatGraph(N)
	for i in range(E):
		tep = input().split()
		appendGraph(G,int(tep[0]),int(tep[1]))
	# 记录该结点是否被访问过
	visit = [False]*len(G)
	for i in range(len(G)):
		if visit[i] == False:
			print('{ ', end='' )
			DFS(G,i,visit)
			print('}')
			
	visit = [False]*len(G)
	queue = []
	for i in range(len(G)):
		if visit[i] == False:
			print('{ ',end='')
			BFS(G,i,queue,visit)
			print('}')
			
main()