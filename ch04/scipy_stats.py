from scipy.stats import bernoulli, poisson, uniform, expon, erlang, norm, triang

# Bernoulli
p = 0.5
x = 1
# Generate a probability using the PMF
print( bernoulli.pmf(x, p) )    # 0.5
# Generate a probability using the CDF
print( bernoulli.cdf(x, p) )    # 1.0
# Generate three Bernoulli random numbers
print( bernoulli.rvs(p, size = 3) ) # [0 1 0]

# Poisson
lmda = 2
x = 5
print( poisson.pmf(x, lmda) )
print( poisson.cdf(x, lmda) )
print( poisson.rvs(lmda, size = 3) )

# Uniform
a = 3
b = 10
x = 10
print( uniform.pdf(x, loc=a, scale=(b-a)) ) # = 1 / 7
print( uniform.cdf(x, loc=a, scale=(b-a)) ) # = 1.0
print( uniform.rvs(loc = 3, scale=(b-a), size = 3) )

# Exponential 
mu = 2
x = 2
print( expon.pdf(x, scale = (1 / mu)) )
print( expon.cdf(x, scale = (1 / mu)) )
print( expon.rvs( scale = (1 / mu), size = 3) )

# Triangular
a = 1
b = 10
c = 7
print( triang.rvs(c, loc = a, scale = (b - a), size = 3) )