import sys
input = sys.stdin.readline

# 구구단에서 짝수 결과만 출력

def main():
    n = int(input())

    for i in range(1, 10):
#       if i % 2 == 0:
        if (n * i) % 2 == 0:

            print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    main()

"""
입력 : 3
3 * 2 = 6
3 * 4 = 12
3 * 6 = 18
3 * 8 = 24
"""