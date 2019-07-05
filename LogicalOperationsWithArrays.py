import numpy as np
#np.genfromtxt('file.csv', delimiter=',')
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[porridge<60]
hot = porridge[porridge>80]
just_right = porridge[(porridge > 60) & (porridge < 80)]
print(porridge)
print(cold)
print(hot)
print(just_right)

#>>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
#>>> a > 5
#array([True, False, False, False, False, False, True, True, True, True], dtype=bool)
