from main import Routine

class Calorie:
    Korean_food = ('떡볶이', '튀김', '순대', '김밥', '어묵','X')
    Korean_food_calorie = (500, 600, 700, 400, 300)

    Western_food = ('피자', '스파게티', '햄버거', '치킨', '샐러드','X')
    Western_food_calorie = (1000, 800, 700, 600, 300)

    Chinese_food = ('짜장면', '짬뽕', '탕수육', '볶음밥', '군만두','X')
    Chinese_food_calorie = (700, 800, 1000, 600, 500)

    Japanese_food = ('초밥', '라멘', '우동', '돈까스', '오므라이스','X')
    Japanese_food_calorie = (500, 700, 600, 800, 900)

    calorie_add = 0

    def __init__(self, name):
        super(Calorie, self).__init__(name)
        self.k = 5
        self.w = 5
        self.c = 5
        self.j = 5

    def __str__(self):
        return f'{self.name}님이 섭취하신 음식은 \n' \
               f'한식 : {Calorie.Korean_food[self.k]} \n' \
                  f'양식 : {Calorie.Western_food[self.w]} \n' \
                    f'중식 : {Calorie.Chinese_food[self.c]} \n' \
                        f'일식 : {Calorie.Japanese_food[self.j]} \n' \
                            f'이므로, \n' \
               f'{self.name}님의 총 섭취 칼로리는 {Calorie.calorie_add}kcal 입니다.'



    def Korean(self):
        for index, Food in enumerate(Calorie.Korean_food[0:5]) :
            print(f'{index + 1}. {Food}')
        k = input("오늘 먹은 음식을 선택하세요 : ")
        if k == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Korean_food_calorie[int(k) - 1]
            self.k = int(k) - 1

    def Western(self):
        for index, Food in enumerate(Calorie.Western_food[0:5]):
            print(f'{index + 1}. {Food}')
        w = input("오늘 먹은 음식을 선택하세요 : ")

        if w == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Western_food_calorie[int(w) - 1]
            self.w = int(w) - 1

    def Chinese(self):
        for index, Food in enumerate(Calorie.Chinese_food[0:5]):
            print(f'{index + 1}. {Food}')
        c = input("오늘 먹은 음식을 선택하세요 : ")

        if c == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Chinese_food_calorie[int(c) - 1]
            self.c = int(c) - 1

    def Japanese(self):
        for index, Food in enumerate(Calorie.Japanese_food[0:5]):
            print(f'{index + 1}. {Food}')
        j = input("오늘 먹은 음식을 선택하세요 : ")
        if j == '':
            Calorie.calorie_add += 0
        else:
            Calorie.calorie_add += Calorie.Japanese_food_calorie[int(j) - 1]
            self.j = int(j) - 1

    def Meals(self):
        self.Korean()
        self.Western()
        self.Chinese()
        self.Japanese()


if __name__ == '__main__':
    # name = input("이름을 입력하세요 : ")
    caloric_calculator = Calorie()
    caloric_calculator.Meals()
    print(caloric_calculator)
