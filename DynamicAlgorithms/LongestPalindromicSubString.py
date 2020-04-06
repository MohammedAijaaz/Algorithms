




def main():
    s = "babbad"
    n = len(s)
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    start_index = -1
    end_index = -1
    max_so_far = 0
    
    # size 1 palindromes
    i = 0
    while i < n:
        arr[i][i] = 1
        i += 1
        start, end = i, i
        max_so_far = 1

    # size 2 palindromes
    i = 0
    while i < n-1:
        if s[i] == s[i+1]:
            arr[i][i+1] = 1
            start = i
            end = i + 1
            max_so_far = 2
        i += 1

    # size 3 and more palindromes
    k = 3
    while k <= n:
        i = 0
        while i < n-k+1:
            j = i + k -1
            if s[i] == s[j] and arr[i+1][j-1] == 1:
                arr[i][j] = 1
                if k > max_so_far:
                    max_so_far = k
                    start = i
                    end = j
            i += 1
        k += 1

    print(s[start: end+1])


if __name__ == "__main__":
    main()