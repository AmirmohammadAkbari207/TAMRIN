count = 0

try:
    while True:  
        print(count)
        count += 1
except KeyboardInterrupt:
    print(f"شمارنده در مقدار {count} متوقف شد.")
except MemoryError:
    print("برنامه به دلیل کمبود حافظه متوقف شد.")
except Exception as e:
    print(f"برنامه به دلیل خطای زیر متوقف شد: {e}")