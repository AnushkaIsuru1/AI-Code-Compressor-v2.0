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













        


















  








    