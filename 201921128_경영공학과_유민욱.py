print('메뉴 선정을 도와 드리겠습니다, 주사위를 굴려주세요!!')
print()

dice=['1','2','3','4','5','6']
print('주사위를 굴려서 나오는 경우')
print(dice)
print()
item=input('주사위 나온 숫자에 알맞게 음식을 고르시오')
item=input('숫자에 따른 음식은 다음과 같다')
print()

foods={'1':'피자','2':'치킨','3':'족발','4':'회','5':'햄버거','6':'스테이크'}
print(foods)

choosefood=input(str(list(foods.keys()))+'중 어떤 숫자를 뽑았습니까??')
print('<%s>에 해당하는 음식은  <%s>입니다.'%(choosefood,foods[choosefood]))
print()

item=input('음식과 같이 먹을 음료를 고르시오')
item=input('음식에 따른 음료는 다음과 같다.')

drinks={'피자':'콜라','치킨':'맥주','족발':'막걸리','회':'소주','햄버거':'사이다','스테이크':'와인'}
print(drinks)
print()

choosedrink=input(str(list(drinks.keys()))+'중 어떤 음식을 뽑았는가?')
print('<%s>에 해당하는 음료는 <%s>입니다.'%(choosedrink,drinks[choosedrink]))
print()


print('메뉴 선정에 도움이 되었으면 좋겠습니다!!')
