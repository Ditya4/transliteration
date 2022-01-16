text = '''SWITCH_ID    SWITCH_NAME    RS_ID    RS_NAME
3200    Львів МЗТС-3    3200    МЗТС АМА автоматика
3200    Львів МЗТС-3    3250    МЗТС АМА послуги
3200    Львів МЗТС-3    3252    МЗТС АМА заголовки блоків
3200    Львів МЗТС-3    3259    МЗТС-3 IAD
3200    Львів МЗТС-3    3260    МЗТС-3 IAD заголовки блоків
3203    Львів АМТС    3203    ОПТС-2/АМТС АМА автоматика
3203    Львів АМТС    3253    ОПТС-2/АМТС АМА заголовки блоків
3203    Львів АМТС    3255    ОПТС-2/АМТС АМА послуги
3203    Львів АМТС    3261    ОПТС-2/АМТС IAD
3203    Львів АМТС    3262    ОПТС-2/АМТС IAD заголовки блоків
3205    Львів ОПТС-1    3207    ОПТС-1 автоматика
3205    Львів ОПТС-1    3256    ОПТС-1 заголовки блоків
3205    Львів ОПТС-1    3258    ОПТС-1 послуги
3210    СПВ-Самбір    3210    СПВ-Самбір
3211    СПВ-Мостиська    3211    СПВ-Мостиська
3212    СПВ-Стрий    3212    СПВ-Стрий
3213    СПВ-Червоноград    3213    СПВ-Червоноград
3214    АТС-Соснівка    3214    АТС-Соснівка
3215    СПВ-Миколаїв    3215    СПВ-Миколаїв
3216    СПВ-Яворів    3216    СПВ-Яворів
3217    ЦС-Дрогобич    3217    АТС-Дрогобич автоматика
3217    ЦС-Дрогобич    3218    АТС-Дрогобич службові
3218    ЦС-Трускавець    3219    ЦС-Трускавець автоматика
3220    АТС-577 Сокаль    3221    АТС-Сокаль автоматика
3220    АТС-577 Сокаль    3222    АТС-Сокаль службові
3221    СПВ-Золочів    3223    СПВ-Золочів
3222    СПВ-Жидачів    3224    СПВ-Жидачів
3223    СПВ-Пустомити    3226    СПВ-Пустомити
3224    СПВ-Новий Розділ    3227    СПВ-Новий Розділ
3225    СПВ Сокаль    3228    СПВ-Сокаль
3229    АТС-221/222/223 ЦТП м.Львів    3233    АТС-221/222/223 ЦТП Львів
3230    АТС-230/231 ЦТП м.Львів    3234    АТС 230/231 ЦТП DWO
3230    АТС-230/231 ЦТП м.Львів    3235    АТС 230/231 ЦТП MGR
3230    АТС-230/231 ЦТП м.Львів    3236    АТС 230/231 ЦТП STO
3232    АТС-292 ЦТП м.Львів    3264    АТС-292 ЦТП
32382    АТС Старий Самбір    32382    АТС Старий Самбір
32526    АТС Жовква    32526    АТС-Жовква
32542    АТС-Кам'янка-Бузька    32542    АТС-Кам'янка-Бузька
32606    АТС Моршин    32606    АТС-Моршин
32632    АТС Перемишляни    32632    АТС-Перемишляни
32693    АТС Турка    32693    АТС Турка
46269    АТС-67 ЦТП м.Львів    46272    АТС-67 ТEX
46318    ВАМ-39 м. Червоноград    46321    ВАМ-39 м. Червоноград
46322    АТС-96 ЦТП м.Львів    46324    АТС-96 ЦТП
61281    СПВ-Броди    61285    СПВ-Броди
61282    СПВ-Сколе    61286    СПВ-Сколе
'''
lines = text.split("\n")
# ===============================================================================
# print(text)
# print(lines)
# print(len(lines), '\n\n\n\n')
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
    