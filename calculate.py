s = []
num = input('введите операцию а затем числа')
for x in num:
  s.append(x)
# try:
assert s[0] in ['+','-','*','/'], 'Ñ‚Ð°ÐºÐ¾Ð¹ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¸ Ð½ÐµÑ‚'
try:
 a = int(s[1])
 b = int(s[2])
 if s[0] == '+':
    suma = a + b
 elif s[0] == '-':
    suma = a - b
 elif s[0] == '*':
    suma = a * b
 if s[0] == '/':
    suma = a / b
except ZeroDivisionError:
     print('делить на ноль нельзя')
     suma = 0
except ValueError:
      print('ввели начение не int')
      suma = 0
except IndexError:
      print('введены не все аргументы')
      suma = 0
print(suma)