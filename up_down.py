import random

num = random.randint(1,100)

chance = 5 # 기회는 총 5번!

ask = int(input("안녕 나는 구렁이야. 너랑 숫자게임을 하고시포! "))

chance -= 1 # 처음 물어본 기회 뺴주기!


while chance >= 1 :
    


        if ask == num:
            if ask == num:
                print("우와 맞췄어요! 대단해요",end="") # end="" 하면 줄바꿈이 없어진다
                break

        else:
                print("")
                print("다시 해보세요")
                print("") 
        if ask < num:
                print("참고로", ask , "보다 커요!")
                print("")
                ask = int(input("무엇인가요? "))
                if ask == num:
                    continue
                chance -= 1        
        
        else:
            print("참고로 숫자는", ask , "보다 작아요!")
            print("")
            ask = int(input("무엇인가요? "))
            if ask == num:
                continue # while 문 처음으로
            chance -= 1
        
        
        if chance == 1:
            print("기회는 단 한 번 뿐이니 신중해지세요!")


print("")
print("정답은", num , "이였습니다~")



    








# elif chance == 1:  # elif는 if와 else 사이에!
#             print("숫자는", ask, "보다 작!")
#             print("기회는 단 한 번 뿐이니 신중해지세요!")
