'''
https://pintia.cn/problem-sets/951072707007700992/problems/977489256881188864
完全二叉树不用担心空间浪费，可以直接用列表
'''

import math

def getLen(N):
	#给定完全二叉树的长度，获取左子树的长度
	H = math.floor(math.log(N+1,2))
	X = N +1 - 2**H
	X = min( X, 2**(H-1) )
	L = 2**(H-1) -1 + X
	return L

def solve(Tleft,Tright,Troot):
	n = Tright - Tleft + 1
	if n == 0:
		return
	L = getLen(n)
	#将初始列表的值填到结果列表
	endList[Troot] = startList[Tleft+L]
	leftRoot = Troot * 2 + 1
	rightRoot = leftRoot + 1
	solve(Tleft, Tleft+L-1, leftRoot)
	solve(Tleft+L+1, Tright, rightRoot)

	
def main():
	global startList,endList
	N = int(input())
	startList = list(map(int,input().split()))
	#排好序的初始列表
	startList.sort()
	#按照二叉树位置生成的列表
	endList = [-1] * N
	Troot = getLen(N)
	solve(0,N-1,0)
	for i in range(len(endList)-1):
		print(endList[i],end = ' ')
	print(endList[-1])
	
main()