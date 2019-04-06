import pandas as pd 
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv (r'tes.csv')
rowlabels = [1,2]
df = df[['tinggi', 'berat']]

knn=KNeighborsClassifier(n_neighbors=3) #define K=1
label = [0,1,0,1,0,1,0,1,0,0,1,0,0,1,1]
knn.fit(df,label)
berat = input("Masukan Berat badan Kamu : ")
tinggi = input("Masukan Tinggi kamu : ")
hasil = knn.predict([[tinggi,berat]])

if	hasil==0 :
    	print ("ideal")
else :
    	print ("tidak ideal")