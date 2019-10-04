import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import defaultdict



def panduan(file,trim_1=30,trim_2=30,ratio=2,interv=7, ignore=40):
    record = SeqIO.read(file, 'abi')
    channels = ['DATA9', 'DATA10', 'DATA11', 'DATA12']
    trace = defaultdict(list)
    #trim = 30
    for c in channels:
        trace[c] = record.annotations['abif_raw'][c]

    def jiequ(DATA, trim):
        if DATA== 'DATA9':
            hegan= 'G'
        if DATA== 'DATA10':
            hegan= 'A'
        if DATA== 'DATA11':
            hegan= 'T'
        if DATA== 'DATA12':
            hegan= 'C'
        
        record= []

        zancun= 0
        for n in range(1, len(trace[DATA])):
            daoshu= trace[DATA][n]-trace[DATA][n-1]
            if daoshu<0:
                if (zancun>0 and trace[DATA][n]>trim):
                    record.append((n, trace[DATA][n], hegan))
                zancun=-1
            else:
                zancun=1
        return record 

        
    record_g= jiequ('DATA9', ignore)
    record_a= jiequ('DATA10', ignore)
    record_t= jiequ('DATA11', ignore)
    record_c= jiequ('DATA12', ignore)


    xulie= record_a+ record_t+ record_c+ record_g
    xulie.sort()
    xulie1= []
    for item in xulie:
        xulie1.append(item[0])

    xulie2= []
    for item in xulie:
        xulie2.append(item[1])


    xulie3= []
    for item in xulie:
        xulie3.append(item[2])

       

    jiange= []
    for  x in range(1, len(xulie1)-1):
        jiange.append(xulie1[x]- xulie1[x-1])

    temp = []
    z= 0
    n= trim_1
    for y in jiange[trim_1: len(jiange)- trim_2]:
        n+= 1
        if y< interv and (xulie2[n]/xulie2[n-1]<ratio and xulie2[n-1]/xulie2[n]<ratio) :
            del xulie3[n]
            z+= 1
            temp.append(n)
            #print(xulie2[n]/xulie2[n-1])
            #print(n)
            #print(xulie3[n:n+10])
    #if z>0:
        #print(file)
        #print(z)

    return (file,xulie3,temp)
    #plt.plot(jiange, color='white',marker='o',mec='r', mfc='w')
    #plt.plot(record_a[0], record_a[1], color='white',marker='o',mec='r', mfc='w')
    #plt.plot(record_t[0], record_t[1], color='white',marker='*',mec='b', mfc='w')
    #plt.plot(record_c[0], record_c[1], color='white',marker='o',mec='y', mfc='w')
    #plt.plot(record_g[0], record_g[1], color='white',marker='o',mec='g', mfc='w')
    #plt.show()


