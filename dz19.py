numbers = [-2, 3, 8, -11, -4, 6]

negative_count = 0

for num in numbers:
    if num < 0:
        negative_count = negative_count + 1

print(f"Количество отрицательных чисел: {negative_count}")