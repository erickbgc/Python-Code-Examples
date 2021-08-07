# a = [1, 2, 2, 3]

# b = [2,2,4,3,2,6]

def main():
    b = [1, 2, 2, 3]
    a = [2, 2, 4, 3, 2, 6]

    copy_a = a.copy()
    copy_b = b.copy()

    if (len(a) == 0 and len(b) == 0) or (len(a) == 0 or len(b) == 0):
        result = a + b
        return print(result)
    elif len(a) > 0 and len(b) > 0:
        for itemInA in a:  # 1
            print("Valores de A: ", itemInA)
            if b.count(itemInA) > 0:
                print("Numero encontrado en B!!", itemInA)
                for itemInB in b:
                    if itemInB == itemInA:
                        if copy_b.count(itemInA) > 0:
                            position_b = copy_b.index(itemInB)
                            copy_b.pop(position_b)

                            if copy_a.count(itemInA) > 0:
                                position_a = copy_a.index(itemInA)
                                copy_a.pop(position_a)
                            else:
                                pass
                            print("Copia A: ", copy_a)
                            print("Copia B: ", copy_b)
                        else:
                            continue
                    else:
                        print("No ha pasado nada!: ", itemInB)
        result = copy_a + copy_b
        return print(result)
    else:
        pass


if __name__ == '__main__':
    main()
