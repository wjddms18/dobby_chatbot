import random
class Marble:
    oe_result = 0
    def __init__(self, dobby, player, expec):
        self.dobby = 10
        self.player = 10
        self.expec = expec

    def turn(dobby,player,expec):                                     
        while dobby == 0 or player == 0:                                #도비나 플레이어가 구슬을 다 쓰면 게임이 종료
            expec = int(input("홀짝을 예상해주세요(홀=1,짝=2) > "))      #예상값을 입력
    
    @classmethod
    def oddeven(cls, dobby):
        oe = [for i in range(11)] 
        result = random.choice(oe)                 
        if result % 2 != 0:                     
            cls.oe_result == 2
            return result,print(result + "이므로 짝수입니다!")
        else:
            cls.oe_result == 1
            return result,print(result + "이므로 홀수입니다!")

    def count(cls,dobby,player,expec,oe,result):
        if cls.oe_result == expec:                     #플레이어가 홀짝을 맞추면 도비의 구슬이 감소, 틀리면 플레이어의 구슬 감소
                dobby -= result
                print("주인님이 맞추셨어요!!")
                print("도비의 구슬을 가져가셔도 좋아요....")
        elif cls.oe_result != expec:
            player -= result
            print("아이쿠..주인님 틀리셨네요 ㅋ\n")
            print("주인님의 구슬은 이제 제 것입니다!")
        
            

    