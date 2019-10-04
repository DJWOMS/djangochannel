letters = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'JO',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'J',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SCH',
    'Ъ': '',
    'Ы': 'Y',
    'Ь': '',
    'Э': 'E',
    'Ю': 'JU',
    'Я': 'JA',
    ' ': '_'
}


def transliteration_rus_eng(text):
    """
    Транслитерация русского в английский,
    символы, которых нет выше, остаются прежними
    """
    l = [":", "'", "(", ")", "`", ",", ".", ";", '"', "+", "="]
    for i in l:
        text = text.replace(i, "")
    formatted_text = '{}'.format(text).upper()
    return ''\
        .join(letters.get(x, x) for x in formatted_text).lower()


def transliteration_rus_eng_image(text):
    """
    Транслитерация русского в английский,
    символы, которых нет выше, остаются прежними
    """
    formatted_text = '{}'.format(text).upper()
    return ''.join(letters.get(x, x) for x in formatted_text).lower()
