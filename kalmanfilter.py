class KalmanFilter:
    def __init__(self, X0, P0, F, H, Q, R ) -> None:
        self.X = X0
        self.P = P0
        self.F = F
        self.H = H
        self.Q = Q
        self.R = R
        
        self.XHist = [X0]
        self.PHist = [P0]
        
    def preditct(self):
        self.X = self.F * self.X
        self.P = self.F*self.P*self.F.T + self.Q
        print("\n predict:")   
        self.print()
        
    def update(self, z ):
        zPred = self.H * self.X
        S = self.H*self.P*self.H.T + self.R 
        K = self.P* self.H.T* S.I 
        self.X = self.X + K *(z - zPred)
        self.P = self.P - K*S*K.T
        print("\n udpate:")   
        print("S: \n {}".format(S))
        print("K: \n {}".format(K))
        self.print()
     
    
    def saveHist(self):
        self.XHist.append(self.X)
        self.PHist.append(self.P)
    
    def print(self):  
        print("X: \n {}".format(self.X))
        print("P: \n {}".format(self.P))
        print("F: \n {}".format(self.F))
        print("H: \n {}".format(self.H))
        print("Q: \n {}".format(self.Q))
        print("R: \n {}".format(self.R))
        

