"""
This is my First Ever Code in Python.
Thanks to this SoloLearn Community and it's very well-behaved, polite members.

To run the Code you simply have to Enter a String (or your Sweet Name)

If you found any error or any Problem in executing this Code, please let me know about that in the Comment Section below!
"""
print("""
It's very good to See you Here!
I Hope You'll Like This...

Coded by: CuriosBasant
""")

"""alpha = {
  'A': ['aH','J','CdC','CdC','J','J','CdC','CdC'],
  'B': ['I','J','CdC','I','I','CdC','J','I'],
  'C': ['aH','J','CdC','Cg','Cg','CdC','J','aH'],
  'D': ['Gc','I','CdC','CdC','CdC','CdC','I','G'],
  'E': ['I','I','C','I','I','C','I','I'],
  'F': ['I','I','C','H','H','C','C','C'],
  'G': ['aH','J','C','CbE','CbE','CdC','J','aH'],
  'H': ['CdC','CdC','CdC','J','J','CdC','CdC','CdC'],
  'I': ['H','H','bD','bD','bD','bD','H','H'],
  'J': ['fD','fD','fD','fD','fD','CcD','J','aH'],
  'K': ['CcD','CbD','CaD','G','G','CaD','CbD','CcD'],
  'L': ['C','C','C','C','C','C','I','I'],
  'M': ['CgC','DeD','EcE','M','CaEaC','CbCbC','CgC','CgC'],
  'N': ['CdC','DcC','EbC','FaC','CaF','CbE','CcD','CdC'],
  'O': ['aH','J','CdC','CdC','CdC','CdC','J','aH'],
  'P': ['I','J','CdC','J','I','C','C','C'],
  'Q': ['aH','J','DcC','CaAbC','CbAaC','CcD','J','aH'],
  'R': ['I','J','CdC','J','I','CaD','CbD','CcD'],
  'S': ['aI','K','C','J','aJ','hC','K','aI'],
  'T': ['L','L','dD','dD','dD','dD','dD','dD'],
  'U': ['CfC','CfC','CfC','CfC','CfC','DdD','aJ','cF'],
  'V': ['CgC','CgC','CgC','aCeC','bCcC','cCaC','dE','eC'],
  'W': ['CgC','CgC','CgC','CbCbC','CaEaC','M','EcE','DeD'],
  'X': ['DeD','aDcD','bDaD','cG','cG','bDaD','aDcD','DeD'],
  'Y': ['CgC','aCeC','bCcC','cCaC','dE','eC','eC','eC'],
  'Z': ['I','I','dD','cD','bD','aD','I','I']  
  }"""
C='CdC' #frequently used string
alpha = {
  'A': ['aHa','J']+[C]*2+['J']*2+[C]*2,
  'B': ['Ia','J',C,'Ia'],
  'C': ['aHa','J',C,'Cg'],
  'D': ['Gc','Ia']+[C]*2,
  'E': ['J']*2+['Cg','J'],
  'F': ['J']*2+['Cg']+['Ia']*2+['Cg']*3,
  'G': ['aHa','J','Cg']+['CbE']*2+[C,'J','aHa'],
  'H': [C]*3+['J'],
  'I': ['J']*2+['cDc']*2,
  'J': ['fD']*5+['CcD','J','aHa'],
  'K': ['CcD','CbDa','CaDb','Gc'],
  'L': ['Df']*6+['J']*2,
  'M': ['CgC','DeD','EcE','M','CaEaC','CbCbC']+['CgC']*2,
  'N': [C,'DcC','EbC','FaC','CaF','CbE','CcD',C],
  'O': ['aHa','J']+[C]*2,
  'P': ['Ia','J',C,'J','Ia']+['Cg']*3,
  'Q': ['aHa','J','DcC','CaAbC','CbAaC','CcD','J','aHa'],
  'R': ['Ia','J',C,'J','Ia','CaDb','CbDa','CcD'],
  'S': ['aKa','M','Di','La','aL','iD','M','aKa'],
  'T': ['M']*2+['dEd']*6,
  'U': ['DeD']*5+['EcE','aKa','cGc'],
  'V': ['CgC']*3+['aCeCa','bCcCb','cCaCc','dEd','eCe'],
  'W': ['CgC']*3+['CbCbC','CaEaC','M','EcE','DeD'],
  'X': ['DeD','aDcDa','bDaDb','cGc'],
  'Y': ['CgC','aCeCa','bCcCb','cCaCc','dEd']+['eCe']*3,
  'Z': ['M']*2+['gEa','eEc','cEe','aEg']+['M']*2
  }

for t in ['B','C','D','E','H','I','K','O','X']: alpha[t]+=reversed(alpha[t])

def disp(text):
  for c in range(len(text)):
    flag=text[c].isupper()
    print(('0' if flag else ' ')*(ord(text[c])-(64 if flag else 96)), end='')
  print()


while True:
  text=input()
  for i in range(len(text)):
     if text[i]==' ':
        print('\n')
        continue
     for r in range(8):
        disp(alpha[text[i].upper()][r])
     print()
  if input('Want to Continue : ')=='n': break
