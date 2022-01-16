text = '''Назва потоку записів;0;Дата;1;2;3;4;5;6;7;8;9;10;11;12;13;Switch Id;14;15;16;17;18;19;20;21;22;23;RS Id
АМТС АМА автоматика;3;11.01.2022, Вт.;3;3;3;2;2;2;3;3;4;4;4;3;4;3104;4;4;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;10.01.2022, Пн.;3;2;2;2;2;3;3;3;4;4;4;3;4;3104;4;4;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;09.01.2022, Нд.;3;3;3;3;2;2;3;3;3;3;3;3;3;3104;3;3;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;08.01.2022, Сб.;2;2;2;3;2;2;3;3;3;3;3;3;3;3104;3;3;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;07.01.2022, Пт.;3;2;3;3;3;2;3;3;3;3;3;3;3;3104;3;3;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;2;06.01.2022, Чт.;3;3;3;2;2;2;3;3;3;3;4;3;3;3104;3;3;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;05.01.2022, Ср.;3;2;2;3;2;2;3;3;4;4;4;4;4;3104;4;4;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;04.01.2022, Вт.;2;2;2;2;3;3;3;3;4;4;4;4;4;3104;4;4;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;03.01.2022, Пн.;3;2;2;2;3;3;3;3;3;3;3;3;3;3104;3;3;3;3;3;3;3;3;3;3;3104
АМТС АМА автоматика;3;02.01.2022, Нд.;3;3;2;2;2;2;2;3;3;3;3;3;3;3104;3;3;3;3;3;3;3;3;3;3;3104'''
lines = text.split("\n")
# ===============================================================================
# print(text)
# print(lines)
# print(len(lines))
# ===============================================================================

for index in range(len(lines)):
    temp_str = ''
    for index_2 in range(len(lines[index])):
        if lines[index][index_2] in ('А', 'а'):
            temp_str += 'a'
        elif lines[index][index_2] in ('Б', 'б'):
            temp_str += 'b'
        elif lines[index][index_2] in ('В', 'в'):
            temp_str += 'v'
        elif lines[index][index_2] in ('Г', 'г'):
            temp_str += 'g'
        elif lines[index][index_2] in ('Д', 'д'):
            temp_str += 'd'
        elif lines[index][index_2] in ('Е', 'е', 'е'):
            temp_str += 'e'
        elif lines[index][index_2] in ('Є', 'є'):
            temp_str += 'je'
        elif lines[index][index_2] in ('Ж', 'ж'):
            temp_str += 'g'
        elif lines[index][index_2] in ('З', 'з'):
            temp_str += 'z'
        elif lines[index][index_2] in ('И', 'и'):
            temp_str += 'u'
        elif lines[index][index_2] in ('І', 'і'):
            temp_str += 'i'
        elif lines[index][index_2] in ('Ї', 'ї'):
            temp_str += 'ji'
        elif lines[index][index_2] in ('Й', 'й'):
            temp_str += 'j'
        elif lines[index][index_2] in ('К', 'к'):
            temp_str += 'k'
        elif lines[index][index_2] in ('Л', 'л'):
            temp_str += 'l'
        elif lines[index][index_2] in ('М', 'м'):
            temp_str += 'm'
        elif lines[index][index_2] in ('Н', 'н'):
            temp_str += 'n'
        elif lines[index][index_2] in ('О', 'о'):
            temp_str += 'o'
        elif lines[index][index_2] in ('П', 'п'):
            temp_str += 'p'
        elif lines[index][index_2] in ('Р', 'р'):
            temp_str += 'r'
        elif lines[index][index_2] in ('С', 'с'):
            temp_str += 's'
        elif lines[index][index_2] in ('Т', 'т'):
            temp_str += 't'
        elif lines[index][index_2] in ('У', 'у'):
            temp_str += 'y'
        elif lines[index][index_2] in ('Ф', 'ф'):
            temp_str += 'f'
        elif lines[index][index_2] in ('Х', 'х'):
            temp_str += 'h'
        elif lines[index][index_2] in ('Ц', 'ц'):
            temp_str += 'c'
        elif lines[index][index_2] in ('Ч', 'ч'):
            temp_str += 'ch'
        elif lines[index][index_2] in ('Ш', 'ш'):
            temp_str += 'sh'
        elif lines[index][index_2] in ('Щ', 'щ'):
            temp_str += 'sh4'
        elif lines[index][index_2] in ('Ь', 'ь'):
            temp_str += '\''
        elif lines[index][index_2] in ('Ю', 'ю'):
            temp_str += 'ju'
        elif lines[index][index_2] in ('Я', 'я'):
            temp_str += 'ja'
        else:
            temp_str += lines[index][index_2]
    # print(temp_str)
    lines[index] = temp_str
    # print(lines[index])

for index in range(len(lines)):
    print(lines[index])
    