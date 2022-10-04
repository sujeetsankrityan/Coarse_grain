import numpy as np
import pandas as pd
file1 = []
phos = []
sugar = []
baseA = []
baseT = []
baseG = []
baseC = []
final_phos = []
final_sugar = []
final_baseA = []
final_baseT = []
final_baseG = []
final_baseC = []

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
        
    if(line[2] == "C2'"  or line[2] == "C4'" or line[2] == "O4'" or line[2] == "C3'" or line[2] == "C5'" or line[2] == "C1'"):
        sugar.append(float(line[6]))
        sugar.append(float(line[7]))
        sugar.append(float(line[8]))
        final_sugar.append(sugar)
        sugar = []
        
    if(line[3] == "DA" and (line[2] == "N1" or line[2] =="C2" or line[2] =="N3" or line[2] =="C4" or line[2] =="C5" or line[2]=="C6" or line[2] =="N6" or line[2] =="N7" or line[2] =="C8" or line[2] =="N9")):
        baseA.append(float(line[6]))
        baseA.append(float(line[7]))
        baseA.append(float(line[8]))
        final_baseA.append(baseA)
        baseA = []
        
    if(line[3] == "DT" and (line[2] == "N1" or line[2]=="C2" or line[2] =="O2" or line[2]=="N3" or line[2]=="C4" or line[2]=="O4" or line[2]=="C5" or line[2]=="C5M" or line[2]=="C6")):
        baseT.append(float(line[6]))
        baseT.append(float(line[7]))
        baseT.append(float(line[8]))
        final_baseT.append(baseT)
        baseT = []
    
    if(line[3] == "DG" and (line[2]=="N1" or line[2]=="C2" or line[2]=="N2" or line[2]=="N3" or line[2]=="C4" or line[2]=="C5" or line[2]=="C6" or line[2]=="O6" or line[2]=="N7" or line[2]=="C8" or line[2]=="N9")):
        baseG.append(float(line[6]))
        baseG.append(float(line[7]))
        baseG.append(float(line[8]))
        final_baseG.append(baseG)
        baseG = []
        
    if(line[3]=="DC" and (line[2]=="N1" or line[2]=="C2" or line[2]=="O2" or line[2]=="N3" or line[2]=="C4" or line[2]=="N4" or line[2]=="C5" or line[2]=="C6")):
        baseC.append(float(line[6]))
        baseC.append(float(line[7]))
        baseC.append(float(line[8]))
        final_baseC.append(baseC)
        baseC = []


phos_cg = [];sugar_cg = [];baseA_cg = [];baseT_cg = [];baseG_cg = [];baseC_cg = []
final_phos_cg = [];final_sugar_cg = [];final_baseA_cg = [];final_baseT_cg = [];final_baseG_cg = [];final_baseC_cg = []
constraintsPX = [];constraintsSX = [];constraintsAX = [];constraintsTX = [];constraintsGX = [];constraintsCX = []
constraintsPY = [];constraintsSY = [];constraintsAY = [];constraintsTY = [];constraintsGY = [];constraintsCY = []
constraintsPZ = [];constraintsSZ = [];constraintsAZ = [];constraintsTZ = [];constraintsGZ = [];constraintsCZ = []
final_constrinPX = [];final_constrinSX = [];final_constrinAX = [];final_constrinTX = [];final_constrinGX = [];final_constrinCX = [];
final_constrinPY = [];final_constrinSY = [];final_constrinAY = [];final_constrinTY = [];final_constrinGY = [];final_constrinCY = [];
final_constrinPZ = [];final_constrinSZ = [];final_constrinAZ = [];final_constrinTZ = [];final_constrinGZ = [];final_constrinCZ = [];
n_phos=4;n_sugar=6;n_baseA = 10;n_baseT=8;n_baseG=11;n_baseC=8


for i in range(0, len(final_phos),n_phos):
    a=0;b=0;c=0
    for j in range(n_phos):
        a+= final_phos[i+j][0]
        b+= final_phos[i+j][1]
        c+= final_phos[i+j][2]
    a = a/n_phos; b = b/n_phos; c = c/n_phos
    for j in range(n_phos):
        ra = a - final_phos[i+j][0]
        rb = b - final_phos[i+j][1]
        rc = c - final_phos[i+j][2]
        constraintsPX.append(ra)
        constraintsPY.append(rb)
        constraintsPZ.append(rc)
    final_constrinPX.append(constraintsPX)
    final_constrinPY.append(constraintsPY)
    final_constrinPZ.append(constraintsPZ)
    constraintsPX = []; constraintsPY = []; constraintsPZ = []
    phos_cg.append(a); phos_cg.append(b); phos_cg.append(c)
    final_phos_cg.append(phos_cg)
    phos_cg = []

