'''
https://pintia.cn/problem-sets/951072707007700992/problems/990061301390385152
'''

def mergeSort(li):
    if len(li) == 1:   #分到只有一个元素为止
        return li
    mid = len(li)//2    #将列表分为左右两个部分
    left = li[:mid]
    right = li[mid:]

    left1 = mergeSort(left) #接着将左右两部分分别再分为左右两部分
    right1 = mergeSort(right)

    return merge(left1,right1) #进行合并

def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:   #将两个列表按照从小到大进行合并
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left  #任一列表为空列表后跳出循环，将result后直接连上剩余的列表
    result += right
    return result
	
def main():
	N = int(input())
	Q = input().split()
	Q = list(map(int,Q))
	Q = mergeSort(Q)
	for i in range(len(Q)-1):
		print(Q[i],end=' ')
	print(Q[-1])
	
if __name__ == '__main__':
	main()