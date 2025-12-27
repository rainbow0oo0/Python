import sys
input = sys.stdin.readline

# 정수 N이 주어진다.
# N의 구구단(1~9) 중에서 결과가 3의 배수인 것만 출력하라.

def main():
    n = int(input())

    for i in range(1, 10):
        if (n * i) % 3 == 0:

            print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    main()