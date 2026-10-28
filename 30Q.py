def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk from", source, "to", destination)
        return

    hanoi(n - 1, source, auxiliary, destination)
    print("Move disk from", source, "to", destination)
    hanoi(n - 1, auxiliary, destination, source)


n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'C', 'B')