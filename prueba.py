# I.B.1 RLE Naive / Ingenuo
def rle_encode_naive(lst):

    if not lst:
        return []
    
    lst_final = []
    count = 1
    aux = lst[0]

    for i in range(1, len(lst)):
        elem = lst[i]
        if elem == aux:
            count += 1

        else:
            lst_final = lst_final + [(aux, count)]
            count = 1
            aux = elem

    lst_final = lst_final + [(aux, count)]

    return lst_final
        
# I.B.2 RLE Optimized / Óptimo
def rle_encode_optimized(lst):
    """Codificación RLE optimizada usando append in-place."""

    if not lst:
        return []

    lst_final = []
    aux = lst[0]
    count = 1

    for i in range(1, len(lst)):
        elem = lst[i]
        if elem == aux:
            count += 1

        else:
            lst_final.append((aux, count))
            aux = elem
            count = 1

    lst_final.append((aux, count))

    return lst_final

lst = ["A", "A", "B", "A", "a", "A", "A"]
lst_final = rle_encode_naive(lst)
lst_final2 = rle_encode_optimized(lst)

print(lst_final)
print(lst_final2)

