#List Leaves
#https://pintia.cn/problem-sets/951072707007700992/problems/975887373624213504
#利用数组来模拟树
def getTree():
	K = eval(input())
	pos = [i for i in range(K)]
	tree = []
	for i in range(K):
		lt = input().split()
		for i in range(2):
			if lt[i] != '-':
				lt[i] = eval(lt[i])
				pos.remove(lt[i])
		tree.append(lt)
	root = pos[0]
	return tree,root
#利用栈按顺序得到叶子
def getLeaves(tree,root):
	result = []
	seq = []
	seq.append(root)
	while len(seq) > 0:
		node = seq.pop(0)
		if tree[node][0] == '-' and tree[node][1] == '-':
			result.append(node)
		if tree[node][0] != '-':
			seq.append(tree[node][0])
		if tree[node][1] != '-':
			seq.append(tree[node][1])
	return result
#格式化输出
def priLeaves(leaves):
	for i in range(len(leaves)-1):
		print(leaves[i],end = ' ')
	print(leaves[-1],end = '')

def main():
	tree,root = getTree()
	leaves = getLeaves(tree,root)
	priLeaves(leaves)
	
main()