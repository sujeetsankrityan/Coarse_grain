import numpy as np
import pandas as pd

file1 = []
baseA = []
final_baseA = []
with open("test.pdb") as file:
    for line in file:
        if (line[0:4] == "ATOM"):
            a = line.split()
            file1.append(a)
            
for line in file1:
    if(line[3] == "DA" and (line[2] == "N1" or line[2] =="C2" or line[2] =="N3" or line[2] =="C4" or line[2] =="C5" or line[2]=="C6" or line[2] =="N6" or line[2] =="N7" or line[2] =="C8" or line[2] =="N9")):
        baseA.append(float(line[6]))
        baseA.append(float(line[7]))
        baseA.append(float(line[8]))
        final_baseA.append(baseA)
        baseA = []

baseA_cg = []
final_baseA_cg = []
constraintsAX = []
constraintsAY = []
constraintsAZ = []
final_constrinAX = []
final_constrinAY = []
final_constrinAZ = []
n_baseA = 10

for i in range(0, len(final_baseA),n_baseA):
    a = (final_baseA[i][0] + final_baseA[i+1][0] + final_baseA[i+2][0] + final_baseA[i+3][0] + final_baseA[i+4][0] + final_baseA[i+5][0] + final_baseA[i+6][0] + final_baseA[i+7][0] + final_baseA[i+8][0] + final_baseA[i+9][0])/n_baseA
    ca = a - final_baseA[i][0]
    constraintsAX.append(round(ca,2))
    cb = a - final_baseA[i+1][0]
    constraintsAX.append(round(cb,2))
    cc = a - final_baseA[i+2][0]
    constraintsAX.append(round(cc,2))
    cd = a - final_baseA[i+3][0]
    constraintsAX.append(round(cd,2))
    ce = a - final_baseA[i+4][0]
    constraintsAX.append(round(ce,2))
    cf = a - final_baseA[i+5][0]
    constraintsAX.append(round(cf,2))
    cg = a - final_baseA[i+6][0]
    constraintsAX.append(round(cg,2))
    ch = a - final_baseA[i+7][0]
    constraintsAX.append(round(ch,2))
    ci = a - final_baseA[i+8][0]
    constraintsAX.append(round(ci,2))
    cj = a - final_baseA[i+9][0]
    constraintsAX.append(round(cj,2))
    final_constrinAX.append(constraintsAX)
    constraintsAX = []
    baseA_cg.append(round(a,3))

    b = (final_baseA[i][1] + final_baseA[i+1][1] + final_baseA[i+2][1] + final_baseA[i+3][1] + final_baseA[i+4][1] + final_baseA[i+5][1] + final_baseA[i+6][1] + final_baseA[i+7][1] + final_baseA[i+8][1] + final_baseA[i+9][1])/n_baseA
    ca = b - final_baseA[i][1]
    constraintsAY.append(round(ca,2))
    cb = b - final_baseA[i+1][1]
    constraintsAY.append(round(cb,2))
    cc = b - final_baseA[i+2][1]
    constraintsAY.append(round(cc,2))
    cd = b - final_baseA[i+3][1]
    constraintsAY.append(round(cd,2))
    ce = b - final_baseA[i+4][1]
    constraintsAY.append(round(ce,2))
    cf = b - final_baseA[i+5][1]
    constraintsAY.append(round(cf,2))
    cg = b - final_baseA[i+6][1]
    constraintsAY.append(round(cg,2))
    ch = b - final_baseA[i+7][1]
    constraintsAY.append(round(ch,2))
    ci = b - final_baseA[i+8][1]
    constraintsAY.append(round(ci,2))
    cj = b - final_baseA[i+9][1]
    constraintsAY.append(round(cj,2))
    final_constrinAY.append(constraintsAY)
    constraintsAY = []
    baseA_cg.append(round(b,3))

    
    c = (final_baseA[i][2] + final_baseA[i+1][2] + final_baseA[i+2][2] + final_baseA[i+3][2] + final_baseA[i+4][2] + final_baseA[i+5][2] + final_baseA[i+6][2] + final_baseA[i+7][2] + final_baseA[i+8][2] + final_baseA[i+9][2])/n_baseA
    ca = c - final_baseA[i][2]
    constraintsAZ.append(round(ca,2))
    cb = c - final_baseA[i+1][2]
    constraintsAZ.append(round(cb,2))
    cc = c - final_baseA[i+2][2]
    constraintsAZ.append(round(cc,2))
    cd = c - final_baseA[i+3][2]
    constraintsAZ.append(round(cd,2))
    ce = c - final_baseA[i+4][2]
    constraintsAZ.append(round(ce,2))
    cf = c - final_baseA[i+5][2]
    constraintsAZ.append(round(cf,2))
    cg = c - final_baseA[i+6][2]
    constraintsAZ.append(round(cg,2))
    ch = c - final_baseA[i+7][2]
    constraintsAZ.append(round(ch,2))
    ci = c - final_baseA[i+8][2]
    constraintsAZ.append(round(ci,2))
    cj = c - final_baseA[i+9][2]
    constraintsAZ.append(round(cj,2))
    final_constrinAZ.append(constraintsAZ)
    constraintsAZ = []
    baseA_cg.append(round(c,3))
    
    final_baseA_cg.append(baseA_cg)
    baseA_cg = []
    
final_baseA = np.array(final_baseA)
final_baseA_cg = np.array(final_baseA_cg)
final_baseA = np.reshape(final_baseA, (len(final_baseA_cg), 3*n_baseA))

final_constrinAX = pd.DataFrame(final_constrinAX)
final_constrinAY = pd.DataFrame(final_constrinAY)
final_constrinAZ = pd.DataFrame(final_constrinAZ)

final_constrinAX_sq = final_constrinAX**2
final_constrinAY_sq = final_constrinAY**2
final_constrinAZ_sq = final_constrinAZ**2

R = final_constrinAX_sq + final_constrinAY_sq + final_constrinAZ_sq

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

#print(Rsqrt)
#print(dist1,dist2,dist3,dist4,dist5,dist6,dist7,dist8,dist9,dist10)
