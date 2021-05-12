def main():
    print("Enter a sequence of non-decreasing numbers.")
    num = float(input("Enter num: "))
    seq_length = 1
    next_num = num
    while num <= next_num:
        num = next_num
        next_num = float(input("Enter num: "))
        if next_num >= num:
            seq_length += 1
    print("Thanks for playing!")            
    print("Sequence length: " + str(seq_length))


if __name__ == "__main__":
    main()
