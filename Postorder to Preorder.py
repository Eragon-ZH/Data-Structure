'''
https://pintia.cn/problem-sets/998409637106466816/problems/998409961867231274
PTA 数据结构2018春期末考试编程题，根据后序和中序遍历输出先序遍历
也可以不建树
'''

# 定义树类型
class Tree:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
# 获得输入
def getList():
    K = eval(input())
    postList = list(map(int,input().split()))
    inList = list(map(int,input().split()))
    return postList,inList
# 构建树
def makeTree(postorder,inorder):
    if len(postorder) == 0:
        return None
    # 后序遍历最后一个节点即为根节点
    # 用根节点将中序遍历分为左子树和右子树，再递归调用
    rootdata = postorder[-1]
    index = inorder.index(rootdata)
    left = makeTree(postorder[:index],inorder[:index])
    right = makeTree(postorder[index:-1],inorder[index+1:])
    return Tree(rootdata,left,right)
# 先序遍历
def Preorder(tree,root):
    if tree == None:
        return
    else:
        print("",tree.data,end = '')
        Preorder(tree.left,root)
        Preorder(tree.right,root)

def main():
    postorder,inorder = getList()
    tree = makeTree(postorder,inorder)
    print("Preorder:",end='')
    Preorder(tree,tree.data)

if __name__ == '__main__'
