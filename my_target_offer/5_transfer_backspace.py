def trans_space(data):
    if type(data) != str:
        return

    result = ""
    for i in range(len(data)):
        if data[i] == " ":
            result += "%20"
        else:
            result += data[i]
    return result

if __name__ == '__main__':
    data = input()      # "we are happy."
    result = trans_space(data)
    print(result)

