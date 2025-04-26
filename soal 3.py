import random
import itertools


numbers = [random.randint(1, 15) for _ in range(20)]
print(f" لیست اعداد تصادفی: {numbers}")


for size in range(1, len(numbers) + 1):  
    for subset in itertools.combinations(numbers, size):
        if 50 <= sum(subset) <= 52:
            print(f" کوچک‌ترین مجموعه ممکن: {subset}, مجموع: {sum(subset)}")
            exit()
