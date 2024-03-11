"""
def bugctrl(dd,mm):
    _30=[4,6,9,11]
    _31=[1,3,5,7,8,10,12]
    if mm not in _30 or _31:
        if mm==2
"""
date=[int(input()) for i in range(3)]
m=date[1]+(10 if date[1]<3 else -2)
y=date[2]%100
c=(date[2]-y)/100
k=date[0]+int((13*m-1)/5)+y+int(y/4)+int(c/4)-2*c 
print(date[1], m)
day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
mon={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
print("The %dth of %s, %d falls on %s"%(date[0], mon[date[1]], date[2], day[k%7]))
