# -*- coding: utf-8 -*-



print ('')

print ('Migratory response to CTLA-4 Blockade)')
print ('Based on software developed by Metzner, C. et al. Nat Commun 6, 7516 (2015)')

print ('')


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from mpl_toolkits.axes_grid.inset_locator import inset_axes
import matplotlib.ticker as mticker


data=[None]*28

#reading previously generated posteriorMeanValues 

data[0] = open('ipi-df22_xy1_1 posteriorMeanValues.txt')
data[1] = open('ipi-df22_xy1_2 posteriorMeanValues.txt')
data[2] = open('ipi-df22_xy1_3 posteriorMeanValues.txt')
data[3] = open('ipi-df22_xy1_4 posteriorMeanValues.txt')
data[4] = open('ipi-df22_xy1_5 posteriorMeanValues.txt')
data[5] = open('ipi-df22_xy1_6 posteriorMeanValues.txt')
data[6] = open('ipi-df22_xy2_1 posteriorMeanValues.txt')
data[7] = open('ipi-df22_xy2_2 posteriorMeanValues.txt')
data[8] = open('ipi-df22_xy2_3 posteriorMeanValues.txt')
data[9] = open('ipi-df22_xy2_4 posteriorMeanValues.txt')
data[10] = open('ipi-df22_xy2_5 posteriorMeanValues.txt')
data[11] = open('ipi-df22xy2_6 posteriorMeanValues.txt')
data[12] = open('ipi-df22_xy2_7 posteriorMeanValues.txt')
data[13] = open('ipi-df22_xy3_1 posteriorMeanValues.txt')
data[14] = open('ipi-df22_xy3_3 posteriorMeanValues.txt')
data[15] = open('ipi-df22_xy3_4 posteriorMeanValues.txt')
data[16] = open('ipi-df22_xy3_5 posteriorMeanValues.txt')
data[17] = open('ipi-df22_xy3_6 posteriorMeanValues.txt')
data[18] = open('ipi-df22_xy4_1 posteriorMeanValues.txt')
data[19] = open('ipi-df22_xy4_2 posteriorMeanValues.txt')
data[20] = open('ipi-df22_xy4_4 posteriorMeanValues.txt')
data[21] = open('ipi-df22_xy4_5 posteriorMeanValues.txt')
data[22] = open('ipi-df22_xy4_6 posteriorMeanValues.txt')
data[23] = open('ipi-df22_xy5_3 posteriorMeanValues.txt')
data[24] = open('ipi-df22_xy5_4 posteriorMeanValues.txt')
data[25] = open('ipi-df22_xy5_5 posteriorMeanValues.txt')
data[26] = open('ipi-df22_xy5_7 posteriorMeanValues.txt')
data[27] = open('ipi-df22_xy5_8 posteriorMeanValues.txt')

    
def dataread(data)   :
    yourfile = []
    for line in data:
 	    line = line.replace('\n','').replace('\r','')
 	    line = line.split(' ')
 	    line[0] = float(line[0])
 	    line[1] = float(line[1])
 	#print line
 	    yourfile.append(line)
    """while True:
 	a = input('Raw number: ')
 	b = input('Col number: ')
 	print yourfile[a-1][b-1], type(yourfile[a-1][b-1])
"""
    col1 = []
    for raw in yourfile:
 	    col1.append(raw[0])
    col2 = []
    for raw in yourfile:
 	    col2.append(raw[1])

    return [col1,col2]


cells=[None]*28
 
for i in range(0,28):
    cells[i]=dataread(data[i])
    
    
paramSequ=[None]*28   
for i in range(0,28):
    paramSequ[i]=np.array(cells[i])     
 

def simulateTVAR(paramSequ):
    veloSequ = np.empty((len(paramSequ[0]),2))
    uOld = np.array([0.0,0.0])
    
    for i in range(len(veloSequ)):
        uNew = paramSequ[0,i]*uOld + paramSequ[1,i]*np.random.randn(2)
        veloSequ[i] = uNew
        uOld = uNew
    
    return veloSequ


