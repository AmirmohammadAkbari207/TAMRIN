def read_numbers(filename):
    """مرحله ۱: خواندن اعداد از فایل"""
    with open(filename, 'r') as file:
        for line in file:
            yield float(line.strip())  

def compute_average(numbers):
    """مرحله ۲: محاسبه میانگین"""
    total, count = 0, 0
    for num in numbers:
        total += num
        count += 1
    return total / count if count > 0 else 0


filename = "numbers.txt"
numbers = read_numbers(filename)  
average = compute_average(numbers) 
print(f"میانگین عددها: {average}")
