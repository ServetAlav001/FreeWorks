import numpy as np

#python listesinden numpy array oluşturma

np_x=np.random.randint(1,100,3)
print("Random Integer Array:", np_x)

np_zero=np.zeros(20)
print("Zero Array:\n", np_zero)
np_one=np.ones(20)
print("One Array:\n", np_one)
np_empty=np.empty(20)
print("Empty Array:\n", np_empty)
np_sin=np.arange(10,50,2)
print("Arange Array:\n", np_sin)
np_lin=np.linspace(0,100,12)
print("Linspace Array:\n", np_lin)
np_log=np.logspace(0,10,3)
print("Logspace Array:\n", np_log)
np_sinus=np.sin(np_lin)
print("Sinus Array:\n", np_sinus)
