import random

while True:
    a = random.randint(1,9)
    b = random.randint(1,9)
    print(str(a)+"*"+str(b)+"=")
    정답 = a*b
    내가_제출한_정답 = int(input())
    if 정답 == 내가_제출한_정답:
        print("정답입니다")
    else:
        print("오답입니다")