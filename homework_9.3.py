def count_ways_to_climb(n):
    if n == 0 or n == 1:
        return 1
    else:
        return count_ways_to_climb(n - 1) + count_ways_to_climb(n - 2)

n = int(input("Введіть кількість сходинок: "))
ways = count_ways_to_climb(n)
print(f"Кількість способів підняття на {n} сходинку: {ways}")
