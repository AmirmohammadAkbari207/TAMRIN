def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# ورودی سال از کاربر
year = int(input("سال را وارد کنید: "))

if is_leap_year(year):
    print(f"سال {year} کبیسه است!")
else:
    print(f"سال {year} کبیسه نیست.")
    