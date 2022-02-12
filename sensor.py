import numpy as np

class Sensor:
    def __init__(self, xGt, vGt, sigmaW) -> None:
        self.xGt = xGt
        self.vGt = vGt
        self.sigmaW = sigmaW
        
        self.xGtHist = [xGt]
        self.vGtHist = [vGt]
        self.xHist = []
    
    def getMeasure(self, t):
        xGt,vGt = self.getGroundTruth(t)
        x = xGt + np.random.normal(0, self.sigmaW)        
        self.xGtHist.append( xGt )
        self.vGtHist.append( vGt )
        self.xHist.append( x )     
        print( "xGt: {}".format( xGt ))
        print( "z: {}".format( x ))         
        return x
        
    def getGroundTruth(self, t):
        return [self.xGt + self.vGt * t, self.vGt]