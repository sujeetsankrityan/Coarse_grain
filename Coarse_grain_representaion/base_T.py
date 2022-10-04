import numpy as np
import pandas as pd

file1 = []
baseT = []
final_baseT = []
with open("test.pdb") as file:
    for line in file:
        if (line[0:4] == "ATOM"):
            a = line.split()
            file1.append(a)
            
    
for line in file1:
    if(line[3] == "DT" and (line[2] == "N1" or line[2]=="C2" or line[2] =="O2" or line[2]=="N3" or line[2]=="C4" or line[2]=="O4" or line[2]=="C5" or line[2]=="C5M" or line[2]=="C6")):
        baseT.append(float(line[6]))
        baseT.append(float(line[7]))
        baseT.append(float(line[8]))
        final_baseT.append(baseT)
        baseT = []
    
baseT_cg = []
final_baseT_cg = []
constraintsTX = []
constraintsTY = []
constraintsTZ = []
final_constrinTX = []
final_constrinTY = []
final_constrinTZ = []
n_baseT=8

for i in range(0, len(final_baseT),n_baseT):
    a = (final_baseT[i][0] + final_baseT[i+1][0] + final_baseT[i+2][0] + final_baseT[i+3][0] + final_baseT[i+4][0] + final_baseT[i+5][0] + final_baseT[i+6][0] + final_baseT[i+7][0])/n_baseT
    ca = a - final_baseT[i][0]
    constraintsTX.append(round(ca,2))
    cb = a - final_baseT[i+1][0]
    constraintsTX.append(round(cb,2))
    cc = a - final_baseT[i+2][0]
    constraintsTX.append(round(cc,2))
    cd = a - final_baseT[i+3][0]
    constraintsTX.append(round(cd,2))
    ce = a - final_baseT[i+4][0]
    constraintsTX.append(round(ce,2))
    cf = a - final_baseT[i+5][0]
    constraintsTX.append(round(cf,2))
    cg = a - final_baseT[i+6][0]
    constraintsTX.append(round(cg,2))
    ch = a - final_baseT[i+7][0]
    constraintsTX.append(round(ch,2))
    final_constrinTX.append(constraintsTX)
    constraintsTX = []
    baseT_cg.append(round(a,3))

    b = (final_baseT[i][1] + final_baseT[i+1][1] + final_baseT[i+2][1] + final_baseT[i+3][1] + final_baseT[i+4][1] + final_baseT[i+5][1] + final_baseT[i+6][1] + final_baseT[i+7][1])/n_baseT
    ca = b - final_baseT[i][1]
    constraintsTY.append(round(ca,2))
    cb = b - final_baseT[i+1][1]
    constraintsTY.append(round(cb,2))
    cc = b - final_baseT[i+2][1]
    constraintsTY.append(round(cc,2))
    cd = b - final_baseT[i+3][1]
    constraintsTY.append(round(cd,2))
    ce = b - final_baseT[i+4][1]
    constraintsTY.append(round(ce,2))
    cf = b - final_baseT[i+5][1]
    constraintsTY.append(round(cf,2))
    cg = b - final_baseT[i+6][1]
    constraintsTY.append(round(cg,2))
    ch = b - final_baseT[i+7][1]
    constraintsTY.append(round(ch,2))
    final_constrinTY.append(constraintsTY)
    constraintsTY = []
    baseT_cg.append(round(b,3))
    
    c = (final_baseT[i][2] + final_baseT[i+1][2] + final_baseT[i+2][2] + final_baseT[i+3][2] + final_baseT[i+4][2] + final_baseT[i+5][2] + final_baseT[i+6][2] + final_baseT[i+7][2])/n_baseT
    ca = c - final_baseT[i][2]
    constraintsTZ.append(round(ca,2))
    cb = c - final_baseT[i+1][2]
    constraintsTZ.append(round(cb,2))
    cc = c - final_baseT[i+2][2]
    constraintsTZ.append(round(cc,2))
    cd = c - final_baseT[i+3][2]
    constraintsTZ.append(round(cd,2))
    ce = c - final_baseT[i+4][2]
    constraintsTZ.append(round(ce,2))
    cf = c - final_baseT[i+5][2]
    constraintsTZ.append(round(cf,2))
    cg = c - final_baseT[i+6][2]
    constraintsTZ.append(round(cg,2))
    ch = c - final_baseT[i+7][2]
    constraintsTZ.append(round(ch,2))
    final_constrinTZ.append(constraintsTZ)
    constraintsTZ = []
    baseT_cg.append(round(c,3))
    
    final_baseT_cg.append(baseT_cg)
    baseT_cg = []
    
    
final_baseT = np.array(final_baseT)
final_baseT_cg = np.array(final_baseT_cg)
final_baseT = np.reshape(final_baseT, (len(final_baseT_cg), 3*n_baseT))
final_constrinTX = pd.DataFrame(final_constrinTX)
final_constrinTY = pd.DataFrame(final_constrinTY)
final_constrinTZ = pd.DataFrame(final_constrinTZ)

final_constrinTX_sq = final_constrinTX**2
final_constrinTY_sq = final_constrinTY**2
final_constrinTZ_sq = final_constrinTZ**2

R = final_constrinTX_sq + final_constrinTY_sq + final_constrinTZ_sq

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

print(Rsqrt)
print(dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8)
