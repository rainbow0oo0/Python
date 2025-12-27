import sys
input = sys.stdin.readline

# 정수 N이 주어진다.
# 1부터 N까지의 수 중에서 3의 배수 또는 5의 배수인 수들의 합을 구하라.

def main():
    # 프로그램의 핵심 로직을 모아둔 함수
    # 파이썬은 함수 없어도 됨

    n = int(input())
    total = 0
    
    for i in range(1, n + 1):
        # 3 또는 5의 배수 조건
        if i % 3 == 0 or i % 5 == 0:
            total += i

    print(total)

if __name__ == "__main__":
    main()