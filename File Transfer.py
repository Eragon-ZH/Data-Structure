'''
https://pintia.cn/problem-sets/951072707007700992/problems/980373213944213504
File Transfer
利用列表存储父结点，序号表示当前节点
负数表示为根，绝对值大小为树的节点数
确实按照大小union的但是测试4、5都超时
6当然也超时
'''

def Find(X):
	if S[X] < 0:
		return X
	else:
		return Find(S[X])

def Union(root1,root2):
	if S[root1] < S[root2]:
		S[root1] += S[root2]
		S[root2] = root1
	else:
		S[root2] += S[root1]
		S[root1] = root2

def Input_connection(u,v):
	root1 = Find(u-1)
	root2 = Find(v-1)
	if root1 != root2:
		Union(root1,root2)
	
def Check_connection(u,v):
	root1 = Find(u-1)
	root2 = Find(v-1)
	if root1 == root2:
		print("yes")
	else:
		print("no")
	
def Check_network():
	counter = 0
	for i in S:
		if i < 0:
			counter += 1
	if counter == 1:
		print("The network is connected.")
	else:
		print("There are {} components.".format(counter))

def main():
	N = int(input())
	global S
	S = [-1] * N
	while True:
		operation = input().split()
		if operation[0] == 'I':
			Input_connection(int(operation[1]),int(operation[2]))
		if operation[0] == 'C':
			Check_connection(int(operation[1]),int(operation[2]))
		if operation[0] == 'S':
			Check_network()
			break

main()

'''
正确的C++代码
#include <iostream>
#define ElementType int
using namespace std;

int *S;
int Find( ElementType X )
{
    if(S[X]==X)
        return X;
    return S[X]=Find(S[X]);
}

void Union( ElementType X1, ElementType X2)
{
    int Root1, Root2;
    Root1 = Find(X1);
    Root2 = Find(X2);
    if ( Root1 != Root2 )
    {
        if(S[Root1] < S[Root2])
        {
            S[Root2] = Root1;
        }
        else
        {
            S[Root1] = Root2;
        }
    }
}

int main()
{
    int num;
    cin >> num;
    char choose;
    int c1, c2;
    S = new int[num+1];
    for(int i=0; i<=num; i++)   // 初始化
        S[i] = i;
    while(1)
    {
        cin >> choose;
        if(choose == 'S')
            break;
        cin >> c1 >> c2;
        if(choose == 'I')
            Union(c1, c2);
        if(choose == 'C')
        {
            if(Find(c1) == Find(c2))
                cout << "yes" << endl;
            else
                cout << "no" << endl;
        }
    }
    int icount=0;
    for(int i=1; i<=num; i++)
        if(S[i] == i)   // 如果Parent就它自己，证明是根结点
            icount++;
    if(icount == 1)
        cout << "The network is connected." << endl;
    else
        cout << "There are " << icount << " components." << endl;
    return 0;
}
'''