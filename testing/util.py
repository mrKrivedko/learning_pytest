def str_to_num(str):
    """Вспомогательная функция:
    преобразует строку в число"""
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():
        return int(str)

def str_to_int_list(str_lst):
    """Тестируемая функция:
    преобразует список строк в список целых чисел"""
    num_list = []
    for item in str_lst:
        n = str_to_num(item)
        if n is not None:
            if isinstance(n, float):
                n = round(n)
            if 0 <= n <= 10:
                num_list.append(n)
    return num_list
