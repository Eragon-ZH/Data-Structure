'''
https://pintia.cn/problem-sets/951072707007700992/problems/987660874267004928
最小生成树——Kruskal算法
'''

def find(a):
	while parent[a] >= 0:
		a = parent[a]
	return a

def merge(a,b):
	parent[find(a)] = find(b)	
	
def Kruskal():
	MST = []
	dist = 0
	parent = [-1] * N
	# 直到所有边都选取（最小生成树不存在）或选取了足够的边
	while len(G)!=0 and len(MST) != N-1:
		# 每次取出权重最小的边
		E = G.pop(0)
		# 如果两个顶点不在同一个集合则选取这条边，并把两个集合合并
		if find(E[1]) != find(E[2]):
			dist += E[0]
			merge(E[1],E[2])
			MST.append(E)
	if len(MST) != N-1:
		return False
	return dist

tep = input().split()
N = int(tep[0])
W = int(tep[1])
G = []	
parent = [-1] * N
	
def main():
	for i in range(W):
		tep = input().split()
		a = int(tep[0]) - 1
		b = int(tep[1]) - 1
		weight = int(tep[2])
		# 记录所有的边并按权值排序
		G.append([weight,a,b])
	G.sort()
	dist = Kruskal()
	if dist == False:
		print(-1)
	else:
		print(dist)
	
if __name__ == '__main__':
	main()