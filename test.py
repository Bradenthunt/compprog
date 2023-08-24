def tuple_slice(startIndex, endIndex, tup):
    sliced = str(tup[slice(startIndex, endIndex)])
    answer = ''.join(sliced)

    return answer

if __name__ == "__main__":
    print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))