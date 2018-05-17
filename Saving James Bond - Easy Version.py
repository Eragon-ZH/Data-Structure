'''
https://pintia.cn/problem-sets/951072707007700992/problems/982816780864188416
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
# 深度优先遍历 用answer来记录是否能成功到岸
def DFS(crocodiles,visit,i,D,answer):
	visit[i] = True
	if isSafe(crocodiles[i],D):
		answer = True
	else:
		for j in range(len(crocodiles)):
			if visit[j] == False and canJump(crocodiles[i],crocodiles[j],D):
				answer = DFS(crocodiles,visit,j,D,answer)
				if answer == True:
					break
	return answer

def main():
	tep = input().split()
	N = int(tep[0])
	D = int(tep[1])
	# 直接用列表存储鳄鱼
	crocodiles = []
	for i in range(N):
		tep = input().split()
		x = int(tep[0])
		y = int(tep[1])
		crocodiles.append((x,y))
	answer = False
	for i in range(len(crocodiles)):
		# 单独判断第一跳
		if (crocodiles[i][0]**2+crocodiles[i][1]**2) < pow(7.5+D,2):
			visit = [False]*len(crocodiles)
			answer = DFS(crocodiles,visit,i,D,answer)
			if answer == True:
				print('Yes')
				break
	if answer == False:
		print('No')
			
main()
