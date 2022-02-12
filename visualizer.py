import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

def visualize(XHist, PHist, xGtHist, vGtHist, xMeasHist):
    fig, axs = plt.subplots(3)
    fig.suptitle('KalmanFilter')
    
    steps = range(0,len(xGtHist))
    
    # draw x
    axs[0].plot(steps, xGtHist, label='ground truth')   
    axs[0].plot(steps, list(map(lambda X: X.item(0), XHist)), label='kalman')
    axs[0].plot(steps[1::], xMeasHist, label='measure')    
    axs[0].legend()    
    axs[0].set_xlabel('steps')
    axs[0].set_ylabel('distance x')
        
    
    axs[1].plot(steps, vGtHist, label='ground truth')   
    axs[1].plot(steps, list(map(lambda X: X.item(1), XHist)), label='kalman')
    axs[1].legend()    
    axs[1].set_xlabel('steps')
    axs[1].set_ylabel('velocity v')
    #axs[1].set_ylim(0,2)
    
    
    
    for i in steps:
        mu = XHist[i].item(0)
        sigma = PHist[i].item(0)
        d = np.linspace(mu-sigma*3, mu+sigma*3,100)
        axs[2].plot(d, norm.pdf(d,mu,sigma))   
    axs[2].set_xlabel('x')
    axs[2].set_ylabel('P(x)')
        
    # for i in steps:
    #     mu = XHist[i].item(1)
    #     sigma = PHist[i].item(3)
    #     d = np.linspace(mu-sigma*6, mu+sigma*6,100)
    #     axs[3].plot(d, norm.pdf(d,mu,sigma))   
    
    # axs[3].set_xlabel('v')
    # axs[3].set_ylabel('P(v)')
    
    plt.show()
