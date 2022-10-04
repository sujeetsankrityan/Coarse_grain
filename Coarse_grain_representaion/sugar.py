import numpy as np
import pandas as pd

file1 = []
carbon = []
final_carbon = []
with open("test.pdb") as file:
    for line in file:
        if (line[0:4] == "ATOM"):
            a = line.split()
            file1.append(a)

for line in file1:
    if(line[2] == "C2'"  or line[2] == "C4'" or line[2] == "O4'" or line[2] == "C3'" or line[2] == "C5'" or line[2] == "C1'"):
        carbon.append(float(line[6]))
        carbon.append(float(line[7]))
        carbon.append(float(line[8]))
        final_carbon.append(carbon)
        carbon = []

carbon_cg = []
final_carbon_cg = []
constraintsCX = []
constraintsCY = []
constraintsCZ = []
final_constrinCX = []
final_constrinCY = []
final_constrinCZ = []
n_carbon=6

for i in range(0, len(final_carbon),n_carbon):
    a = (final_carbon[i][0] + final_carbon[i+1][0] + final_carbon[i+2][0] + final_carbon[i+3][0] + final_carbon[i+4][0] + final_carbon[i+5][0])/n_carbon
    ca = a - final_carbon[i][0]
    constraintsCX.append(round(ca,2))
    cb = a - final_carbon[i+1][0]
    constraintsCX.append(round(cb,2))
    cc = a - final_carbon[i+2][0]
    constraintsCX.append(round(cc,2))
    cd = a - final_carbon[i+3][0]
    constraintsCX.append(round(cd,2))
    ce = a - final_carbon[i+4][0]
    constraintsCX.append(round(ce,2))
    cf = a - final_carbon[i+5][0]
    constraintsCX.append(round(cf,2))
    final_constrinCX.append(constraintsCX)
    constraintsCX = []
    carbon_cg.append(round(a,3))
    
    b = (final_carbon[i][1] + final_carbon[i+1][1] + final_carbon[i+2][1] + final_carbon[i+3][1] + final_carbon[i+4][1] + final_carbon[i+5][1])/n_carbon
    ca = b - final_carbon[i][1]
    constraintsCY.append(round(ca,2))
    cb = b - final_carbon[i+1][1]
    constraintsCY.append(round(cb,2))
    cc = b - final_carbon[i+2][1]
    constraintsCY.append(round(cc,2))
    cd = b - final_carbon[i+3][1]
    constraintsCY.append(round(cd,2))
    ce = b - final_carbon[i+4][1]
    constraintsCY.append(round(ce,2))
    cf = b - final_carbon[i+5][1]
    constraintsCY.append(round(cf,2))
    final_constrinCY.append(constraintsCY)
    constraintsCY = []
    carbon_cg.append(round(b,3))
    
    c = (final_carbon[i][2] + final_carbon[i+1][2] + final_carbon[i+2][2] + final_carbon[i+3][2] + final_carbon[i+4][2] + final_carbon[i+5][2])/n_carbon
    ca = c - final_carbon[i][2]
    constraintsCZ.append(round(ca,2))
    cb = c - final_carbon[i+1][2]
    constraintsCZ.append(round(cb,2))
    cc = c - final_carbon[i+2][2]
    constraintsCZ.append(round(cc,2))
    cd = c - final_carbon[i+3][2]
    constraintsCZ.append(round(cd,2))
    ce = c - final_carbon[i+4][2]
    constraintsCZ.append(round(ce,2))
    cf = c - final_carbon[i+5][2]
    constraintsCZ.append(round(cf,2))
    final_constrinCZ.append(constraintsCZ)
    constraintsCZ = []
    carbon_cg.append(round(c,3))
    
    final_carbon_cg.append(carbon_cg)
    carbon_cg=[]

final_carbon = np.array(final_carbon)
final_carbon_cg = np.array(final_carbon_cg)
final_carbon = np.reshape(final_carbon, (len(final_carbon_cg),3*n_carbon))

final_constrinCX = pd.DataFrame(final_constrinCX)
final_constrinCY = pd.DataFrame(final_constrinCY)
final_constrinCZ = pd.DataFrame(final_constrinCZ)
final_constrinCX_sq = final_constrinCX**2
final_constrinCY_sq = final_constrinCY**2
final_constrinCZ_sq = final_constrinCZ**2

R = final_constrinCX_sq + final_constrinCY_sq + final_constrinCZ_sq
Rsqrt = np.sqrt(R)
Rsqrt = round(Rsqrt,3)
dist_s1 = np.mean(Rsqrt)[0]
dist_s2 = np.mean(Rsqrt)[1]
dist_s3 = np.mean(Rsqrt)[2]
dist_s4 = np.mean(Rsqrt)[3]
dist_s5 = np.mean(Rsqrt)[4]
dist_s6 = np.mean(Rsqrt)[5]
