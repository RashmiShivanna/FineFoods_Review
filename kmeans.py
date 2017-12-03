
from sklearn import cluster as c
import numpy as np
import pandas as pd
import csv
from collections import Counter

df = pd.read_csv('vectors.csv')
kmeans = c.KMeans(n_clusters=10, random_state=0).fit(df)
print("cluster created")
Reviews = df.values
for i in range(len(labels)):
    print(1)
    clusters[labels[i]].append(Reviews[i])

f= open('Top5_Cluster.txt',"w+")
for i in range(len(clusters)):
        print("for cluster "+str(i))
        file1.write("for cluster "+str(i))
        cluster=pd.DataFrame(clusters[i])
        cluster.columns=columns
        sum={}
        for i in columns:
            sum[i]=cluster[i].sum()
        sorted_labels = sorted(sum.items(), key=operator.itemgetter(1), reverse=True)
        print(str(sorted_x))
        for i in range(5):
            print(sorted_labels[i])
            file1.write(str(sorted_labels[i]))
        file1.write('\n')
