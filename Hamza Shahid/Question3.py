#In this, we are finding mode

from scipy import stats

speed = [99, 98, 77, 66, 77, 55, 88, 77]

x = stats.mode(speed)
print(x)