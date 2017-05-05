adef main():
    numbers = [int(x) for x in raw_input().split(" ")] # List elements
    total, large, small = 0, 0, 0
    for i in range(0, len(numbers)):
        if (numbers[large] < numbers[i]): large = i
            if (numbers[small] > numbers[i]): small = i
                total = total + numbers[i]
                print("{} {}".format(total - numbers[large], total - numbers[small]))

if __name__ == "__main__":
    main()
