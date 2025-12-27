import sys
input = sys.stdin.readline

# 구구단
# 정수 N이 주어진다.
# N의 1부터 9까지 곱한 결과를 아래 형식으로 출력하라.

def main():
    n = int(input())
    total = 0

    for i in range(1, 10):
        print(f"{n} * {i} = {n * i}")
        

if __name__ == "__main__":
    main()

"""
입력 값 : 3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
"""