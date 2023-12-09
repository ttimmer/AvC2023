class Moves:
     def __init__(self, start, left, right):
        self.start = start
        self.left = left
        self.right = right
def find_next(Move_list,moveto):
    for move in Move_list:
       # print(f"Move towards {moveto} {move.start} is { moveto in move.start}")
        if moveto in move.start:
            return move
        else:
            pass
def find_all_start(Move_list,start):
    new_list = []
    for move in Move_list:
         if start in move.start[2]:
            new_list.append(move)
         else:
            pass
    return new_list

def find_all_next(Move_list,move_to_list):
    new_list = []
    for moveto in move_to_list:
        for move in Move_list:
             if moveto in move.start:
                new_list.append(move)
             else:
                pass
    return new_list
def parse_input(input):
    input_lines= input.splitlines()
    sequence = input_lines[0]
    move_list = []
    for line in input_lines[1:]:
        start = line.split(' = ')[0].strip()
        moves = line.split(' = ')[1]
        left_move = moves.split(',')[0][1:].strip()
        right_move = moves.split(',')[1][:-1].strip()
        move_list.append(Moves(start,left_move,right_move))
       # print(f"Start {start}, {left_move},{right_move}")
    return move_list,sequence
def perform_solution(input):
    move_list,sequence = parse_input(input)

    currentposition = find_next(move_list,'AAA')
    sequencePos = 0
    iterations = 0
    #print(f"This is the sequence {sequence}")
    while not (currentposition.start =='ZZZ'):
        decision = sequence[sequencePos]
        moveto =''
        if decision == 'L':
            moveto = currentposition.left
        elif decision =='R':
            moveto = currentposition.right
        #print(f"{iterations} from {currentposition.start} {decision} to {currentposition.left} or {currentposition.right}")
        iterations+=1
        currentposition= find_next(move_list,moveto)
        if sequencePos==len(sequence)-1:
            #print(f"Retrysequence")
            sequencePos= 0;
        else:
            sequencePos+=1
    #print(iterations)
    return iterations

def perform_solution2(input):
   move_list,sequence =  parse_input(input)
   currentpositions = find_all_start(move_list,'A')
   sequencePos = 0
   iterations = 0
   iterationlist = []
   while len(find_all_start(currentpositions,'Z'))<len(currentpositions):
       decision = sequence[sequencePos]
       moveto_list =[]
       for position in currentpositions:
            if decision == 'L':
                moveto = position.left
            elif decision =='R':
                moveto = position.right
            elif decision == 'Z':
                moveto = currentpositions
                print(currentpositions)
                iterationlist.append(iterations)
            moveto_list.append(moveto)
       iterations+=1
       if decision!= 'Z':
            currentpositions= find_all_next(move_list,moveto_list)
       if sequencePos==len(sequence)-1:
           sequencePos= 0
       else:
           sequencePos+=1

   summed_value =1
   for x in iterationlist:
       summed_value =summed_value*int(x)
   print(summed_value)

   return iterations

if __name__ == '__main__':
    input_test = """LLR
AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
    solution_test1 = 6
    if (solution_test1== perform_solution(input_test)):
        print("Test number one works")

    input_actual ="""LRLLLRRLRRLRRLRRLLRRLRRLLRRRLLRRLRRLRRLRRLRLRLLLLLRRLRRLLRLRRRLLRRLRLLLLLLLRRLRLRRRLRRLRRRLRRLLLRRLLRRRLLRRRLRRLRLRRRLRRRLRLRLLRRRLRRRLRRLLRRRLRLRRLLRLLRRLLRRLRRRLRRLRLRRLLRRRLRRRLRRRLRLRLRLRRRLLRRRLRLRRLLRRLRRLRRLRLLRRLLRRRLRRRLRRLRRLRLLRRLRLRRLRRRLRRRLRRLRLRRRLRRRLRLLLRRLRLLRRRR