veloSequArray=[None]*28

for i in range(0,28):
    veloSequArray[i] = simulateTVAR(paramSequ[i])
    

gridSize = 200
qBound = [-1, 1]
aBound = [ -1000, 10000]

# Setting parameters of algorithm
pMin = 1.0*10**(-7)
Rq   = 2
Ra   = 2


# parameter grid (excluding boundary values)
qGrid  = (np.array([np.linspace(qBound[0], qBound[1], gridSize+2)[1:-1]]*gridSize)).T
aGrid  = (np.array([np.linspace(aBound[0], aBound[1], gridSize+2)[1:-1]]*gridSize))
a2Grid = (np.array([np.linspace(aBound[0], aBound[1], gridSize+2)[1:-1]]*gridSize))**2

# likelihood evaluation on parameter grid
def compLike(vp,v):
    return np.exp(-((v[0] - qGrid*vp[0])**2 + (v[1] - qGrid*vp[1])**2)/(2*a2Grid) - np.log(2*np.pi*a2Grid))

# posterior distribution as new prior

def compNewPrior(oldPrior,like):
    
    post = oldPrior*like
    post /= np.sum(post)
    newPrior = post
    
    # introduce minimal probability
    mask = newPrior < pMin
    newPrior[mask] = pMin
    
    # boxcar filter
    ker = np.ones((2*Rq + 1, 2*Ra+1))/((2*Rq+1)*(2*Ra+1))
    
    newPrior = convolve2d(newPrior, ker, mode='same', boundary='symm')
    
    return newPrior

# compute sequence of posterior distributions for a sequence of measured velocities

def compPostSequ(uList):
    # initialize array for posterior distributions
    dist = np.empty((len(uList),gridSize,gridSize))

    # initialize flat prior
    dist[0].fill(1.0/(gridSize**2))

    # forward pass (create forward priors for all time steps)
    for i in np.arange(1,len(uList)):
        dist[i] = compNewPrior(dist[i-1], compLike(uList[i-1], uList[i]))

    # backward pass
    backwardPrior = np.ones((gridSize,gridSize))/(gridSize**2)
    for i in np.arange(1,len(uList))[::-1]:
        # re-compute likelihood
        like = compLike(uList[i-1], uList[i])
    
        # forward prior * likelihood * backward prior
        dist[i] = dist[i-1]*like*backwardPrior
        dist[i] /= np.sum(dist[i])
        
        # generate new backward prior for next iteration
        backwardPrior = compNewPrior(backwardPrior, compLike(uList[i-1], uList[i]))
    
    # drop initial flat prior before return
    return dist[1:]

# compute posterior mean values from a list of posterior distributions
def compPostMean(postSequ):
    qMean = [np.sum(post*qGrid) for post in postSequ]
    aMean = [np.sum(post*aGrid) for post in postSequ]
    
    return np.array([qMean,aMean])


# The algorithm applys to the simulated cell trajectories  


print ('Started inference algorithm...')
print ('Computed sequences of posterior distributions.')
print ('Computed posterior mean values.')



postSequArray=[None]*28
meanPost=[None]*28
for i in range(0,28):
    postSequArray[i]=compPostSequ(veloSequArray[i])
    meanPost[i]=compPostMean(postSequArray[i])
    


### Plotting


print ('Plotting posterior mean values...')

fig, ax = plt.subplots(7,4,figsize=(8,10))
fig.canvas.set_window_title('Posterior mean values')
fig.subplots_adjust(wspace=0.3)
fig.subplots_adjust(hspace=0.3)
fig.suptitle('CTLA-4 Blockage', fontsize=12)
fig.subplots_adjust(top=0.93)
fig.text(0.5, 0.06, 'Time Steps', ha='center')
fig.text(0.04, 0.5, 'Single Cell Activity', va='center', rotation='vertical')


