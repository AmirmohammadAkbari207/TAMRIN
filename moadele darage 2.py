import math

def solve_quadratic(a, b, c):
    # محاسبه دلتا
    delta = b**2 - 4*a*c
    print(f"دلتا: {delta}")
    
    if delta > 0:
        # دو ریشه حقیقی و متمایز
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"ریشه‌ها حقیقی و متمایز هستند: {root1} و {root2}")
    elif delta == 0:
        # دو ریشه حقیقی و برابر
        root = -b / (2 * a)
        print(f"ریشه‌ها حقیقی و برابر هستند: {root}")
    else:
        # ریشه‌ها موهومی
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print(f"ریشه‌ها موهومی هستند:")
        print(f"ریشه اول: {real_part} + {imaginary_part}i")
        print(f"ریشه دوم: {real_part} - {imaginary_part}i")

# دریافت ضرایب از کاربر
print("معادله درجه دوم به فرم ax^2 + bx + c = 0 است.")
a = float(input("ضریب a را وارد کنید: "))
b = float(input("ضریب b را وارد کنید: "))
c = float(input("ضریب c را وارد کنید: "))

# بررسی مقدار a
if a == 0:
    print("این معادله درجه دوم نیست! زیرا a نمی‌تواند صفر باشد.")
else:
    solve_quadratic(a, b, c)