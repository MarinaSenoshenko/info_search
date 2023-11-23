def is_valid_sequence(sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack:
            stack.pop()
        else:
            return False
    return len(stack) == 0


def main():
    sequence = str(input("Enter bracket sequence: "))

    if is_valid_sequence(sequence):
        print("correct sequence")
        return
    print("incorrect sequence")


main()