for i in range(0, len(final_sugar),n_sugar):
    a=0;b=0;c=0
    for j in range(n_sugar):
        a+= final_sugar[i+j][0]
        b+= final_sugar[i+j][1]
        c+= final_sugar[i+j][2]
    a = a/n_sugar; b = b/n_sugar; c = c/n_sugar
    for j in range(n_sugar):
        ra = a - final_sugar[i+j][0]
        rb = b - final_sugar[i+j][1]
        rc = c - final_sugar[i+j][2]
        constraintsSX.append(ra)
        constraintsSY.append(rb)
        constraintsSZ.append(rc)
    final_constrinSX.append(constraintsSX)
    final_constrinSY.append(constraintsSY)
    final_constrinSZ.append(constraintsSZ)
    constraintsSX = []; constraintsSY = []; constraintsSZ = []
    sugar_cg.append(a); sugar_cg.append(b); sugar_cg.append(c)
    final_sugar_cg.append(sugar_cg)
    sugar_cg = []

for i in range(0, len(final_baseA),n_baseA):
    a=0;b=0;c=0
    for j in range(n_baseA):
        a+= final_baseA[i+j][0]
        b+= final_baseA[i+j][1]
        c+= final_baseA[i+j][2]
    a = a/n_baseA; b = b/n_baseA; c = c/n_baseA
    for j in range(n_baseA):
        ra = a - final_baseA[i+j][0]
        rb = b - final_baseA[i+j][1]
        rc = c - final_baseA[i+j][2]
        constraintsAX.append(ra)
        constraintsAY.append(rb)
        constraintsAZ.append(rc)
    final_constrinAX.append(constraintsAX)
    final_constrinAY.append(constraintsAY)
    final_constrinAZ.append(constraintsAZ)
    constraintsAX = []; constraintsAY = []; constraintsAZ = []
    baseA_cg.append(a); baseA_cg.append(b); baseA_cg.append(c)
    final_baseA_cg.append(baseA_cg)
    baseA_cg = []

for i in range(0, len(final_baseT),n_baseT):
    a=0;b=0;c=0
    for j in range(n_baseT):
        a+= final_baseT[i+j][0]
        b+= final_baseT[i+j][1]
        c+= final_baseT[i+j][2]
    a = a/n_baseT; b = b/n_baseT; c = c/n_baseT
    for j in range(n_baseT):
        ra = a - final_baseT[i+j][0]
        rb = b - final_baseT[i+j][1]
        rc = c - final_baseT[i+j][2]
        constraintsTX.append(ra)
        constraintsTY.append(rb)
        constraintsTZ.append(rc)
    final_constrinTX.append(constraintsTX)
    final_constrinTY.append(constraintsTY)
    final_constrinTZ.append(constraintsTZ)
    constraintsTX = []; constraintsTY = []; constraintsTZ = []
    baseT_cg.append(a); baseT_cg.append(b); baseT_cg.append(c)
    final_baseT_cg.append(baseT_cg)
    baseT_cg = []

for i in range(0, len(final_baseG),n_baseG):
    a=0;b=0;c=0
    for j in range(n_baseG):
        a+= final_baseG[i+j][0]
        b+= final_baseG[i+j][1]
        c+= final_baseG[i+j][2]
    a = a/n_baseG; b = b/n_baseG; c = c/n_baseG
    for j in range(n_baseG):
        ra = a - final_baseG[i+j][0]
        rb = b - final_baseG[i+j][1]
        rc = c - final_baseG[i+j][2]
        constraintsGX.append(ra)
        constraintsGY.append(rb)
        constraintsGZ.append(rc)
    final_constrinGX.append(constraintsGX)
    final_constrinGY.append(constraintsGY)
    final_constrinGZ.append(constraintsGZ)
    constraintsGX = []; constraintsGY = []; constraintsGZ = []
    baseG_cg.append(a); baseG_cg.append(b); baseG_cg.append(c)
    final_baseG_cg.append(baseG_cg)
    baseG_cg = []

for i in range(0, len(final_baseC),n_baseC):
    a=0;b=0;c=0
    for j in range(n_baseC):
        a+= final_baseC[i+j][0]
        b+= final_baseC[i+j][1]
        c+= final_baseC[i+j][2]
    a = a/n_baseC; b = b/n_baseC; c = c/n_baseC
    for j in range(n_baseC):
        ra = a - final_baseC[i+j][0]
        rb = b - final_baseC[i+j][1]
        rc = c - final_baseC[i+j][2]
        constraintsCX.append(ra)
        constraintsCY.append(rb)
        constraintsCZ.append(rc)
    final_constrinCX.append(constraintsCX)
    final_constrinCY.append(constraintsCY)
    final_constrinCZ.append(constraintsCZ)
    constraintsCX = []; constraintsCY = []; constraintsCZ = []
    baseC_cg.append(a); baseC_cg.append(b); baseC_cg.append(c)
    final_baseC_cg.append(baseC_cg)
    baseC_cg = []

########## Calculation for Phosphorus  ####################
final_phos = np.array(final_phos)
final_phos_cg = np.array(final_phos_cg)
final_phos = np.reshape(final_phos, (len(final_phos_cg), 3*n_phos))

