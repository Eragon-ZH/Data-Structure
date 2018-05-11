'''
https://pintia.cn/problem-sets/951072707007700992/problems/980373149213519872
堆中的路径
'''

def InserHeap(X,size):
	i = size + 1
	Heap[size+1] = X
	while Heap[i//2] > X:
		Heap[i] = Heap[i//2]
		i = i // 2
	Heap[i] = X

def printHeap(j):
	while j > 1:
		print(Heap[j],end = ' ')
		j = j // 2
	print(Heap[1])
	
def main():
	NMList = input().split()
	N = int(NMList[0])
	M = int(NMList[1])
	numList = input().split()
	reseltList = input().split()
	#用数组实现堆
	global Heap
	Heap = [-1] * (N+1)
	Heap[0] = -10001
	size = 0
	for i in numList:
		InserHeap(int(i),size)
		size += 1
	for j in range(M):
		printHeap(int(reseltList[j]))
			
main()