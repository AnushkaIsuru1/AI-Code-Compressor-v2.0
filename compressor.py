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









        


















  








    