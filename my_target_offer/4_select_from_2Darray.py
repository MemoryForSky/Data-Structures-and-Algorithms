def search_num(array2D, target):
    if array2D == None:
        return 0

    rows, columns = len(array2D), len(array2D[0])
    row = 0
    column = columns - 1
    found = False
    while row < rows and column >= 0:
        if target == array2D[row][column]:
            found = True
            break
        elif target < array2D[row][column]:
            column -= 1
        else:
            row += 1

    return found

if __name__ == "__main__":
    array2D = [[]]
    if search_num(array2D, 10):
        print("found")
    else:
        print("not found")



