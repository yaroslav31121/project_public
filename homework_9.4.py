def sum_of_naturals(start, end):
    if start > end:
        return 0
    else:
        return start + sum_of_naturals(start + 1, end)

start_num = int(input("Введіть початкове число: "))
end_num = int(input("Введіть кінцеве число: "))

result = sum_of_naturals(start_num, end_num)
print(f"Сума натуральних чисел від {start_num} до {end_num} дорівнює {result}")
