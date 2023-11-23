def main():
    error_string = "Invalid input. Please enter integer value for n"
    try:
        n = int(input("Enter n: "))
        if n < 0:
            print(error_string)
            exit(0)

        string = []
        for i in range(n):
            string.append([])
            string[i].append(1)
            for j in range(1, i):
                string[i].append(string[i - 1][j - 1] + string[i - 1][j])
            if n != 0:
                string[i].append(1)
        for i in range(n):
            print(" " * (n - i), end=" ", sep=" ")
            for j in range(0, i + 1):
                print('{0:6}'.format(string[i][j]), end=" ", sep=" ")
            print()
    except ValueError:
        print(error_string)
        exit(0)


main()
