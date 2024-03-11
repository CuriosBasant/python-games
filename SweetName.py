txt=input();
print("It's very good to See you Here!\nI Hope You'll Like This.... \n\n")

alpha = {
  'A': ["aHa","J","CdC","CdC","J","J","CdC","CdC"],
  'B': ["Ia","J","CdC","Ia","Ia","CdC","J","Ia"],
  'C': ["aHa","J","CdC","Cg","Cg","CdC","J","aHa"],
  'D': ["Gc","Ia","CdC","CdC","CdC","CdC","Ia","Gc"],
  'E': ["I","I","Cf","I","I","Cf","I","I"],
  'F': ["I","I","Cf","Ha","Ha","Cf","Cf","Cf"],
  'G': ["aHa","J","Cg","CbE","CbE","CdC","J","aHa"],
  'H': ["CdC","CdC","CdC","J","J","CdC","CdC","CdC"],
  'I': ["H","H","bDb","bDb","bDb","bDb","H","H"],
  'J': ["fD","fD","fD","fD","fD","CcD","J","aHa"],
  'K': ["CcD","CbDa","CaDb","Gc","Gc","CaDb","CbDa","CcD"],
  'L': ["Cf","Cf","Cf","Cf","Cf","Cf","I","I"],
  'M': ["CfC","DdD","EbE","L","CaDaC","CbBbC","CfC","CfC"],
  'N': ["CdC","DcC","EbC","FaC","CaF","CbE","CcD","CdC"],
  'O': ["aHa","J","CdC","CdC","CdC","CdC","J","aHa"],
  'P': ["Ia","J","CdC","J","Ia","Cg","Cg","Cg"],
  'Q': ["aHa","J","DcC","CaAbC","CbAaC","CcD","J","aHa"],
  'R': ["Ia","J","CdC","J","Ia","CaDb","CbDa","CcD"],
  'S': ["aI","J","Cg","Ia","aI","gC","J","Ia"],
  'T': ["L","L","dDd","dDd","dDd","dDd","dDd","dDd"],
  'U': ["CfC","CfC","CfC","CfC","CfC","DdD","aJa","cFc"],
  'V': ["CgC","CgC","CgC","aCeCa","bCcCb","cCaCc","dEd","eCe"],
  'W': ["CkC","CkC","CkC","CeAeC","aCcCcCa","bCaEaCb","cEaEc","dCcCd"],
  'X': ["DeD","aDcDa","bDaDb","cGc","cGc","bDaDb","aDcDa","DeD"],
  'Y': ["DfD","aDdDa","bDbDb","cHc","dFd","eDe","eDe","eDe"],
  'Z': ["I","I","dDa","cDb","bDc","aDd","I","I"]  
  }
#---------------------------------------------------------------------
"""
def Disp(text):
  for c in range(len(text)):
    fg=text[c].isupper()
    for i in range(65 if fg else 97, ord(text[c])+1):
      print(end=('0' if fg else ' '))
  print()
  
for ch in range(len(txt)):
  for r in range(8):
    Disp(alpha[txt[ch].upper()][r])
  print()
"""
#----------------------------------------------------------------------

#hv, vh, nl=(range(8), range(len(txt)), '  ') if txt[0]=='=' else (range(len(txt)), range(8), '\n')

if txt[0]=='=':
  hv=range(1,8)
  vh=range(len(txt)-1)
  nl='   '
  #txt=txt[1:]
else:
  hv=range(len(txt))
  vh=range(8)
  nl='\n'

def Disp(text):
  for c in range(len(text)):
    fg=text[c].isupper()
    for i in range(64 if fg else 96, ord(text[c])):
      print(end=('0' if fg else ' '))
  print(end='  ')
  

for r in hv:
  for ch in vh:
    a, b=(r, ch) if txt[0]=='=' else (ch, r)
    Disp(alpha[txt[a].upper()][b])
  print()