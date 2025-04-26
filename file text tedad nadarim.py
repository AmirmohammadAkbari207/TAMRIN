def calculate_average_dynamic(filename):
    with open(filename, 'r') as file:
        total, count = 0, 0
        for line in file:
            total += float(line.strip())
            count += 1
    
    return total / count if count > 0 else 0

filename = "numbers.txt"
average = calculate_average_dynamic(filename)
print(f"میانگین عددها: {average}")
