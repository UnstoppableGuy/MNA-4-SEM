count = int(input())
numbers = input().split()
array = [abs(int(numbers[item])) for item in range(count)]
# print(numbers)
# print(array)
array.sort()
if array[count - 1] * array[count - 2] < abs(array[0] * array[1]):
    print(abs(array[0] * array[1]))
else:
    print(array[count - 1] * array[count - 2])

