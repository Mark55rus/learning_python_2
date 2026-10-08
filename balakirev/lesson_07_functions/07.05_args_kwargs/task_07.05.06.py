# Подвиг 4. Объявите в программе функцию с именем get_data_fig для вычисления 
# периметра произвольного N-угольника. На вход этой функции передаются N 
# длин сторон через ее аргументы. Дополнительно могут быть указаны именованные аргументы:
# tp - булево значение True/False;
# color - целое числовое значение;
# closed - булево значение True/False;
# width - вещественное значение.
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения 
# именованных параметров в порядке их перечисления в тексте задания (если они были переданы). 
# Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).
# P.S. Функцию выполнять не нужно, только объявить.

def get_data_fig(*args, tp=None, color=None, closed=None, width=None):
    result = [sum(args)]
  
    if tp is not None:
        result.append(tp)
    if color is not None:
        result.append(color)
    if closed is not None:
        result.append(closed)
    if width is not None:
        result.append(width)

    return tuple(result)