for j in range(0,7):
 for i in range(0,4):
 
   ax[j,i].set_ylim(-1000,10000)
   if j==0:
    ax[j,i].plot(paramSequ[i+j][1], lw=2., alpha=.8,label='Single cell Activity'
               ,c='hotpink')
    ax[j,i].plot(meanPost[i+j][1], lw=2., alpha=.8,label='Simulation')
   elif j==1:
    ax[j,i].plot(paramSequ[i+j+3][1], lw=2., alpha=.8,label='Single cell Activity'
               ,c='hotpink')
    ax[j,i].plot(meanPost[i+j+3][1], lw=2., alpha=.8,label='Simulation')
   elif j==2:
       
    ax[j,i].plot(paramSequ[i+j+6][1], lw=2., alpha=.8,label='Single cell Activity'
               ,c='hotpink')   
    ax[j,i].plot(meanPost[i+j+6][1], lw=2., alpha=.8,label='Simulation')
   elif j==3:
    ax[j,i].plot(paramSequ[i+j+9][1], lw=2., alpha=.8,label='Single cell Activity'
               ,c='hotpink')   
    ax[j,i].plot(meanPost[i+j+9][1], lw=2., alpha=.8,label='Simulation')
   elif j==4:
    ax[j,i].plot(paramSequ[i+j+12][1], lw=2., alpha=.8,label='Single cell Activity'
               ,c='hotpink')   
    ax[j,i].plot(meanPost[i+j+12][1], lw=2., alpha=.8,label='Simulation')
   elif j==5:
    ax[j,i].plot(paramSequ[i+j+15][1], lw=2., alpha=.8,label='Single cell Activity'
               ,c='hotpink')   
    ax[j,i].plot(meanPost[i+j+15][1], lw=2., alpha=.8,label='Simulation')
            
   elif j==6:
    ax[j,i].plot(paramSequ[i+j+18][1], lw=2., alpha=.8,label='Single cell Activity'
               ,c='hotpink')   
    ax[j,i].plot(meanPost[i+j+18][1], lw=2., alpha=.8,label='Simulation')
   
    
  
  
for j in range(0,7):
 for i in range(0,4):
     
       
     inset_axesP= inset_axes(ax[j,i], 
                    width="40%", 
                    height=.3, 
                    loc=1)
     if j==0:
          inset_axesP.plot(paramSequ[i+j][0], lw=2., alpha=.8,c='#39ad48'
                  ,label='Single Cell Persistence')
          inset_axesP.plot(meanPost[i+j][0], lw=2, alpha=.8)
     elif j==1:
        inset_axesP.plot(paramSequ[i+3+j][0], lw=2., alpha=.8,c='#39ad48'
                  ,label='Single Cell Persistence')
        inset_axesP.plot(meanPost[i+3+j][0], lw=2, alpha=.8)
     elif j==2:
           inset_axesP.plot(paramSequ[i+6+j][0], lw=2., alpha=.8,c='#39ad48'
                  ,label='Single Cell Persistence')
           inset_axesP.plot(meanPost[i+6+j][0], lw=2, alpha=.8)
     elif j==3:
               inset_axesP.plot(paramSequ[i+9+j][0], lw=2., alpha=.8,c='#39ad48'
                  ,label='Single Cell Persistence')
               inset_axesP.plot(meanPost[i+9+j][0], lw=2, alpha=.8)
     elif j==4:
                   inset_axesP.plot(paramSequ[i+12+j][0], lw=2., alpha=.8,c='#39ad48'
                  ,label='Single Cell Persistence')
                   inset_axesP.plot(meanPost[i+12+j][0], lw=2, alpha=.8)
     elif j==5:
                       inset_axesP.plot(paramSequ[i+15+j][0], lw=2., alpha=.8,c='#39ad48'
                       ,label='Single Cell Persistence')
                       inset_axesP.plot(meanPost[i+15+j][0], lw=2, alpha=.8)
     elif j==6:
                           inset_axesP.plot(paramSequ[i+18+j][0], lw=2., alpha=.8,c='#39ad48'
                  ,label='Single Cell Persistence')
                           inset_axesP.plot(meanPost[i+18+j][0], lw=2, alpha=.8)
                           
     inset_axesP.set_ylim(-1,1)  
     inset_axesP.set_ylabel('P',fontsize=6,labelpad=1)
     plt.xticks([])


