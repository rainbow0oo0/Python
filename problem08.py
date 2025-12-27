import sys
input = sys.stdin.readline

# N의 구구단(1~9) 중에서 결과가 20을 초과하는 줄을 출력하고,
# 마지막에 총 몇 줄이 출력됐는지 출력하라.

def main():
    n = int(input())
    count = 0

    for i in range(1, 10):
        if (n * i) > 20:
            count += 1
            print(f"{n} * {i} = {n * i}")

    print(f"count = {count}" )

if __name__ == "__main__":
    main()