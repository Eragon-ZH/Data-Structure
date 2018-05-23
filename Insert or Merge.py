'''
https://pintia.cn/problem-sets/951072707007700992/problems/990061372701700096
最大N，Mg，后面N位没变化
卡住Mg检查片段长度的错误算法，连续长度有3种 没过
'''
# 插入排序
def InsertSort(myList,i):
	length = len(myList)
	key = myList[i]
	j = i - 1
	while j >= 0:
		if myList[j] > key:
			myList[j+1] = myList[j]
			myList[j] = key
		j -= 1
	return myList
# 合并两个列表
def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result	
# 判断是否是插入排序	
def isInsert(startList,middleList):
	tep = -float('inf')
	for i in range(len(middleList)):
		if middleList[i]>=tep:
			tep = middleList[i]
		else:
			break
	if startList[i:] == middleList[i:]:
		isInsert = True
	else:
		isInsert = False
	return i,isInsert
# 获取mg检查片段长度
def getN(middleList,N):
	i = 2
	while i<N:
		flag = 0
		tep = -float('inf')
		for j in range(i,N,2*i):
			if middleList[j-1] < middleList[j]:
				pass
			else:
				flag = 1
		if flag == 1:
			break
		i *= 2
	return i
	
def main():
	N = int(input())
	startList = list(map(int,input().split()))
	middleList = list(map(int,input().split()))
	answer = isInsert(startList,middleList)
	if answer[1]:
		print('Insertion Sort')
		endList = InsertSort(middleList,answer[0])
	else:
		print('Merge Sort')
		l = getN(middleList,N)
		endList = []
		start = 0
		# 再做一步归并排序，就是对片段长度为N的列表两两合并一次
		while start+2*l<=N:
			a = middleList[start:start+l]
			b = middleList[start+l:start+l+l]
			# print(a,b,endList)
			endList += merge(a,b)
			start += 2*l
		a = middleList[start:start+l]
		b = middleList[start+l+1:]
		endList += merge(a,b)
		# print(a,b,endList)
	for i in range(len(endList)-1):
		print(endList[i],end=' ')
	print(endList[-1])

if __name__ == '__main__':
	main()