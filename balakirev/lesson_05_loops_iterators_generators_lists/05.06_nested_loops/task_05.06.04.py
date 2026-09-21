# Подвиг 2. На вход программе подаются строки (URL-адреса, каждая с новой строки). 
# В программе уже реализовано их чтение и сохранение в списке:
# lst_in = list(map(str.strip, sys.stdin.readlines())) 
# Требуется заменить в строках списка lst_in все пробелы на символ дефиса (-). 
# Следует учесть, что может быть несколько подряд идущих пробелов. 
# Полученные URL-адреса (строки) вывести на экран в столбик в порядке их следования в списке lst_in.

# lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii '] - для теста

import sys

lst_in = list(map(str.strip, sys.stdin.readlines())) 

for i, row in enumerate(lst_in):
    row = row.replace(' ', '-')
    while '--' in row:
        row = row.replace('--', '-')

    lst_in[i] = row

for row in lst_in:
    print(row)
