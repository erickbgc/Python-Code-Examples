# a = [1, 2, 2, 3]

# b = [2,2,4,3,2,6]

def array_diff(a, b):
    copy_a = a.copy()
    copy_b = b.copy()

    itemsToRemove = []

    if (len(a) == 0 and len(b) == 0) or (len(a) == 0 or len(b) == 0):
        result = a + b
        return print(result)
    elif len(a) > 0 and len(b) > 0:
        for itemInA in a:  # 1
            # print("Valores de A: ", itemInA)
            if b.count(itemInA) > 0:
                # print("Numero encontrado en B!!", itemInA)
                for itemInB in b:
                    if itemInB == itemInA:
                        if copy_b.count(itemInA) > 0:
                            position_b = copy_b.index(itemInB)
                            copy_b.pop(position_b)

                            if itemInB not in itemsToRemove:
                                itemsToRemove.append(itemInB)
                            # if copy_a.count(itemInA) > 0:
                            #     position_a = copy_a.index(itemInA)
                            #     copy_a.pop(position_a)
                            # else:
                            #     pass
                            # print("Copia A: ", copy_a)
                            # print("Copia B: ", copy_b)
                        else:
                            continue
                    else:
                        pass
                        # print("No ha pasado nada!: ", itemInB)

        for item in a:
            if item in itemsToRemove:
                position = copy_a.index(item)
                copy_a.pop(position)
        result = copy_a + copy_b
        return print(result)
    else:
        pass


def main():
    array_diff([1, -3, -3], [9, -2, -4, 7, -20, 10, 9, -11,
               20, -1, 15, 5, 5, -17, 9, -6, 14, 6, -17, -11])


if __name__ == '__main__':
    main()
