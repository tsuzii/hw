# int - целое число - неизменяемый
print(-92)
print(92574357948327594325984375983427598437598423759873429587)
print(0)

# str - строка - неизменяемый
print("Hello '12'")  # последовательность символов
print('Hello "Tom"')
print("Hello \"12\"")
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")  # Hello\World
print("o")

print("""Hello 
'12'""")

# Доступ к элементу в последовательности
print('Hello'[0])  # H
print('Hello'[3])  # l

# 'Hello'[0] = 'A'  - 'str' object does not support item assignment

# int()  # преобразовать в int
# str()  # преобразовать в str
# type()  # показать тип данных

print(int('12'), type(int('12')))
print(str(89543), type(str(89543)))

print(int('   54   ') + 3)
print(int('-2'))
# print(int(''))  # ValueError: invalid literal for int() with base 10: ''

