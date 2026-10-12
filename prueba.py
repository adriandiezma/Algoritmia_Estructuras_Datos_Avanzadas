def rle_encode_naive(lst):

    if lst == []:
        return []
    
    lst_final = []
    count = 0
    aux = lst[0]

    for elem in lst:
        if elem != aux:
            lst_final = lst_final + [(aux, count)]
            count = 1
            aux = elem
        else:
            count += 1

    lst_final = lst_final + [(aux, count)]

    return lst_final
lst = ["A", ]
lst_final = rle_encode_naive(lst)

print(lst_final)
# Resultado correcto: [('A', 2), ('B', 1), ('A', 1)]
