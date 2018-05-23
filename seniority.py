'''
https://pintia.cn/problem-sets/951072707007700992/problems/993315598882746368
'''

def main():
	N = int(input())
	sen = [0] * 51
	inp = list(map(int,input().split()))
	while len(inp)!= 0:
		tep = inp.pop()
		sen[tep] += 1
		
	for i in range(len(sen)):
		if sen[i] != 0:
			print('{}:{}'.format(i,sen[i]))
	
if __name__ == '__main__':
	main()