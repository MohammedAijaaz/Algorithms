# Kadane's algorithm


def main():

    arr = [-2, -3, 4, -1, -2, 1, 5, -3]

    res = arr[0]
    curr_max = arr[0]

    for a in arr[1:]:
        curr_max = max(a, a+curr_max)
        res = max(res, curr_max)
    print(res)
    return res


if __name__ == "__main__":
    main()
