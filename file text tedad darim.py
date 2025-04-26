def calculate_average(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file.readlines()]
    
    return sum(numbers) / len(numbers)

filename = "numbers.txt"
average = calculate_average(filename)
print(f"میانگین عددها: {average}")
