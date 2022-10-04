import numpy as np
import pandas as pd

file1 = []
baseG = []
final_baseG = []
with open("test.pdb") as file:
    for line in file:
        if (line[0:4] == "ATOM"):
            a = line.split()
            file1.append(a)
            
    
for line in file1:
    if(line[3] == "DG" and (line[2]=="N1" or line[2]=="C2" or line[2]=="N2" or line[2]=="N3" or line[2]=="C4" or line[2]=="C5" or line[2]=="C6" or line[2]=="O6" or line[2]=="N7" or line[2]=="C8" or line[2]=="N9")):
        baseG.append(float(line[6]))
        baseG.append(float(line[7]))
        baseG.append(float(line[8]))
        final_baseG.append(baseG)
        baseG = []

baseG_cg = []
final_baseG_cg = []
constraintsGX = []
constraintsGY = []
constraintsGZ = []
final_constrinGX = []
final_constrinGY = []
final_constrinGZ = []
n_baseG=11

for i in range(0, len(final_baseG),n_baseG):
    a = (final_baseG[i][0] + final_baseG[i+1][0] + final_baseG[i+2][0] + final_baseG[i+3][0] + final_baseG[i+4][0] + final_baseG[i+5][0] + final_baseG[i+6][0] + final_baseG[i+7][0] + final_baseG[i+8][0] + final_baseG[i+9][0] + final_baseG[i+10][0])/n_baseG
    ca = a - final_baseG[i][0]
    constraintsGX.append(round(ca,2))
    cb = a - final_baseG[i+1][0]
    constraintsGX.append(round(cb,2))
    cc = a - final_baseG[i+2][0]
    constraintsGX.append(round(cc,2))
    cd = a - final_baseG[i+3][0]
    constraintsGX.append(round(cd,2))
    ce = a - final_baseG[i+4][0]
    constraintsGX.append(round(ce,2))
    cf = a - final_baseG[i+5][0]
    constraintsGX.append(round(cf,2))
    cg = a - final_baseG[i+6][0]
    constraintsGX.append(round(cg,2))
    ch = a - final_baseG[i+7][0]
    constraintsGX.append(round(ch,2))
    ci = a - final_baseG[i+8][0]
    constraintsGX.append(round(ci,2))
    cj = a - final_baseG[i+9][0]
    constraintsGX.append(round(cj,2))
    ck = a - final_baseG[i+10][0]
    constraintsGX.append(round(ck,2))
    final_constrinGX.append(constraintsGX)
    constraintsGX = []
    baseG_cg.append(round(a,3))
       
    b = (final_baseG[i][1] + final_baseG[i+1][1] + final_baseG[i+2][1] + final_baseG[i+3][1] + final_baseG[i+4][1] + final_baseG[i+5][1] + final_baseG[i+6][1] + final_baseG[i+7][1] + final_baseG[i+8][1] + final_baseG[i+9][1] + final_baseG[i+10][1])/n_baseG
    ca = b - final_baseG[i][1]
    constraintsGY.append(round(ca,2))
    cb = b - final_baseG[i+1][1]
    constraintsGY.append(round(cb,2))
    cc = b - final_baseG[i+2][1]
    constraintsGY.append(round(cc,2))
    cd = b - final_baseG[i+3][1]
    constraintsGY.append(round(cd,2))
    ce = b - final_baseG[i+4][1]
    constraintsGY.append(round(ce,2))
    cf = b - final_baseG[i+5][1]
    constraintsGY.append(round(cf,2))
    cg = b - final_baseG[i+6][1]
    constraintsGY.append(round(cg,2))
    ch = b - final_baseG[i+7][1]
    constraintsGY.append(round(ch,2))
    ci = b - final_baseG[i+8][1]
    constraintsGY.append(round(ci,2))
    cj = b - final_baseG[i+9][1]
    constraintsGY.append(round(cj,2))
    ck = b - final_baseG[i+10][1]
    constraintsGY.append(round(ck,2))
    final_constrinGY.append(constraintsGY)
    constraintsGY = []
    baseG_cg.append(round(b,3))
    
    c = (final_baseG[i][2] + final_baseG[i+1][2] + final_baseG[i+2][2] + final_baseG[i+3][2] + final_baseG[i+4][2] + final_baseG[i+5][2] + final_baseG[i+6][2] + final_baseG[i+7][2]  + final_baseG[i+8][2] + final_baseG[i+9][2] + final_baseG[i+10][2])/n_baseG
    ca = c - final_baseG[i][2]
    constraintsGZ.append(round(ca,2))
    cb = c - final_baseG[i+1][2]
    constraintsGZ.append(round(cb,2))
    cc = c - final_baseG[i+2][2]
    constraintsGZ.append(round(cc,2))
    cd = c - final_baseG[i+3][2]
    constraintsGZ.append(round(cd,2))
    ce = c - final_baseG[i+4][2]
    constraintsGZ.append(round(ce,2))
    cf = c - final_baseG[i+5][2]
    constraintsGZ.append(round(cf,2))
    cg = c - final_baseG[i+6][2]
    constraintsGZ.append(round(cg,2))
    ch = c - final_baseG[i+7][2]
    constraintsGZ.append(round(ch,2))
    ci = c - final_baseG[i+8][2]
    constraintsGZ.append(round(ci,2))
    cj = c - final_baseG[i+9][2]
    constraintsGZ.append(round(cj,2))
    ck = c - final_baseG[i+10][2]
    constraintsGZ.append(round(ck,2))
    final_constrinGZ.append(constraintsGZ)
    constraintsGZ = []
    baseG_cg.append(round(c,3))
    
    final_baseG_cg.append(baseG_cg)
    baseG_cg = []
    

final_baseG = np.array(final_baseG)
final_baseG_cg = np.array(final_baseG_cg)
final_baseG = np.reshape(final_baseG, (len(final_baseG_cg), 3*n_baseG))

final_constrinGX = pd.DataFrame(final_constrinGX)
final_constrinGY = pd.DataFrame(final_constrinGY)
final_constrinGZ = pd.DataFrame(final_constrinGZ)

final_constrinGX_sq = final_constrinGX**2
final_constrinGY_sq = final_constrinGY**2
final_constrinGZ_sq = final_constrinGZ**2

R = final_constrinGX_sq + final_constrinGY_sq + final_constrinGZ_sq

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
dist9 = np.mean(Rsqrt)[8]
dist10 = np.mean(Rsqrt)[9]
dist11 = np.mean(Rsqrt)[10]

#print(Rsqrt)
#print(dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10,dist11)
