import statistics as stat
import math
sample_set = [3.2, 3, 2.8, 2.9, 3.1]
n = 5
mean = stat.mean(sample_set)
std_dev = stat.stdev(sample_set)
t = 2.776
ci1 = mean - t * (std_dev/math.sqrt(n))
ci2 = mean + t * (std_dev/math.sqrt(n))
print("Confidence Interval: ", round(ci1, 2), round(ci2, 2))