RLP = (BMK, PCM)
JTJ = (TVN, CJQ)
PFR = (MMX, BQC)
JGM = (NDJ, PCV)
LVD = (TCK, PVR)
SVS = (CDL, RNX)
QDF = (XFG, NDX)
TBH = (THM, DBC)
FQK = (TFT, CNF)
THV = (NQD, VNT)
VRL = (HCQ, DPS)
LDM = (CCH, PJB)
GXR = (BRH, XLM)
CKF = (THV, BNQ)
KMH = (TLN, PKX)
SLP = (XSV, VCR)
SXF = (MJC, TJX)
KMJ = (LBC, FKT)
VDX = (MJQ, SGJ)
SHM = (LJT, PBV)
PGX = (KFM, SLD)
VHN = (BBB, SJV)
BFL = (VJG, JJF)
HKX = (HNN, MQK)
SNB = (PFJ, CTB)
GCD = (BKX, DHR)
DQN = (CTP, XDN)
DJP = (GGK, NSF)
KPG = (QCX, PQR)
PGR = (QXN, PGT)
RVG = (QDF, MVK)
BMV = (FFH, FFH)
VCX = (LDH, TQD)
KLC = (DFP, FQD)
JMQ = (JKT, BVH)
KLM = (QJQ, NMB)
TTQ = (GMV, QFC)
XFG = (RCP, DTL)
DDC = (FKG, JGM)
FCD = (SPS, JSS)
LBC = (VDX, NFH)
RXN = (KTP, JMB)
MVH = (NJC, LVJ)
PJB = (RXN, JSB)
PBS = (QGF, LSB)
RCP = (PKL, HSJ)
TBF = (RJP, JHJ)
SFB = (FQH, TMH)
XLC = (BXM, MSF)
TCS = (TGT, GPT)
CPQ = (JXT, FCH)
GDM = (XBM, DDS)
QQQ = (FLS, VCX)
MDT = (TFS, TLV)
PFK = (NPJ, SSR)
KSN = (JXV, DRL)
VBS = (NJC, LVJ)
TCP = (TBK, XXS)
QTT = (FLS, VCX)
FSH = (FBM, XXN)
MND = (KJH, MGC)
DTN = (JNL, CGM)
QXV = (NQJ, FSR)
TRQ = (SNB, QRR)
RCG = (NMR, BRG)
TGB = (KFM, SLD)
QSK = (NNT, TBH)
DDD = (HPQ, XGH)
KHK = (XMS, DXH)
VVC = (CDB, LNP)
KNT = (MTB, QXS)
FBH = (HXT, FBG)
LJB = (TBF, FXQ)
HHH = (RPH, FSB)
KMR = (PFT, VVC)
CFC = (TVV, TVV)
LKC = (LHN, QRL)
PFT = (CDB, LNP)
JXV = (NXS, KVX)
XDN = (BRK, GGS)
NQJ = (KMH, QSS)
FQD = (PVS, JBV)
KJX = (DJV, XPP)
VJP = (HKX, VDR)
BSQ = (MGS, CFK)
VJG = (PSQ, KSD)
NNZ = (GPT, TGT)
CSR = (MFN, NQF)
KFM = (GFN, GMH)
PHR = (TJC, XTJ)
KCL = (JJG, VJL)
VCR = (BML, KCS)
PVM = (BMH, QDN)
HPQ = (LFD, FQM)
MLR = (JKV, NTB)
XGV = (RQL, JKX)
FHB = (NPR, MNG)
DBC = (LDK, TVP)
FSN = (XQR, DBZ)
JJF = (PSQ, KSD)
CLK = (BMH, QDN)
QMH = (BLQ, VKX)
SBH = (SRN, SPX)
MJP = (JXV, DRL)
CTB = (XSF, XKC)
BJK = (RKS, FQB)
CCX = (CND, CND)
DTL = (HSJ, PKL)
NNT = (THM, DBC)
GBR = (XGG, LNN)
AAA = (XRF, DNR)
FLJ = (GNM, MTK)
BXQ = (LNX, GFM)
GMH = (JXC, CSR)
DXL = (SVN, FGV)
XBD = (GHF, HJQ)
PTQ = (SGQ, GVD)
SCJ = (SJV, BBB)
LHN = (LHH, FLK)
HBL = (JVT, MHM)
QLM = (TVJ, SVB)
BRH = (HNK, CTR)
MQJ = (GQR, DDC)
MTM = (KLV, FGJ)
MJQ = (LPR, JFH)
GQJ = (GKT, JKP)
FDC = (KPG, LDQ)
DRN = (SBH, NNV)
JRT = (DJP, JFJ)
LCP = (HPL, KLJ)
SDL = (MST, PDL)
NGM = (DRH, RTK)
TVV = (JSL, JSL)
QRR = (CTB, PFJ)
GGS = (FHF, XSJ)
MKD = (NGR, CDR)
GBM = (MNR, SVS)
SHK = (NMK, KNH)
BKB = (GHB, RVC)
GHH = (CFC, HQT)
CRN = (LBC, FKT)
BCF = (CBQ, NGM)
MQK = (DXL, JQV)
XQK = (TTG, XTV)
PMZ = (FBH, VMT)
LGV = (QMH, QPM)
TMH = (MTM, MVR)
TRM = (DJJ, FJS)
XFS = (XDH, VFP)
QPM = (VKX, BLQ)
CJN = (RXP, KLC)
RBC = (CND, DKZ)
RSP = (TTQ, PQQ)
LVJ = (XXK, XGT)
TTN = (BVH, JKT)
MBS = (KLM, XHN)
PJK = (CCS, TRS)
LDX = (XGM, PBP)
XGB = (NBS, LGV)
QXF = (MLR, MKB)
FFD = (MQF, MQF)
NPR = (BMQ, TPX)
JPN = (TBK, XXS)
FQJ = (MXL, BXP)
QXP = (JNL, CGM)
XBQ = (DDS, XBM)
NNG = (VJL, JJG)
BLQ = (CBN, FDT)
FQB = (XNP, SNR)
DHR = (DCM, SHK)
JVT = (KKR, BXQ)
PCV = (FFD, PDG)
PFJ = (XKC, XSF)
RTB = (RHT, SPG)
BXF = (PGR, CFJ)
DGS = (MKB, MLR)
MTK = (NJL, PQJ)
NMS = (XQJ, TLL)
XFF = (KHK, DRB)
MDR = (HCQ, DPS)
GMD = (XTT, XKV)
FKT = (VDX, NFH)
VNS = (PFR, GMK)
JTB = (BSC, XFF)
XPM = (BSQ, MFD)
QDT = (GQJ, GPK)
LLV = (VCR, XSV)
BQC = (MVH, VBS)
JLL = (CRV, HBL)
SNH = (LJT, PBV)
XGG = (LVD, RCD)
LPR = (JBJ, JBH)
QVC = (BXM, MSF)
NMB = (HQD, FVF)
XST = (GBM, MKH)
VTL = (JXT, FCH)
LDQ = (QCX, PQR)
QKK = (GFP, CVB)
KLV = (JCR, CJV)
GLC = (MNG, NPR)
GHJ = (JTB, KVQ)
XRF = (FTK, JXN)
JGB = (HQS, JSG)
VNT = (NCK, TXF)
PGT = (VVV, JDP)
GFB = (PSM, VLK)
TVP = (RDX, PPL)
VKX = (CBN, FDT)
NMR = (HLQ, NCV)
MGQ = (TPM, MND)
TFT = (DKH, TSX)
CBV = (CCX, CCX)
TJS = (RJK, RMC)
TRX = (XBB, MDP)
MTB = (QMV, RMR)
XSL = (CFC, HQT)
FRK = (SVF, LDX)
QGM = (LDM, GMS)
XGS = (NGR, CDR)
CTP = (GGS, BRK)
JXT = (JCN, KGR)
GFM = (FJQ, TMX)
NST = (MBS, MTX)
NDV = (JJT, KMR)
RDD = (MJP, KSN)
RDX = (JTJ, SKB)
HDF = (TVK, LCP)
DJV = (TRF, TFJ)
SGJ = (JFH, LPR)
BTX = (PHB, PBS)
KMK = (MQB, VLQ)
HXM = (VLK, PSM)
DPS = (QPG, HDC)
RJP = (PGL, SXF)
DKZ = (KCL, NNG)
GHR = (DFN, XTH)
XQJ = (JGB, BLH)
BRG = (NCV, HLQ)
HJQ = (QQQ, QTT)
JBJ = (JRT, HDD)
XSV = (KCS, BML)
CDL = (QDT, NGV)
LQS = (PCL, CKF)
TGH = (SSR, NPJ)
DBK = (MVC, GFJ)
VRX = (FXB, PHR)
RBH = (FFH, DXV)
DRQ = (GDJ, QBV)
GNM = (NJL, PQJ)
NCF = (QRL, LHN)
JQP = (KMR, JJT)
SBN = (TXS, QXB)
CFJ = (PGT, QXN)
KVQ = (XFF, BSC)
NDX = (RCP, DTL)
SRF = (KJX, QJG)
BFD = (LCP, TVK)
PBN = (XKL, TJS)
GRB = (QBV, GDJ)
TGT = (RGF, LQT)
TFJ = (LPT, KMK)
SRT = (FQQ, GBR)
THM = (LDK, TVP)
KVB = (RXP, KLC)
TVJ = (QVS, SQP)
XHN = (NMB, QJQ)
QGF = (JVB, GCD)
RKS = (XNP, SNR)
MFN = (NKF, RCG)
BVH = (QKK, TJL)
CNF = (DKH, TSX)
MSF = (QXP, DTN)
KCS = (LMM, GMD)
XGH = (LFD, FQM)
KJH = (KLD, FNH)
PKM = (BRH, XLM)
VVT = (CFJ, PGR)
XTC = (PHB, PBS)
LQT = (BTJ, DPM)
JKX = (TBP, QGM)
ZZZ = (DNR, XRF)
QXS = (RMR, QMV)
PBP = (KVB, CJN)
TTG = (FDM, FDM)
BML = (LMM, GMD)
RNX = (NGV, QDT)
TPX = (NDB, GHR)
MFS = (SDL, LRQ)
LGG = (LXG, JLL)
MJC = (GVX, JJK)
RRF = (GSK, NMS)
FBM = (HBB, FQJ)
PQQ = (QFC, GMV)
FCH = (KGR, JCN)
PDG = (MQF, FSN)
HLQ = (NGF, FKK)
QQB = (MTB, QXS)
HNN = (JQV, DXL)
TLN = (CNJ, PSX)
NGV = (GPK, GQJ)
LDK = (RDX, PPL)
NJC = (XXK, XGT)
XQA = (TGT, GPT)
JCH = (XBB, MDP)
KMB = (QJG, KJX)
TCK = (VVH, SML)
FKS = (PVM, CLK)
GMS = (CCH, PJB)
LHH = (GRB, DRQ)
JML = (RQL, JKX)
DTP = (TGH, PFK)
BKX = (SHK, DCM)
HPL = (QLM, DPV)
JJG = (VKR, DQN)
PDL = (QNS, BJC)
SLD = (GFN, GMH)
JQV = (SVN, FGV)
FKK = (LLV, SLP)
CTC = (HKX, VDR)
TSX = (FRM, FRK)
FNH = (BTX, XTC)
JMB = (BCF, SKS)
KGR = (QLB, HTP)
TXS = (VRL, MDR)
KNH = (DGS, QXF)
DDS = (VHN, SCJ)
MML = (TPM, MND)
XKB = (SHM, SNH)
RMC = (FRX, JRJ)
XVP = (JSL, LSH)
HXT = (GLC, FHB)
FQM = (MDT, DBH)
PSX = (LRL, GHJ)
VSC = (FXQ, TBF)
JFH = (JBJ, JBH)
SML = (GSN, TVS)
BMK = (XNT, KCD)
VFP = (BXF, VVT)
GHB = (LHM, HDQ)
FDM = (SGQ, SGQ)
FQH = (MTM, MVR)
JJC = (GXR, PKM)
HFM = (PKM, GXR)
LNX = (FJQ, FJQ)
XTT = (VRX, PML)
TQD = (NSN, DDD)
FGV = (XFS, FLT)
FHF = (QXV, NVN)
HDQ = (TTB, RLP)
CQN = (STG, LQS)
VNJ = (SNH, SHM)
DPB = (JTP, PJK)
JCQ = (CNF, TFT)
LPF = (XMB, FBB)
SQP = (JML, XGV)
QSS = (TLN, PKX)
CDB = (SDB, QJS)
GTF = (TRQ, QNQ)
KSD = (BMV, RBH)
JFD = (CCX, RBC)
GSN = (DRN, KKD)
RXP = (DFP, FQD)
RTK = (RDD, DTF)
GPT = (LQT, RGF)
TLV = (LGT, VGM)
FSB = (HGC, TXM)
KKD = (SBH, NNV)
XNT = (LJB, VSC)
LXG = (HBL, CRV)
TTB = (PCM, BMK)
QPG = (KKX, SFB)
RQL = (QGM, TBP)
JNL = (JJC, HFM)
TPM = (KJH, MGC)
KKR = (LNX, GFM)
SVF = (PBP, XGM)
LHM = (RLP, TTB)
JDP = (XQL, NST)
PCM = (KCD, XNT)
TQF = (LDQ, KPG)
NGR = (DTP, NFD)
PPS = (NQN, RHG)
DRL = (KVX, NXS)
MVF = (CPP, FCD)
SSR = (BJK, VCP)
DRH = (RDD, DTF)
NSJ = (FKS, XVL)
CPS = (QDF, MVK)
PML = (PHR, FXB)
DPM = (MML, MGQ)
MJS = (QKF, PMZ)
JSS = (XPM, FLV)
CRV = (JVT, MHM)
QJS = (PKV, RTB)
JHJ = (PGL, SXF)
JSB = (KTP, JMB)
KBN = (JHB, NJZ)
BMJ = (CCK, GTF)
NDJ = (FFD, FFD)
LFD = (MDT, DBH)
NQD = (NCK, TXF)
NSN = (HPQ, XGH)
XKV = (PML, VRX)
SHS = (NBS, LGV)
SRN = (KRJ, DPJ)
QCX = (HHH, LLJ)
MNG = (TPX, BMQ)
TJX = (GVX, JJK)
FVF = (PPS, LFK)
LDH = (DDD, NSN)
MVC = (FHQ, MQJ)
TJL = (GFP, CVB)
JXC = (MFN, NQF)
LJT = (LKC, NCF)
PVS = (XGB, SHS)
VVV = (NST, XQL)
CBQ = (DRH, RTK)
SKS = (NGM, CBQ)
LLJ = (FSB, RPH)
CND = (NNG, KCL)
JSG = (SFL, LCQ)
NJZ = (VMD, PBN)
PKL = (XGS, MKD)
BLH = (JSG, HQS)
JHB = (PBN, VMD)
GQR = (FKG, JGM)
CNJ = (GHJ, LRL)
MVR = (KLV, FGJ)
SPG = (XQC, FJX)
FTK = (SBN, PDJ)
FJB = (FQQ, GBR)
LRL = (KVQ, JTB)
PQJ = (XST, TMM)
NXS = (JHF, SKG)
TFS = (LGT, VGM)
SNR = (RSP, XTB)
DPJ = (VXJ, DBK)
NJL = (XST, TMM)
VCP = (FQB, RKS)
NGF = (LLV, SLP)
KLD = (XTC, BTX)
QJF = (QQB, KNT)
FHQ = (GQR, DDC)
MQB = (VNJ, XKB)
FHG = (LLC, QSK)
VXJ = (GFJ, MVC)
LJV = (TRM, FXH)
TXM = (GFB, HXM)
BMQ = (NDB, GHR)
MXL = (RSB, FHL)
TBK = (HHK, DQQ)
GKT = (LGG, FHR)
DTF = (KSN, MJP)
VDJ = (MTK, GNM)
PCL = (BNQ, THV)
VLK = (XCH, LJV)
BSC = (KHK, DRB)
XTH = (VTL, CPQ)
XXS = (HHK, DQQ)
GMV = (MFS, XLJ)
BMH = (SLL, CTM)
RGF = (BTJ, DPM)
FJS = (DPB, PLN)
QDN = (SLL, CTM)
CVB = (CBV, JFD)
TMX = (XCR, KBN)
XKC = (JQP, NDV)
VGM = (QVC, XLC)
FGT = (SJH, MVF)
DXV = (DQL, MJS)
MGC = (FNH, KLD)
CCS = (JFG, NGD)
STG = (PCL, CKF)
NKF = (BRG, NMR)
HQT = (TVV, XVP)
QJQ = (HQD, FVF)
HQS = (SFL, LCQ)
MGS = (XBD, QHS)
QXB = (MDR, VRL)
GFP = (CBV, CBV)
JVX = (XRF, DNR)
MST = (BJC, QNS)
PBV = (NCF, LKC)
RJS = (MVF, SJH)
NBS = (QMH, QPM)
QHS = (GHF, HJQ)
XQL = (MBS, MTX)
DQQ = (LTJ, BKB)
SJV = (HDF, BFD)
VLQ = (XKB, VNJ)
CBN = (GHH, XSL)
JKT = (QKK, TJL)
MQF = (XQR, XQR)
MVK = (NDX, XFG)
CPP = (SPS, JSS)
FJX = (NSJ, PJD)
SKA = (VMT, FBH)
NDB = (XTH, DFN)
CCH = (RXN, JSB)
VVH = (GSN, TVS)
SVB = (SQP, QVS)
JXN = (PDJ, SBN)
PLN = (JTP, PJK)
DNR = (FTK, JXN)
RVC = (LHM, HDQ)
QKF = (VMT, FBH)
MNS = (GMK, PFR)
QLB = (FSH, MQP)
RHT = (XQC, FJX)
KCD = (VSC, LJB)
DQL = (QKF, QKF)
TBP = (LDM, GMS)
TRS = (NGD, JFG)
JKP = (LGG, FHR)
QXN = (VVV, JDP)
LCQ = (XBQ, GDM)
KLJ = (DPV, QLM)
BFK = (NMS, GSK)
DXH = (RVG, CPS)
JTP = (TRS, CCS)
MNR = (CDL, RNX)
SFL = (XBQ, GDM)
TJC = (MNS, VNS)
SDB = (PKV, RTB)
BBB = (BFD, HDF)
QRG = (TTG, XTV)
XSF = (NDV, JQP)
HQD = (LFK, PPS)
FHR = (JLL, LXG)
FBG = (GLC, FHB)
XCH = (FXH, TRM)
SGQ = (TCS, TCS)
DBZ = (GDD, CQN)
QFC = (MFS, XLJ)
KTP = (SKS, BCF)
HBB = (MXL, BXP)
TLL = (BLH, JGB)
RMR = (CQM, FHG)
BXM = (DTN, QXP)
GDD = (LQS, STG)
DFN = (VTL, CPQ)
DBH = (TLV, TFS)
HNK = (CTC, VJP)
FRX = (RRF, BFK)
XMB = (TGB, PGX)
NTB = (DBB, LPF)
MFD = (MGS, CFK)
JFJ = (GGK, NSF)
GDJ = (FQK, JCQ)
XCR = (JHB, JHB)
LRQ = (PDL, MST)
DPV = (SVB, TVJ)
HDC = (SFB, KKX)
LMM = (XTT, XKV)
SLL = (TRX, JCH)
PSQ = (BMV, RBH)
VJL = (VKR, DQN)
SPX = (DPJ, KRJ)
DBB = (FBB, XMB)
SPS = (FLV, XPM)
FRM = (LDX, SVF)
PKX = (CNJ, PSX)
TMM = (GBM, MKH)
VDR = (MQK, HNN)
MHM = (KKR, BXQ)
TVN = (XQK, QRG)
NSF = (VDJ, FLJ)
FXH = (DJJ, FJS)
FGJ = (JCR, CJV)
SJH = (FCD, CPP)
JJT = (VVC, PFT)
DRB = (DXH, XMS)
LNP = (QJS, SDB)
FKG = (NDJ, PCV)
CQM = (LLC, QSK)
HTP = (FSH, MQP)
FJQ = (XCR, XCR)
CFK = (QHS, XBD)
QJG = (DJV, XPP)
KKX = (FQH, TMH)
LSJ = (TCP, JPN)
QHD = (JPN, TCP)
PVR = (SML, VVH)
XSJ = (NVN, QXV)
QMV = (FHG, CQM)
NFD = (TGH, PFK)
LTJ = (GHB, RVC)
HCQ = (HDC, QPG)
JKV = (LPF, DBB)
BNQ = (NQD, VNT)
GGK = (VDJ, FLJ)
LLC = (NNT, TBH)
SKB = (TVN, CJQ)
KRJ = (DBK, VXJ)
BTJ = (MML, MGQ)
GJM = (CCK, GTF)
JHF = (QHD, LSJ)
GFJ = (FHQ, MQJ)
LFK = (NQN, RHG)
GVD = (TCS, NNZ)
XDH = (VVT, BXF)
NCK = (BMJ, GJM)
QRL = (FLK, LHH)
XKL = (RJK, RMC)
TXF = (BMJ, GJM)
TVS = (DRN, KKD)
FXQ = (JHJ, RJP)
XTB = (PQQ, TTQ)
XBB = (SRT, FJB)
DFP = (JBV, PVS)
NQA = (NNG, KCL)
DKH = (FRM, FRK)
CCK = (TRQ, QNQ)
XTJ = (MNS, VNS)
MDP = (FJB, SRT)
QBV = (JCQ, FQK)
PKV = (RHT, SPG)
CJV = (FDC, TQF)
LSH = (JVX, ZZZ)
JJK = (CRN, KMJ)
LPT = (MQB, VLQ)
RHG = (BFL, SJT)
FLT = (XDH, VFP)
KVX = (JHF, SKG)
FXB = (XTJ, TJC)
HSJ = (XGS, MKD)
PDJ = (TXS, QXB)
XNP = (XTB, RSP)
LGT = (QVC, XLC)
XPP = (TRF, TFJ)
XQR = (CQN, GDD)
NNV = (SRN, SPX)
FLV = (MFD, BSQ)
QVS = (XGV, JML)
JSL = (JVX, JVX)
CQP = (QQB, KNT)
TVK = (KLJ, HPL)
QNS = (JMQ, TTN)
BXP = (FHL, RSB)
JFG = (KMB, SRF)
GMK = (MMX, BQC)
MTX = (KLM, XHN)
CTM = (JCH, TRX)
XBM = (SCJ, VHN)
RCD = (PVR, TCK)
XLJ = (LRQ, SDL)
PPL = (JTJ, SKB)
NQF = (NKF, RCG)
RSB = (FGT, RJS)
NCV = (FKK, NGF)
GHF = (QTT, QQQ)
XVL = (PVM, CLK)
VMD = (XKL, TJS)
CTR = (VJP, CTC)
CGM = (JJC, HFM)
PJD = (XVL, FKS)
LJA = (CQN, GDD)
MKH = (MNR, SVS)
JVB = (DHR, BKX)
HDD = (DJP, JFJ)
XGM = (CJN, KVB)
HHK = (LTJ, BKB)
CJQ = (XQK, QRG)
FHL = (RJS, FGT)
FQQ = (XGG, LNN)
MMX = (MVH, VBS)
FLS = (TQD, LDH)
VMT = (HXT, FBG)
PSM = (LJV, XCH)
JBV = (XGB, SHS)
FSR = (QSS, KMH)
FDT = (GHH, XSL)
LSB = (GCD, JVB)
XMS = (CPS, RVG)
FLK = (GRB, DRQ)
PGL = (TJX, MJC)
JCN = (HTP, QLB)
JRJ = (RRF, BFK)
FFH = (DQL, DQL)
XTV = (FDM, PTQ)
VKR = (XDN, CTP)
XXK = (CQP, QJF)
SKG = (QHD, LSJ)
MQP = (XXN, FBM)
GFN = (JXC, CSR)
BJC = (TTN, JMQ)
NVN = (FSR, NQJ)
PHB = (QGF, LSB)
NPJ = (VCP, BJK)
LNN = (LVD, RCD)
BRK = (FHF, XSJ)
JBH = (HDD, JRT)
XXN = (FQJ, HBB)
SJT = (JJF, VJG)
DCM = (NMK, KNH)
GSK = (XQJ, TLL)
XGT = (CQP, QJF)
RJK = (FRX, JRJ)
DJJ = (PLN, DPB)
TRF = (LPT, KMK)
JCR = (TQF, FDC)
RPH = (TXM, HGC)
MKB = (NTB, JKV)
XQC = (PJD, NSJ)
NGD = (SRF, KMB)
GVX = (KMJ, CRN)
GPK = (GKT, JKP)
SVN = (FLT, XFS)
FBB = (PGX, TGB)
CDR = (DTP, NFD)
HGC = (HXM, GFB)
PQR = (HHH, LLJ)
QNQ = (SNB, QRR)
NVA = (PBN, VMD)
NFH = (SGJ, MJQ)
NMK = (QXF, DGS)
XLM = (CTR, HNK)
NQN = (SJT, BFL)"""
    print(perform_solution(input_actual))
    input_test2 ="""LR
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
    solution_test2 = 6
    if (solution_test2== perform_solution2(input_test2)):
        print("Test number two works")

    print(perform_solution2(input_actual))

