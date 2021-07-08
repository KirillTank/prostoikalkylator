what=input('выберите команду: (+,-,•,:)')
a=float( input('введите число: '))
b=float( input('введите число: '))
if what =='+':
    c=a+b
    print('результат' + str(c))
elif what =='-':
    c=a-b
    print('результат' + str(c))
elif what =='•':
    c=a*b
    print('результат' + str(c))
elif what ==':':
    c=a/b
    print('результат' + str(c))
else:
    print('неверная команда')
