kakao = 1000
kium = 500

for i in range(0, 3):
    kakao = kakao + 500
    kium = kium + 1000

if kakao < kium:
    print("키움이 더 높다")
elif kakao > kium:
    print("카카오가 더 높다")
else:
    print("가격은 같다")

for i in range(0, 9):
    for j in range(0, 9):
        print("%d x %d = %d" % (i+1, j+1, (i+1)*(j+1)))
