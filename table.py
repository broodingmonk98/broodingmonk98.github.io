import pandas as pd
import numpy as np
import html5lib

Math = {'Course':["Linear Algebra","Measure and Integration","Topology","Fourier Analysis"],"Grade":["A","TBA","TBA","TBA"]}
CSE  = {'Course':["Computational Complexity","Discrete Math"],"Grade":["TBA","A"]}
EE   = {'Course':["Statistical Learning Theory","Error Correcting Codes","Information Theory"],"Grade":["TBA","A","B-"]}
Books_cur = {'Book':['Notes on set theory','Math Analysis','Topology','Measure Theory','Probability'],
        'Author': ['Yiannis','Rudin','Simmons','Halmos','Feller'],
        'Comments':['','','','','']}
#'queued':{'Math':['Fourier analysis on groups-rudin','Real and Complex analysis-rudin','Functional Analysis-rudin',
#    'Advanced Linear Algebra-Romero','Abstract Algebra-dummit','Topology-Munkres'],"CSE":['Finite Model Theory-libkin','Descriptive Complexity-Immerman']}}
fp = open('index.html','w')
fp.write("This is meant to serve as an informal CV/get to know me page, which I also use\
        to keep track of what I'm up to<br><br>");
fp.write("<br><H2>About me:<end H2><br><br>")
fp.write("<p><H5>I'm a second year Engineering Science (Btech) Student at Indian Institute of Technology - Hyderabad\
        but I find myself moreo oriented towards research, especially in abstract topics, which is why I'm particularly\
        dawn to Math (Especially set theory) as well as theoritical computer science. Take a look at the currently reading\
        and currently working on sectionso to gauge my current interests<H5><p>")

Math = pd.DataFrame(Math);
Math = Math.to_html()
fp.write(Math)
CSE = pd.DataFrame(CSE);
CSE = CSE.to_html()
fp.write(CSE)
EE  = pd.DataFrame(EE);
EE  = EE.to_html()
fp.write(EE)
current  = pd.DataFrame(Books_cur);
current  = current.to_html()
fp.write("<H3>Currently Reading<H3><br><br>");
fp.write('Math books')
fp.write(current)
#current  = pd.DataFrame(Books['queued']);
#current  = current.to_html()
#fp.write(current)
Books_cur = {'Book':['Graph Theory','Computational Complexity','Algebraic automata theory','Descriptive Complexity'],
        'Author': ['Diestel','Arora-Borak','Lecture Notes','Immerman'],
        'Comments':['','','','']}

current  = pd.DataFrame(Books_cur);
current  = current.to_html()
fp.write('CS books (mostly theory)')
fp.write(current)