formatter = mticker.ScalarFormatter(useMathText=True)
formatter.set_powerlimits((-3,2))

for j in range(0,7):
 for i in range(0,4):
     
      ax[j,i].yaxis.set_major_formatter(formatter)

      
for j in range(0,7):
 for i in range(0,4):
         
      ax[j,i].tick_params(axis='both', labelsize=5.5)


for j in range(0,7):
 for i in range(0,4):
     
      ax[j,i].yaxis.set_ticks(np.arange(0,10000,2500))


ax[0,0].text(5, 3000, '#DFCI-22-1-1', fontsize=5.5,style='italic')
ax[0,1].text(5, 3000, '#DFCI-22-1-2', fontsize=5.5,style='italic')
ax[0,2].text(5, 3000, '#DFCI-22-1-3', fontsize=5.5,style='italic')
ax[0,3].text(5, 3000, '#DFCI-22-1-4', fontsize=5.5,style='italic')

ax[1,0].text(5, 3000, '#DFCI-22-1-5', fontsize=5.5,style='italic')
ax[1,1].text(5, 3000, '#DFCI-22-1-6', fontsize=5.5,style='italic')
ax[1,2].text(5, 3000, '#DFCI-22-2-1', fontsize=5.5,style='italic')
ax[1,3].text(5, 3000, '#DFCI-22-2-2', fontsize=5.5,style='italic')

ax[2,0].text(5, 3000, '#DFCI-22-2-3', fontsize=5.5,style='italic')
ax[2,1].text(5, 3000, '#DFCI-22-2-4', fontsize=5.5,style='italic')
ax[2,2].text(5, 3000, '#DFCI-22-2-5', fontsize=5.5,style='italic')
ax[2,3].text(5, 3000, '#DFCI-22-2-6', fontsize=5.5,style='italic')

ax[3,0].text(5, 3000, '#DFCI-22-2-7', fontsize=5.5,style='italic')
ax[3,1].text(5, 3000, '#DFCI-22-3-1', fontsize=5.5,style='italic')
ax[3,2].text(5, 3000, '#DFCI-22-3-3', fontsize=5.5,style='italic')
ax[3,3].text(5, 3000, '#DFCI-22-3-4', fontsize=5.5,style='italic')

ax[4,0].text(5, 3000, '#DFCI-22-3-5', fontsize=5.5,style='italic')
ax[4,1].text(5, 3000, '#DFCI-22-3-6', fontsize=5.5,style='italic')
ax[4,2].text(5, 3000, '#DFCI-22-4-1', fontsize=5.5,style='italic')
ax[4,3].text(5, 3000, '#DFCI-22-4-2', fontsize=5.5,style='italic')

ax[5,0].text(5, 3000, '#DFCI-22-4-4', fontsize=5.5,style='italic')
ax[5,1].text(5, 3000, '#DFCI-22-4-5', fontsize=5.5,style='italic')
ax[5,2].text(5, 3000, '#DFCI-22-4-6', fontsize=5.5,style='italic')
ax[5,3].text(5, 3000, '#DFCI-22-5-3', fontsize=5.5,style='italic')

ax[6,0].text(5, 3000, '#DFCI-22-5-4', fontsize=5.5,style='italic')
ax[6,1].text(5, 3000, '#DFCI-22-5-5', fontsize=5.5,style='italic')
ax[6,2].text(5, 3000, '#DFCI-22-5-7', fontsize=5.5,style='italic')
ax[6,3].text(5, 3000, '#DFCI-22-5-8', fontsize=5.5,style='italic')



plt.rc('ytick',labelsize=5)

lines_labels = [ax[0,0].get_legend_handles_labels(),
                inset_axesP.get_legend_handles_labels()]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]

fig.legend(lines, labels,loc='lower center',ncol=3)


plt.draw()
plt.savefig('Posterior_mean_values.png', format='png')

