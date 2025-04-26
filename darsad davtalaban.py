import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


mu = 1019 
sigma = 209  
x_value = 820 


probability = stats.norm.cdf(x_value, mu, sigma)
print(f"درصد داوطلبانی که نمره‌ای کمتر از {x_value} دارند: {probability * 100:.2f}%")


x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="توزیع نرمال", color="blue")


x_fill = np.linspace(mu - 4*sigma, x_value, 500)
y_fill = stats.norm.pdf(x_fill, mu, sigma)
plt.fill_between(x_fill, y_fill, color="red", alpha=0.5, label="داوطلبان مردود")


plt.axvline(x_value, color="black", linestyle="--", label=f"حداقل نمره ({x_value})")
plt.xlabel("نمره")
plt.ylabel("چگالی احتمال")
plt.title("توزیع نرمال آزمون")
plt.legend()
plt.grid()
plt.show()
