
import numpy as np
from sensor import Sensor
from kalmanfilter import KalmanFilter
from visualizer import visualize

    
if __name__ == '__main__':

    X0 = np.matrix([[0], [0.8]])
    P0 = np.matrix([[1.,0.],[0.,1.]])
    T = 1.0
    F = np.matrix([[1,T],[0,1]])    
    H = np.matrix([[1.,0.]])        
    sigmaA = 0.001
    Q = np.matrix( [[0.25*T**4, 0.5*T**3],[0.5*T**3, T**2]] )* sigmaA
    sigmaX = 1.0
    R = np.matrix( [sigmaX] )
    
    kalmanfilter = KalmanFilter( X0, P0, F, H, Q, R )
    sensor = Sensor(0, 1, 1.0)
        
    
    for step in range(1,20):
        print( "\n\nstep: {}".format(step) )
        kalmanfilter.preditct()
        z = sensor.getMeasure(T*step)    
        kalmanfilter.update( z )            
        kalmanfilter.saveHist()
    
    visualize( kalmanfilter.XHist, kalmanfilter.PHist, sensor.xGtHist, sensor.vGtHist, sensor.xHist )

        

