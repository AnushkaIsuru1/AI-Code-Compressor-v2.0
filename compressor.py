rpc = [" ",";"]
skbfsm = [":", "{", ">", ";", ",", "(", "["]
rmafsc=[" ",";"]
skspbf = [")" , "}","]",","]

def rmvcmnt(t):
    fn1=fn2=1
    t1=t2=""
    r = ""
    for l in t:
        if fn1:
            if(r==l=="/"):fn1 = 0; t1 = t1[0:len(t1)-1]
            else: t1+=l
        elif (l=="\n"):fn1=1; t1+=l
        r = l
    #css
    r = ""
    for l in t1:
        if fn2:
            if((r=="/") and (l=="*")):fn2 = 0; t2 = t2[0:len(t2)-1]
            else: t2+=l
        elif ((r=="*") and (l=="/")):fn2=1; t2+=" "
        r = l
    #html
    fn = 1
    r1=r2=r3=t3=""
    for l in t2:
        if fn:
            if (r1+r2+r3+l == "<!--"):fn = 0; t3 = t3[0:len(t3)-3]
            else:t3+=l
        elif (r2+r3+l=="-->"):fn=1
        r1 = r2
        r2 = r3
        r3 = l
    #php
    r1=r2=r3=r4=t4=""
    php = 0
    qut = 0
    cm=0
    lqut = ""
    for a in t3:
        if (php):              
            if not cm:
                if ((not qut) and (a=="#")):cm=1
                else:t4+=a
            elif (a=="\n"):cm = 0;t4+=a
        else:t4+=a                
        if (r1+r2+r3+r4+a=="<?php"):php=1
        elif (php and (r4+a=="?>")):php=0
        if (not(qut) and(a in ["'",'"'])):qut=1;lqut = a
        elif ((a == lqut) and (r4!="\\")):qut = 0
        r1 = r2
        r2 = r3
        r3 = r4
        r4 = a
    return(t4)

def jscript(t):
    l1=l2=l3=l4=l5=l6=l7=l8 = t1= ""
    x = fn1 = fn2= 0
    while (x<len(t)):
        r = t[x]
        t1+=r
        if (fn2 and (r=="\n")):t1=t1[0:len(t1)-1]+";"
        if ( x>5 ):
            l1 = t[x-1].lower()
            l2 = t[x-2].lower()
            l3 = t[x-3].lower()
            l4 = t[x-4].lower()
            l5 = t[x-5].lower()
            l6 = t[x-6].lower()            
        if ( x > 6 ): l7 = t[x-7].lower()
        if ( x > 7 ): l8 = t[x-8].lower()
        if(l6+l5+l4+l3+l2+l1+r=="<script"):fn1=1
        if (fn1 and (r==">")):fn2 = 1; fn1=0
        elif (l8+l7+l6+l5+l4+l3+l2+l1+r=="</script>"):fn2=0
        x+=1
    return(t1)

def rmvrepeat(t):
    x = t1 = ""
    global rpc
    for y in t:
        if not( (y in rpc) and (x==y)):t1+=y
        x = y
    return t1    
def equalmark(t):
    c = t1= ""
    for x in t:
        if(c+x!="= "):
            if (c+x==" ="):t1 = t1[0:len(t1)-1]
            t1+=x
        c = x
    return t1

def semicolan(t):
    global skbfsm,rmafsc
    t1=t2=t3=c=""
    for x in t:
        if((c in skbfsm) and (x in rmafsc)):continue
        t1+=x
        c = x
    c = fn1=fn2=""
    a1=a2=a3=a4=a5=a6=a7=nme1 = ""
    nmc = 0
    for y in t1:
        xz = " "
        if (c+y=="={"):fn1 = 1
        if (fn1 and y==":"):fn2 = 1;
        if (fn2 and y=="}"):xz=";";fn1=fn2=0        






  








    