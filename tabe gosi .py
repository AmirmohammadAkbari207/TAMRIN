import math

def gaussian_cdf(x, mu=0, sigma=1):
    """ تابع توزیع تجمعی گوسی برای مقدار x با میانگین mu و انحراف معیار sigma """
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


x_value = 1.5
mu = 0  
sigma = 1 
cdf_value = gaussian_cdf(x_value, mu, sigma)

print(f"توزیع تجمعی نرمال برای x={x_value}: {cdf_value:.4f}")
