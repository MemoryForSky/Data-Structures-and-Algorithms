def same_number(array):
    number_dict = {}
    result = []
    for item in array:
        if item not in number_dict:
            number_dict[item] = 1
        else:
            result.append(item)
    return list(set(result))


if __name__ == "__main__":
    array = [2, 3, 1, 0, 2, 5, 3]
    result = same_number(array)
    print(result)





