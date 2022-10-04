file1 = []
phos = []
final_phos = []

import numpy as np
import pandas as pd
with open("test.pdb") as file:
    for line in file:
        if (line[0:4] == "ATOM"):
            a = line.split()
            file1.append(a)

for line in file1:
    if(line[5] != "1" and line[5] != "56"):
        if(line[2] == "P" or line[2] == "O5'" or line[2] == "OP1" or line[2] == "OP2" or line[2] == "O1P" or line[2] == "O2P"):
            phos.append(float(line[6]))
            phos.append(float(line[7]))
            phos.append(float(line[8]))
            final_phos.append(phos)
            phos = []

phos_cg = []
final_phos_cg = []
constraintsX = []
constraintsY = []
constraintsZ = []
final_constrinX = []
final_constrinY = []
final_constrinZ = []
n_phos=4


for i in range(0, len(final_phos),n_phos):
    a = (final_phos[i][0] + final_phos[i+1][0] + final_phos[i+2][0] + final_phos[i+3][0])/n_phos
    ca = a - final_phos[i][0]
    constraintsX.append(round(ca,2))
    cb = a - final_phos[i+1][0]
    constraintsX.append(round(cb,2))
    cc = a - final_phos[i+2][0]
    constraintsX.append(round(cc,2))
    cd = a - final_phos[i+3][0]
    constraintsX.append(round(cd,2))
    final_constrinX.append(constraintsX)
    constraintsX = []
    phos_cg.append(round(a,2))
    
    b = (final_phos[i][1] + final_phos[i+1][1] + final_phos[i+2][1] + final_phos[i+3][1])/n_phos
    ca = b - final_phos[i][1]
    constraintsY.append(round(ca,2))
    cb = b - final_phos[i+1][1]
    constraintsY.append(round(cb,2))
    cc = b - final_phos[i+2][1]
    constraintsY.append(round(cc,2))
    cd = b - final_phos[i+3][1]
    constraintsY.append(round(cd,2))
    final_constrinY.append(constraintsY)
    constraintsY = []
    phos_cg.append(round(b,2))
    
    c = (final_phos[i][2] + final_phos[i+1][2] + final_phos[i+2][2] + final_phos[i+3][2])/n_phos
    ca = c - final_phos[i][2]
    constraintsZ.append(round(ca,2))
    cb = c - final_phos[i+1][2]
    constraintsZ.append(round(cb,2))
    cc = c - final_phos[i+2][2]
    constraintsZ.append(round(cc,2))
    cd = c - final_phos[i+3][2]
    constraintsZ.append(round(cd,2))
    final_constrinZ.append(constraintsZ)
    constraintsZ = []    
    phos_cg.append(round(c,3))
    
    final_phos_cg.append(phos_cg)
    phos_cg = []

final_phos = np.array(final_phos)
final_phos_cg = np.array(final_phos_cg)
final_phos = np.reshape(final_phos, (len(final_phos_cg), 3*n_phos))

final_constrinX = pd.DataFrame(final_constrinX)
final_constrinY = pd.DataFrame(final_constrinY)
final_constrinZ = pd.DataFrame(final_constrinZ)

final_constrinX_sq = final_constrinX**2
final_constrinY_sq = final_constrinY**2
final_constrinZ_sq = final_constrinZ**2

R = final_constrinX_sq + final_constrinY_sq + final_constrinZ_sq

Rsqrt = np.sqrt(R)
Rsqrt = round(Rsqrt,3)

dist1 = np.mean(Rsqrt)[0]
dist2 = np.mean(Rsqrt)[1]
dist3 = np.mean(Rsqrt)[2]
dist4 = np.mean(Rsqrt)[3]

#### Rsqrt is the distance of each phosphate atoms from centre of mass      ####
#### dist are the average distance of 4 phosphorus atom from centre of mass ####
