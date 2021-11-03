file = open('text2.txt', 'w')
with open('text.txt') as f:  
    stri = f.read()
code=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
decode =['E','4','D','1','2','F','B','8','3','A','6','C','5','9','0','7']
d=''
s=0
str1=''
for i in range (len(stri)):
    for j in range (len(code)):
        if stri[i]==code[j]:
            str1+=stri[i]
            d+=decode[j]
            s+=1
            if s%4==0:
                file = open('text2.txt', 'a')  
                file.write('S['+str1+ ']')
                file.write('='+ d + '\n')
                str1=''
                d=''                
            
                
            
               
