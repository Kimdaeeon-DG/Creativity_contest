def solution(a, b):
	dy = [-1, 0, 1, 0] 
	dx = [0, 1, 0, -1]
	arr = [[0 for _ in range(10)] for _ in range(10)]
	x, y, d, i = 0, 0, 0, 0
	while (i < 1000): # 임의의 값 1000번 반복
		if (x, y) == (a, b):
			d = (d - 1) % 4
		elif arr[y][x] == 0:
			d = (d + 1) % 4
			arr[y][x] += 1
		elif arr[y][x] == 1:
			d = (d - 1) % 4
			arr[y][x] += 1
		x, y = (x + dx[d]) % 10, (y + dy[d]) % 10
		i += 1
	
	count = sum(row.count(2) for row in arr) # 2의 갯수를 세어 줌
	return count

def main():
	for i in range(10):
		for j in range(10):
			if solution(i, j) == 99: # 만약 2의 갯수가 99개면(모두 됐으면)
				print(f"x: {i}\ny:{j}\n") # 이 좌표일 때 모두 됨
main()
