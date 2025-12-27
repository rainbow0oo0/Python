import sys
input = sys.stdin.readline

# 정수 N이 주어진다.
# 1부터 N까지의 수 중에서 짝수인 수들의 합을 구하라.

def main():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        # 짝수 조건
        if i % 2 == 0:
            total += i

    print(total)

if __name__ == "__main__":
    main()