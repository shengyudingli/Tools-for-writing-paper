import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

engfre = np.zeros((26,26))

engcorpus = open("words.txt").readlines()

engtotal=0.0

for i in engcorpus:
    i = i.replace("\n","").replace(" ","").replace("-","")
    length = len(i)
    if length< 1:
        continue
    idx = 0
    while idx<length-1:
        print(i)
        engfre[ord(i[idx])-97][ord(i[idx+1])-97] +=1
        engtotal+=1
        idx+=1
engfre = engfre/engtotal
print(engfre)

column = []
for i in range(0,26):
    column.append(chr(i+97))

def drawHeatMap(matric):

    fig, ax = plt.subplots(figsize = (9,9))
    #二维的数组的热力图，横轴和数轴的ticklabels要加上去的话，既可以通过将array转换成有column
    #和index的DataFrame直接绘图生成，也可以后续再加上去。后面加上去的话，更灵活，包括可设置labels大小方向等。
    sns.heatmap(engfre,  xticklabels=column,yticklabels=column, vmax=0.2,vmin = 0,  square=True, cmap="YlGnBu")

    sns.heatmap(pd.DataFrame(engfre, columns =column, index = column), 
                    annot=False, vmax=0.01,vmin = 0, xticklabels= True, yticklabels= True, square=True, cmap="YlGnBu")

    #sns.heatmap(np.round(a,2), annot=True, vmax=1,vmin = 0, xticklabels= True, yticklabels= True, 
    #            square=True, cmap="YlGnBu")
    ax.set_title('2-Gram distribution of English words', fontsize = 15)
    ax.set_ylabel('First Character', fontsize = 15)
    ax.set_xlabel('Second Character', fontsize = 15)
    plt.savefig('full_malay.jpg')



    
