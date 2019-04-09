# Python 3.6.7
import csv
import matplotlib   as plot
import numpy        as np
import numpy.linalg as lin
import pandas
import random       as rand

print("Assignment 3\n")

data = pandas.read_csv("glass.data").values.tolist()
rand.shuffle(data)
data = np.asarray(data)
attributes = data[:, 0:9]
classes = data[:, 10]
for i in range(len(classes)): # set 0 for windowed or A -- 1 for not or B
    classes[i] = 0 if classes[i] < 5 else 1

print (attributes)

c = ln(pseudoDeterminant(covariance(B))) - ln(pseudoDeterminant(covariance(A))) + (x-MB).T * pseudoInv(covariance(B)) * 