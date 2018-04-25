import pandas as pd
import numpy as np
import html5lib

Math = {'Course':["Linear Algebra","Measure and Integration","Topology","Fourier Analysis"],"Grade":["A","TBA","TBA","TBA"]}
Math = pd.DataFrame(Math);
Math = Math.to_html()
fp = open('data.html','w')
fp.write(Math)
