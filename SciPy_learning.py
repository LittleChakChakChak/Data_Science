import numpy as np
from scipy import special
from scipy import integrate
import scipy
from scipy.fftpack import fft, ifft
from scipy import signal
from scipy import linalg

a = special.exp10(3)
print(a)

b = special.exp2(3)
print(b)

c = special.sindg(90)
print(c)

d = special.cosdg(45)
print(d)

print('-' * 40)

a = lambda x:special.exp10(x)
b = scipy.integrate.quad(a, 0, 1)
print(b)

print('-' * 40)

x = np.array([0,1,2,3])
y = fft(x)
print(y)

x = np.array([0,1,2,3])
y = ifft(x)
print(y)

print('-' * 40)

x = np.arange(35).reshape(7, 5)
domain = np.identity(3)
print(x,end='nn')
print(signal.order_filter(x, domain, 1))

print('-' * 40)

a = np.array([[1,2], [4,3]])
b = linalg.inv(a)
print(b)

a = np.array([[1,2], [4,3]])
b = linalg.det(a)
print(b)

print('-' * 20)

A = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 6, 3], [2, 3, 2, 5]])
a, b = linalg.eigh(A)
print("Selected eigenvalues :", a)
print("Complex ndarray :", b)