final_constrinPX = pd.DataFrame(final_constrinPX)
final_constrinPY = pd.DataFrame(final_constrinPY)
final_constrinPZ = pd.DataFrame(final_constrinPZ)
final_constrinPX_sq = final_constrinPX**2
final_constrinPY_sq = final_constrinPY**2
final_constrinPZ_sq = final_constrinPZ**2

R = final_constrinPX_sq + final_constrinPY_sq + final_constrinPZ_sq
Rsqrt = np.sqrt(R)
dist_p1 = np.mean(Rsqrt)[0]
dist_p2 = np.mean(Rsqrt)[1]
dist_p3 = np.mean(Rsqrt)[2]
dist_p4 = np.mean(Rsqrt)[3]
############################################################

########## Calculation for Sugar  ##########################
final_sugar = np.array(final_sugar)
final_sugar_cg = np.array(final_sugar_cg)
final_sugar = np.reshape(final_sugar, (len(final_sugar_cg),3*n_sugar))

final_constrinSX = pd.DataFrame(final_constrinSX)
final_constrinSY = pd.DataFrame(final_constrinSY)
final_constrinSZ = pd.DataFrame(final_constrinSZ)
final_constrinSX_sq = final_constrinSX**2
final_constrinSY_sq = final_constrinSY**2
final_constrinSZ_sq = final_constrinSZ**2

R = final_constrinSX_sq + final_constrinSY_sq + final_constrinSZ_sq
Rsqrt = np.sqrt(R)
dist_s1 = np.mean(Rsqrt)[0]
dist_s2 = np.mean(Rsqrt)[1]
dist_s3 = np.mean(Rsqrt)[2]
dist_s4 = np.mean(Rsqrt)[3]
dist_s5 = np.mean(Rsqrt)[4]
dist_s6 = np.mean(Rsqrt)[5]
############################################################

########## Calculation for Base-A ##########################
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
dist_a1 = np.mean(Rsqrt)[0]
dist_a2 = np.mean(Rsqrt)[1]
dist_a3 = np.mean(Rsqrt)[2]
dist_a4 = np.mean(Rsqrt)[3]
dist_a5 = np.mean(Rsqrt)[4]
dist_a6 = np.mean(Rsqrt)[5]
dist_a7 = np.mean(Rsqrt)[6]
dist_a8 = np.mean(Rsqrt)[7]
dist_a9 = np.mean(Rsqrt)[8]
dist_a10 = np.mean(Rsqrt)[9]
############################################################

########## Calculation for Base-T ##########################
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
dist_t1 = np.mean(Rsqrt)[0]
dist_t2 = np.mean(Rsqrt)[1]
dist_t3 = np.mean(Rsqrt)[2]
dist_t4 = np.mean(Rsqrt)[3]
dist_t5 = np.mean(Rsqrt)[4]
dist_t6 = np.mean(Rsqrt)[5]
dist_t7 = np.mean(Rsqrt)[6]
dist_t8 = np.mean(Rsqrt)[7]
############################################################

########## Calculation for Base-G ##########################
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
dist_g1 = np.mean(Rsqrt)[0]
dist_g2 = np.mean(Rsqrt)[1]
dist_g3 = np.mean(Rsqrt)[2]
dist_g4 = np.mean(Rsqrt)[3]
dist_g5 = np.mean(Rsqrt)[4]
dist_g6 = np.mean(Rsqrt)[5]
dist_g7 = np.mean(Rsqrt)[6]
dist_g8 = np.mean(Rsqrt)[7]
dist_g9 = np.mean(Rsqrt)[8]
dist_g10 = np.mean(Rsqrt)[9]
dist_g11 = np.mean(Rsqrt)[10]
############################################################

########## Calculation for Base-C ##########################
final_baseC = np.array(final_baseC)
final_baseC_cg = np.array(final_baseC_cg)
final_baseC = np.reshape(final_baseC, (len(final_baseC_cg), 3*n_baseC))

final_constrinCX = pd.DataFrame(final_constrinCX)
final_constrinCY = pd.DataFrame(final_constrinCY)
final_constrinCZ = pd.DataFrame(final_constrinCZ)
final_constrinCX_sq = final_constrinCX**2
final_constrinCY_sq = final_constrinCY**2
final_constrinCZ_sq = final_constrinCZ**2

R = final_constrinCX_sq + final_constrinCY_sq + final_constrinCZ_sq
Rsqrt = np.sqrt(R)
dist_c1 = np.mean(Rsqrt)[0]
dist_c2 = np.mean(Rsqrt)[1]
dist_c3 = np.mean(Rsqrt)[2]
dist_c4 = np.mean(Rsqrt)[3]
dist_c5 = np.mean(Rsqrt)[4]
dist_c6 = np.mean(Rsqrt)[5]
dist_c7 = np.mean(Rsqrt)[6]
dist_c8 = np.mean(Rsqrt)[7]
#####################################################
