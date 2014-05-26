import pylab as plt
import numpy as np

def processingFile(filename):
    underattack = []
    fullway = []
    halfway = []
    for f in filename:
        rd = open(f)
        d = []
        for i in rd:
            d.append(int(i))
        res = []
        for i in range(0, len(d)-1):
            res.append(d[i+1]-d[i])
        figureData = res[::2]

        underattack.append(np.mean(figureData[:10]))
        fullway.append(np.mean(figureData[10:20]))
        halfway.append(np.mean(figureData[20:]))
    return underattack, fullway, halfway


if __name__ == "__main__":
    files = ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt']

    ua, fw, hw = processingFile(files)
    print ua, fw, hw
    x = range(1,6)
    plt.plot(x, ua, marker='o', label='Without any protection')
    plt.plot(x, fw, marker='*', label='Naive SDN implementation')
    plt.plot(x, hw, marker='s', label='Improved proposal')
    plt.xlabel('Time tried (should be DDoS attack bandwidth ><)')
    plt.ylabel('Time elapsed for legitimate packets under attack(in 10-6 s)')
    plt.title("Average time elapsed of legitimate packet")
    plt.legend(bbox_to_anchor=(0., 1.06, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)
    # ind = np.arange(5)  # the x locations for the groups
    # width = 0.35 
    # fig, ax = pylab.subplots()

    # rects1 = ax.bar(ind, ua, width, color='r')
    # rects2 = ax.bar(ind+width, fw, width, color='y')
    # rects3 = ax.bar(ind+width*2, hw, width, color='b')
    # ax.set_xticks(ind+width*1.5)
    # ax.set_xlabel("DDoS attack bandwidth")
    # ax.set_ylabel("Time elapsed for legitimate packets under attack(in 10-6 s)")
    # ax.set_xticklabels( range(1,11) )
    # #ax.legend((rects1[0], rects2[0], rects3[0]), ('Normal case', 'Req & res go thru ctl', 'Req go thru ctl'))

    # pylab.title("Time elapsed")
    plt.show()
