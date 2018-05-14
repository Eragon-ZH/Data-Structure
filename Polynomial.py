#多项式加法和乘法
#获取多项式非零项的项数以及非零项的指数和系数
def getDuo():
	li = input().split()
	duo = []
	for i in range(len(li)):
		li[i] = int(li[i])
	k = li.pop(0)
	for i in range(len(li)):
		if i % 2 == 0:
			duo.append([li[i+1],li[i]])
	return duo
#多项式加法
def duoAdd(duo1,duo2):
	result = []
	#记录合并的位置
	ilist = []
	jlist = []
	for i in range(len(duo1)):
		for j in range(len(duo2)):
			if duo1[i][0] == duo2[j][0]:
				result.append([duo1[i][0],duo1[i][1]+duo2[j][1]])
				ilist.append(i)
				jlist.append(j)
	#删除列表中已经合并的项
	for i in range(len(ilist)-1,-1,-1):
		del duo1[ilist[i]]
	for j in range(len(jlist)-1,-1,-1):
		del duo2[jlist[j]]
	result += duo1
	result += duo2
	return result
	
#多项式乘法
def duoMulti(duo1,duo2):
	result = []
	#相乘
	for i in range(len(duo1)):
		for j in range(len(duo2)):
			result.append([duo1[i][0]+duo2[j][0],duo1[i][1]*duo2[j][1]])
	#合并同类项
	i = 0
	while i < len(result):
		j = i + 1
		while j < len(result):
			if result[i][0] == result[j][0]:
				result[i][1] += result[j][1]
				result.pop(j)
			j += 1
		i += 1
	return result
#输出
def priDuo(li):
	result = mergeSort(li)
	# print(result)
	if len(result) > 1:
		#如果最后一项为[0,0]则删除
		if result[-1][0] == 0 and result[-1][1] == 0:
			result.pop(-1)
		#删除系数为0的项
		for i in range(len(result)-1,-1,-1):
			if result[i][1] == 0 and result[i][0] != 0:
				result.pop(i)
	if len(result) > 1:
		#依次输出每一项的系数和指数，空格隔开，结尾没有空格
		for i in range(len(result)-1):
			print(result[i][1],result[i][0],end=' ')
		print(result[-1][1],result[-1][0])
	#恰巧为零多项式
	else:
		print('0','0')
#归并排序
def mergeSort(li):
    if len(li) == 1:   #分到只有一个元素为止
        return li
    mid = len(li)//2    #将列表分为左右两个部分
    left = li[:mid]
    right = li[mid:]
    left1 = mergeSort(left) #接着将左右两部分分别再分为左右两部分
    right1 = mergeSort(right)
    return merge(left1,right1) 
#进行合并
def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:   #将两个列表按照从小到大进行合并
        if left[0][0] >= right[0][0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left  #任一列表为空列表后跳出循环，将result后直接连上剩余的列表
    result += right
    return result

def main():
	duo1 = getDuo()
	duo2 = getDuo()
	priDuo(duoMulti(duo1,duo2))
	priDuo(duoAdd(duo1,duo2))
main()