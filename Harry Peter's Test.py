'''
https://pintia.cn/problem-sets/951072707007700992/problems/985411779057623040
'''

import copy
# 找出最大值中最小的动物的编号
def minmax(D):
	a = []
	for i in range(len(D)):
		maxnum = 0
		for j in range(len(D)):
			if i!=j and D[i][j] > maxnum:
				maxnum = D[i][j]
		if maxnum == float('inf'):
			print(0)
			return
		a.append(maxnum)
	minmax = float('inf')
	for i in range(len(a)):
		if a[i] < minmax:
			minmax = a[i]
			odr = i
	print(odr+1,minmax)

# 多源最小路径Floyd
def Floyd(G):
	N = len(G)
	D = copy.deepcopy(G)
	for k in range(N):
		for i in range(N):
			for j in range(N):
				if (D[i][k] + D[k][j] < D[i][j]) and i != j:
					D[i][j] = D[i][k] + D[k][j]
	return D

def main():
	tep = input().split()
	N = int(tep[0])
	M = int(tep[1])
	# 用邻接矩阵表示图
	G = [[float('inf')]*N for x in range(N)]
	for i in range(M):
		tep = input().split()
		G[int(tep[0])-1][int(tep[1])-1] = int(tep[2])
		G[int(tep[1])-1][int(tep[0])-1] = int(tep[2])
	D = Floyd(G)
	minmax(D)

if __name__ == '__main__':
	main()