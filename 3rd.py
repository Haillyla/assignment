import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import csv
a = []
data = []
with open('Stats.csv', mode='r', encoding='utf-8-sig') as file:
    csvFile = csv.reader(file)
    next(csvFile)
    for lines in csvFile:
        try:
            row = [float(lines[8]), float(lines[9]), float(lines[10]), float(lines[11]), float(lines[12]), float(lines[13]), float(lines[14]), float(lines[15]), float(lines[16]), float(lines[17]), float(lines[18]), float(lines[19]), float(lines[20]), float(lines[21]), float(lines[22]), float(lines[23]), float(lines[24]), float(lines[25]), float(lines[26]), float(lines[27]), float(lines[28]), float(lines[29]), float(lines[30]), float(lines[31]), float(lines[32]), float(lines[33]), float(lines[34]), float(lines[35]), float(lines[36]), float(lines[37]), float(lines[38]), float(lines[39]), float(lines[40]), float(lines[41]), float(lines[42]), float(lines[43]), float(lines[44]), float(lines[45]), float(lines[46]), float(lines[47]), float(lines[48]), float(lines[49]), float(lines[50]), float(lines[51]), float(lines[52]), float(lines[53]), float(lines[54]), float(lines[55]), float(lines[56]), float(lines[57]), float(lines[58]), float(lines[59]), float(lines[60]), float(lines[61]), float(lines[62]), float(lines[63]), float(lines[64]), float(lines[65]), float(lines[66]), float(lines[67]), float(lines[68]), float(lines[69]), float(lines[70]), float(lines[71]), float(lines[72]), float(lines[73]), float(lines[74]), float(lines[75]), float(lines[76])]
            data.append(row)
        except (ValueError, IndexError):    
            continue
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

kmeans = KMeans(n_clusters=7, random_state=0)
labels = kmeans.fit_predict(data_scaled)

plt.figure(figsize=(8, 6))
data_np = np.array(data)
for i in range(7):
    cluster = data_np[labels == i]
    plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Group {i+1}')


centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200, label='center')


plt.legend()
plt.grid(True)
plt.show()
