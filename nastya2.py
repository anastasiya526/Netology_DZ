month=int(input("Введите месяц рождения в формате от 1 до 12):"))
day=int(input("Введите число рождения в формате от 1 до 31):"))
if (month==1 and day >= 20) or (month==2 and day <= 18):
  print('Ваш знак водолей')
elif (month==2 and day >= 19) or (month==3 and day <= 20):
  print('Ваш знак рыбы')
elif (month==3 and day >= 21) or (month==4 and day <= 19):
  print('Ваш знак овен')
elif (month==4 and day >=21) or (month==5 and day <= 20):
  print('Ваш знак телец')
elif (month==5 and day >= 21) or (month==6 and day <= 20):
  print('Ваш знак близнецы')
elif (month==6 and day >= 21) or (month==7 and day <= 22):
  print('Ваш знак рак')
elif (month==7 and day >=23) or (month==8 and day <= 22):
  print('Ваш знак лев')
elif (month==8 and day >= 23) or (month==9 and day <= 22):
  print('Ваш знак дева')
elif (month==9 and day >= 23) or (month==10 and day <= 22):
  print('Ваш знак весы')
elif (month==10 and day >=23) or (month==11 and day <= 21):
  print('Ваш знак скорпион')
elif (month==11 and day >=22) or (month==12 and day <= 21):
  print('Ваш знак стрелец')
#elif (month==12 and day >=22) or (month==1 and day <= 19):
#   print('Ваш знак козерог')
else:
  print('Ваш знак козерог')