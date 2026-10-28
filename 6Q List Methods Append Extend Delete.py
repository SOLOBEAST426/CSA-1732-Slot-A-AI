numbers = [10, 20, 30]
print("Original List:", numbers)

numbers.insert(1, 15)
print("After Add:", numbers)

numbers.append(40)
print("After Append:", numbers)

numbers.extend([50, 60])
print("After Extend:", numbers)

del numbers[1]
print("After Delete:", numbers)
