import pandas as pd
import numpy as np
import html5lib

Math = {'Course':["Linear Algebra","Measure and Integration","Topology","Fourier Analysis"],"Grade":["A","TBA","TBA","TBA"]}
CSE  = {'Course':["Computational Complexity","Discrete Math"],"Grade":["TBA","A"]}
EE   = {'Course':["Statistical Learning Theory","Error Correcting Codes","Information Theory"],"Grade":["TBA","A","B-"]}
Books_Reading = []
Books_Read = []
Books_Queued=[]

fp = open('index.html','w')
Math = pd.DataFrame(Math);
Math = Math.to_html()
fp.write(Math)
CSE = pd.DataFrame(CSE);
CSE = CSE.to_html()
fp.write(CSE)
EE  = pd.DataFrame(EE);
EE  = EE.to_html()
fp.write(EE)
