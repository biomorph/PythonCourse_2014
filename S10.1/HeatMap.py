__author__ = 'ravi'
import numpy as np
import pandas
import scipy
import scipy.cluster.hierarchy as hier
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt

a = pandas.read_table('HeatMap_Diff.txt')
a = a[(a['20MG/CTRL']>1) | (a['20MG/CTRL']<-1)]
a = a[(a['100MG/CTRL']>1) | (a['100MG/CTRL']<-1)]
a.to_csv('2fold_diff.tab',sep='\t',header=None,index=False)
a = pandas.read_table('2fold_diff.tab',header=None)
dataMatrix = np.array(a.icol([1,2]))
distanceMatrix =  dist.pdist(dataMatrix,'euclidean')
distanceSquareMatrix = dist.squareform(distanceMatrix)
linkageMatrix = scipy.cluster.hierarchy.linkage(distanceSquareMatrix)
heatmapOrder = hier.leaves_list(linkageMatrix)
rowHeaders = a.icol(0)
roworder = []
for n in heatmapOrder: roworder.append(rowHeaders[n])


orderedDataMatrix = dataMatrix[heatmapOrder,:]

rowHeaders = np.array(rowHeaders)
orderedRowHeaders = rowHeaders[heatmapOrder,:]
#do the same for the row headers
outFile='HeatMapOut.tab'
fh=open(outFile,'w')
fh.write('Gene'+'\t'+'\t'.join(['CTRL_20MG','CTRL_100MG'])+'\n')
z=zip(orderedRowHeaders,orderedDataMatrix)
for n in z:
    fh.write(n[0]+'\t'+'\t'.join(map(str,list(n[1])))+'\n')
fh.close()

dataArray = np.array(pandas.read_table('HeatMapOut.tab').icol([1,2]))

fig, ax = plt.subplots()
heatmap= plt.pcolor(dataArray,cmap=plt.cm.RdBu,vmin=-3,vmax=3)
plt.savefig('HeatMap.pdf')