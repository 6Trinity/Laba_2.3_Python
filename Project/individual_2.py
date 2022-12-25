text = str(input("Введите текст: "))
text_i = text.partition('.')[0] + '.'
number = text_i.count('и')
print("В первом предложении {0} букв и".format(number))