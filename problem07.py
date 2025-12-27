import sys
input = sys.stdin.readline

# 정수 N이 주어진다.
# N의 구구단을 9부터 1까지 역순으로 출력하라.

def main():
    n = int(input())

    for i in range(9, 0, -1):

        print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    main()