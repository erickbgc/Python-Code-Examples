def Knapsack(maxCap, sortedList):
    result = [] # The items that will be carried by the Knapsack
    peso_actual = maxCap # The Actual Weight value will be reduced regarding the items weights that are inserted in the knapsack
    max_beneficio = 0 # Volume for the benefit values that are in the knapsack
    for sublist in sortedList:
        if sublist[0] <= peso_actual:
            result.append(sublist)
            peso_actual -= sublist[0]
            max_beneficio += sublist[1]
        else:
            continue
    return result, max_beneficio

def customMax(myFlatlist) -> []:
    """
    Function that return a list of indexes from a list sorted from their maximum to minimum values.
    """
    sortedIndexes = []
    for i_range in range(len(myFlatlist)):
        maxNumber = -1
        maxIndex = 0
        for i, item in enumerate(myFlatlist):
            if i in sortedIndexes:
                continue
            else:
                if item > maxNumber:
                    maxNumber = item
                    maxIndex = i
        sortedIndexes.append(maxIndex)
    return sortedIndexes

def main():

    # knapsackItems = [ [18, 30], [5, 50], [20, 10], [60, 25], [30, 70] ]
    knapsackItems = [ [95, 55], [4, 10], [60, 47], [32, 5], [23, 4], [72, 50], [80, 8], [62, 61], [65, 85], [46, 87] ]
    # knapsackItems = [ [55, 95], [10, 4], [47, 60], [5, 32], [4, 23], [50, 72], [8, 80], [61, 62], [85, 65], [87, 46] ]

    flat_list = [ sublist[1] for sublist in knapsackItems ] # Flat List and append just the Benefit into a new list

    indexesOrd = customMax(flat_list)

    itemsOrd = [ sublist for index in indexesOrd for i, sublist in enumerate(knapsackItems) if index == i ] # Append the sublists from the Knapsack items sorted by the Benefit Values (Max to Min)

    itemsInKnapsack = Knapsack(269, itemsOrd)

    print(itemsInKnapsack)
        

if "__main__" == __name__:
    main()
