s1=(" +------+\n        |\n        |\n        |\n     =======")
s2=(" +------+\n o      |\n        |\n        |\n     =======")
s3=(" +------+\n o      |\n/       |\n        |\n     =======")
s4=(" +------+\n o      |\n/|      |\n        |\n     =======")
s5=(" +------+\n o      |\n/|\     |\n        |\n     =======")
s6=(" +------+\n o      |\n/|\     |\n/       |\n     =======")
s7=(" +------+\n o      |\n/|\     |\n/ \     |\n     =======")

dct={0:s1,1:s2,2:s3,3:s4,4:s5,5:s6,6:s7,7:'',8:'',9:'',10:''}
import random
lst=("python","agency","almost","almost","action","advice","bright","bottom","breath","bridge","camera")
b=random.choice(lst)
lst1=[i for i in b]
mst=[i for i in b]
st='_'*len(lst1)
print(lst1)
print(st)
missed=''
u=0
for k in range(10):
    user=input("Guess a character :\n")
    
    
    if user in lst1:
        u+=1
        print(dct[u])
        if u==7:
            print("You Win The Game!!!")
            break
        
        ind=lst1.index(user)
        
        l=list(st)
        l[ind]=user
        st=''.join([str(i) for i in l])
        print(st)
        
    else:
        missed+=user+' '
        print('\nMissed Letters are: ',missed)
    if '_' not in st:
        print("You Won!!")
        break
print(st)

