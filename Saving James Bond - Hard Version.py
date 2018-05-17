'''
https://pintia.cn/problem-sets/951072707007700992/problems/985411848322359296
'''
# 是否能跳到另一个鳄鱼
def canJump(a,b,D):
	if (a[0]-b[0])**2 + (a[1]-b[1])**2 <= D**2:
		return True
	else:
		return False
# 是否能跳上岸
def isSafe(a,D):
	if a[0] <= (-50+D) or a[0] >= (50-D):
		return True
	if a[1] <= (-50+D) or a[1] >= (50-D):
		return True
	return False	
# 单源最短路径，类似BFS，利用dist存储路径长度，path存储路径
def minBFS(crocodiles,i,D,queue,dist,path):
	answer = False
	# 为了避免转回第一个点，课程里的代码没有考虑这个问题但是sample就有这个问题
	first = i
	queue.append(i)
	lastcrocodile = None
	dist[first] = 0
	while len(queue) != 0:
		v = queue.pop(0)
		for j in range(len(crocodiles)):
			# 对所有邻接点进行遍历
			if v != j and canJump(crocodiles[v],crocodiles[j],D) and j != first:
				# dist为-1说明没有访问过，dist等于前一个+1，路径等于前一个点
				if dist[j] == -1:
					dist[j] = dist[v]+1
					path[j] = v
					queue.append(j)
				if isSafe(crocodiles[j],D):
					lastcrocodile = j
					answer = True
					return answer,lastcrocodile,path,dist
	return answer,lastcrocodile,path,dist

# 借助堆栈输出路径以及路径长度	
def printAnswer(lastcrocodile,path,crocodiles,dist):
	print(dist[lastcrocodile]+2)
	queue = []
	queue.append(lastcrocodile)
	while path[lastcrocodile] != -1:
		queue.append(path[lastcrocodile])
		lastcrocodile = path[lastcrocodile]
	while len(queue) != 0:
		tem = queue.pop()
		print(crocodiles[tem][0],crocodiles[tem][1])
		
def main():
	tep = input().split()
	N = int(tep[0])
	D = int(tep[1])
	# 邦德牛逼到能一步跳上岸直接退出
	if D > 42.5:
			print(1)
			return
	# 直接用列表存储鳄鱼坐标
	crocodiles = []
	for i in range(N):
		tep = input().split()
		x = int(tep[0])
		y = int(tep[1])
		# 如果鳄鱼在岛上或者岸上不计算在内
		if (x**2+y**2<7.5**2) or abs(x)>50 or abs(y)>50:
			N -= 1
		else:
			crocodiles.append((x,y))
	answer = False
	distance = float('inf')
	# 题目要求路径长度相同时输出第一步最小的，因此需要对第一步所有的点按距离进行排序
	firstlist = {}
	for i in range(N):
		if (crocodiles[i][0]**2+crocodiles[i][1]**2) < pow(7.5+D,2):
			firstlist[i] = crocodiles[i][0]**2+crocodiles[i][1]**2
	firstlist = sorted(firstlist.items(),key=lambda x:x[1])
	
	for k in firstlist:
		i = k[0]
		queue = []
		dist = [-1] * N
		path = [-1] * N
		answer,lastcrocodile,path,dist = minBFS(crocodiles,i,D,queue,dist,path)
		if answer == True:
			printAnswer(lastcrocodile,path,crocodiles,dist)
			return
	if answer == False:
		print(0)
			
main()
