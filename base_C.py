import numpy as np
import pandas as pd

file1 = []
baseC = []
final_baseC = []
with open("test.pdb") as file:
    for line in file:
        if (line[0:4] == "ATOM"):
            a = line.split()
            file1.append(a)
            
    
for line in file1:
    if(line[3]=="DC" and (line[2]=="N1" or line[2]=="C2" or line[2]=="O2" or line[2]=="N3" or line[2]=="C4" or line[2]=="N4" or line[2]=="C5" or line[2]=="C6")):
        baseC.append(float(line[6]))
        baseC.append(float(line[7]))
        baseC.append(float(line[8]))
        final_baseC.append(baseC)
        baseC = []

baseC_cg = []
final_baseC_cg = []
constraintsCX = []
constraintsCY = []
constraintsCZ = []
final_constrinCX = []
final_constrinCY = []
final_constrinCZ = []
n_baseC=8

for i in range(0, len(final_baseC),n_baseC):
    a = (final_baseC[i][0] + final_baseC[i+1][0] + final_baseC[i+2][0] + final_baseC[i+3][0] + final_baseC[i+4][0] + final_baseC[i+5][0] + final_baseC[i+6][0] + final_baseC[i+7][0])/n_baseC
    ca = a - final_baseC[i][0]
    constraintsCX.append(round(ca,2))
    cb = a - final_baseC[i+1][0]
    constraintsCX.append(round(cb,2))
    cc = a - final_baseC[i+2][0]
    constraintsCX.append(round(cc,2))
    cd = a - final_baseC[i+3][0]
    constraintsCX.append(round(cd,2))
    ce = a - final_baseC[i+4][0]
    constraintsCX.append(round(ce,2))
    cf = a - final_baseC[i+5][0]
    constraintsCX.append(round(cf,2))
    cg = a - final_baseC[i+6][0]
    constraintsCX.append(round(cg,2))
    ch = a - final_baseC[i+7][0]
    constraintsCX.append(round(ch,2))
    final_constrinCX.append(constraintsCX)
    constraintsCX = []
    baseC_cg.append(round(a,3))
       
    b = (final_baseC[i][1] + final_baseC[i+1][1] + final_baseC[i+2][1] + final_baseC[i+3][1] + final_baseC[i+4][1] + final_baseC[i+5][1] + final_baseC[i+6][1] + final_baseC[i+7][1])/n_baseC
    ca = b - final_baseC[i][1]
    constraintsCY.append(round(ca,2))
    cb = b - final_baseC[i+1][1]
    constraintsCY.append(round(cb,2))
    cc = b - final_baseC[i+2][1]
    constraintsCY.append(round(cc,2))
    cd = b - final_baseC[i+3][1]
    constraintsCY.append(round(cd,2))
    ce = b - final_baseC[i+4][1]
    constraintsCY.append(round(ce,2))
    cf = b - final_baseC[i+5][1]
    constraintsCY.append(round(cf,2))
    cg = b - final_baseC[i+6][1]
    constraintsCY.append(round(cg,2))
    ch = b - final_baseC[i+7][1]
    constraintsCY.append(round(ch,2))
    final_constrinCY.append(constraintsCY)
    constraintsCY = []
    baseC_cg.append(round(b,3))
    
    c = (final_baseC[i][2] + final_baseC[i+1][2] + final_baseC[i+2][2] + final_baseC[i+3][2] + final_baseC[i+4][2] + final_baseC[i+5][2] + final_baseC[i+6][2] + final_baseC[i+7][2])/n_baseC
    ca = c - final_baseC[i][2]
    constraintsCZ.append(round(ca,2))
    cb = c - final_baseC[i+1][2]
    constraintsCZ.append(round(cb,2))
    cc = c - final_baseC[i+2][2]
    constraintsCZ.append(round(cc,2))
    cd = c - final_baseC[i+3][2]
    constraintsCZ.append(round(cd,2))
    ce = c - final_baseC[i+4][2]
    constraintsCZ.append(round(ce,2))
    cf = c - final_baseC[i+5][2]
    constraintsCZ.append(round(cf,2))
    cg = c - final_baseC[i+6][2]
    constraintsCZ.append(round(cg,2))
    ch = c - final_baseC[i+7][2]
    constraintsCZ.append(round(ch,2))
    final_constrinCZ.append(constraintsCZ)
    constraintsCZ = []
    baseC_cg.append(round(c,3))
    
    final_baseC_cg.append(baseC_cg)
    baseC_cg = []
    

final_baseC= np.array(final_baseC)
final_baseC_cg = np.array(final_baseC_cg)
final_baseC = np.reshape(final_baseC,(len(final_baseC_cg), 3*n_baseC))

final_constrinCX = pd.DataFrame(final_constrinCX)
final_constrinCY = pd.DataFrame(final_constrinCY)
final_constrinCZ = pd.DataFrame(final_constrinCZ)

final_constrinCX_sq = final_constrinCX**2
final_constrinCY_sq = final_constrinCY**2
final_constrinCZ_sq = final_constrinCZ**2

R = final_constrinCX_sq + final_constrinCY_sq + final_constrinCZ_sq

Rsqrt = np.sqrt(R)
Rsqrt = round(Rsqrt,3)

dist1 = np.mean(Rsqrt)[0]
dist2 = np.mean(Rsqrt)[1]
dist3 = np.mean(Rsqrt)[2]
dist4 = np.mean(Rsqrt)[3]
dist5 = np.mean(Rsqrt)[4]
dist6 = np.mean(Rsqrt)[5]
dist7 = np.mean(Rsqrt)[6]
dist8 = np.mean(Rsqrt)[7]

#print(Rsqrt)
#print(dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8)
