def is_prime(num):
    """ چک می‌کند که آیا عدد اول است یا نه """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_kth_prime_after_n(n, k):
    """ پیدا کردن k-امین عدد اول بعد از n """
    count = 0
    num = n + 1  
    while count < k:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1  


n = int(input("عدد n را وارد کنید: "))
k = int(input("عدد k را وارد کنید: "))


result = find_kth_prime_after_n(n, k)
print(f"{k}-امین عدد اول بعد از {n}: {result}")
