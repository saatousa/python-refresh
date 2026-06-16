numbers = [100, 5, 8, 10, 15, 20, 80, 1]

def largest_number(nums):
    prev_value = 0
    for num in nums:
        if num > prev_value:
            prev_value = num
    return prev_value


def smallest_number(nums):
    prev_value = nums[0]
    for num in nums:
        if num < prev_value:
            prev_value = num
    return prev_value


def sum_of_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total


def is_even(nums):
    for num in nums:
        if num % 2 == 0:
            print(True)
        else:
             print(False)


# is_even(numbers)
# print(largest_number(numbers))
# print(smallest_number(numbers))
# print(sum_of_numbers(numbers))


names = ["Sara", "John", "Emma", "David"]

def print_names(names):
    for name in names:
        print(name)

print_names(names)

student = {
    "name": "Sara",
    "age": 25,
    "city": "New York"
}

for key,value in student.items():
    print(key, value)
