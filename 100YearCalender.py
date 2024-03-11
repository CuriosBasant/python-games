"""
for i in range(1,29):
    for j in range(i,6*28,28):
        print(int('2'+'{:0>3}'.format(j))%28, end='\t')
    print()
    meri taqdeer khul gyi ae
"""
dd, mm, yy = input('Enter a Valid Date: ').split(' ')
lis=['G','A','B','J','E','F','G','H','C','D','E','M','A','B','C','K','F','G','A','I','D','E','F','N','B','C','D','L']
year=[0,6,1,2,4,5,0,6,2,3,4,5,6,1,2,3,5,0,6,1,3,4,5,0,1,2,3,4]
mon=[3,0,3,2,3,2,3,3,2,3,2,3]
#for i in range(28): print(2017+i,'\t',lis[i],'\t',i)
for i in range(28):
    print((ord(lis[i])-65)%7, end=',')

cntr=year[yy%28]+mon[mm-1]+
week={
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
    }
""" 
