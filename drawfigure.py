import pylab
import numpy as np


rd = open("rawdata.txt")
#rd = open("log-0502.txt")
d = []
for i in rd:
    d.append(int(i))
res = []
for i in range(0, len(d)-1):
    res.append(d[i+1]-d[i])


figureData = res[::2]
ind = np.arange(10)  # the x locations for the groups
width = 0.35 
fig, ax = pylab.subplots()

rects1 = ax.bar(ind, figureData[:10],width, color='r')
rects2 = ax.bar(ind+width, figureData[10:],width, color='y')
ax.set_xticks(ind+width)
ax.set_xlabel("Time tried")
ax.set_ylabel("Time elapsed (in 10-6 s)")
ax.set_xticklabels( range(1,11) )
ax.legend((rects1[0], rects2[0]), ('Normal case', 'Req & res go thru ctl'))

pylab.title("Time elapsed")
pylab.show()
