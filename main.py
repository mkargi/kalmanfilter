import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import norm


T = 1.0
x_axis = np.arange(-5, 13, 0.01)


def getGt(step):
    velcotiy_gt = 1.0
    x0_gt = 0.0
    gt = x0_gt + T*step*velcotiy_gt
    
    return gt

def getMeasure(step):
    error = s = np.random.normal(0, 1.0)
    
    return getGt(step) + error   
    


if __name__ == '__main__':
    
    xList = list()
    measuremntList = list()
    groundTruthList = list()
    stepList = list()
    
    X = np.array([[0],[0.6]])
    F = np.array([[1.,T],[0.,1.]])
    print("F: \n {}".format(F))
    P = np.array([[1.,0.],[0.,1.]])
    H = np.array([[1.,0.]])
    
    
    sigmaA = 0.001
    Q = np.array( [[0.25*pow(T,4), 0.5*pow(T,3)],[0.5*pow(T,3), pow(T,2)]] )* sigmaA
    sigmaX = 1.0
    R = np.array( [sigmaX] )
    
    fig = plt.figure()   
    #plt.plot(x_axis, norm.pdf(x_axis,X[0],P[0][0]))
    
    for step in range(1,100):    
        print("step: {}".format(step) )
        
        print("F: \n {}".format(F))
        X = np.matmul(F,X)
        print("X pred: \n {}".format(X))
        FT = F.transpose().copy()
        P = np.matmul(np.matmul(F,P),FT) + Q
        print("F: \n {}".format(F))
        
        print("Q: \n {}".format(Q))
        print("P pred: \n {}".format(P))
        
        ZPred = np.matmul(H,X)
        print("H: \n {}".format(H))
        print("Z pred: \n {}".format(ZPred))
        
        
        S = np.matmul(np.matmul(H,P),H.transpose().copy()) + R 
        print("S: \n {}".format(S))

       
        K = np.matmul(P,H.transpose().copy()) * np.linalg.inv(S).copy()
        print("K: \n {}".format(K))
        
        Z = getMeasure(step)
        print("Z: \n {}".format(Z))
        
        X = X + K*(Z-ZPred)
        print("X pred: \n {}".format(X))
        
        P = P - np.matmul(np.matmul(K,S),K.transpose().copy())
        print("P pred: \n {}".format(P))
        
        stepList.append(step)
        xList.append( X[0] )
        measuremntList.append( Z )
        groundTruthList.append( getGt(step) )

    
    plt.plot( stepList, groundTruthList )     
    plt.plot( stepList, measuremntList )  
    plt.plot( stepList, xList )        
    #plt.ylim([0,10])
    plt.show()
        

