mystr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def str_replace(str):
    abet = "abcdefghijklmnopqrstuvwxyz"
    newstr = ""
    for i in range(0,len(str)):
        if str[i] not in abet:
            newstr += str[i]
        else:
            abet_index = abet.find(str[i])
            newstr += abet[(abet_index + 2) % len(abet)]
    return newstr

print str_replace(mystr)
