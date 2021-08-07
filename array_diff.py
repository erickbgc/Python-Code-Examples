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
    array_diff([-12, -11], [13, 9, 11, -19]) # should equal [-12, -11]
    array_diff([-15, 14, 15], [-16]) # should equal [-15, 14, 15]
    array_diff([6, 1], [4]) # should equal [6, 1]
    array_diff([13, -5, -5, -7, -18, 18], [-2, -14, 15, -7, 3, 1, 0, 10, 14, 1]) # should equal [13, -5, -5, -18, 18]
    array_diff([], [-3, 11, -1, -16, -4, -3, 9]) # should equal []
    array_diff([6, 15, -18, -17, -16, 14, -15], [-16, 12, -15, -17, -11, -17, -17, -20, 10, 10, 0, -14]) # should equal [6, 15, -18, 14]

if __name__ == '__main__':
    main()
