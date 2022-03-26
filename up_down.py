import random

# num = random.randint(1,100)

num = 10

chance = 5

ask = int(input("안녕 나는 구렁이야. 너랑 숫자게임을 하고시포! "))

chance -= 1



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
                chance -= 1        
        
        else:
            print("참고로 숫자는", ask , "보다 작아요!")
            print("")
            ask = int(input("무엇인가요? "))
            chance -= 1
        
        if chance == 0:
            print("기회는 끝~")
            break
        
        if chance == 1:
            print("기회는 단 한 번 뿐이니 신중해지세요!"))

    








# elif chance == 1:  # elif는 if와 else 사이에!
#             print("숫자는", ask, "보다 작!")
#             print("기회는 단 한 번 뿐이니 신중해지세요!")
