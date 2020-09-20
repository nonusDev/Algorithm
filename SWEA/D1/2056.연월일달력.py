import sys

sys.stdin = open("2056.연월일달력.txt", 'r')

for tc in range(1, int(input())+1):
    num = input()

    res = ""
    if num[5] == '0':
        res = -1
    elif num[5] == '2' and num[6] == '3' or num[7] == '9':
        res = -1
    else:
        res = f"{num[:4]}/{num[4:6]}/{num[6:]}"
    
    print(f"#{tc} {res}")