def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# summa = 0
# counter = 1

# while True:
#     if counter > 1000:
#         break
#     if counter % 5 != 0:
#         counter += 1
#         continue

#     summa += counter
#     counter += 1

# counter = 1
# summa = 0
# while counter <= 1000:
#     if counter % 5 == 0:
#         summa += counter
#     counter += 1

# print(f"Summa: {summa}")

summa = sum(i for i in range(1, 1001) if i % 5 == 0)
print(f"Summa: {summa}")
