import os

#p = ''

def append(v, d, r=False, /):
    d = p + d
    if r == False:
        for f in os.listdir(d):
            fSplit = os.path.splitext(f)
            os.rename(d + fSplit[0] + fSplit[1], d + fSplit[0] + '-icon' + fSplit[1])

def enum(d, r=False, ext='.jpg', /):
    d = p + d
    if r == False:
        i = 1
        for f in os.listdir(p):
            f = os.path.splitext(f)
            if f[1] == ext:
                os.rename(p + '\\' + f[0] + f[1], p + '\\' + str(i) + f[1])
                i += 1
    else:
        for d, sds, fs in os.walk(p):
            i = 1
            for f in fs:
                f = os.path.splitext(f)
                if f[1] == ext:
                    os.rename(d + '\\' + f[0] + f[1], d + '\\' + str(i) + f[1])
                    i += 1

def prepend(v, d, r=False, /):
    d = p + d
    if r == False:
        for f in os.listdir(d):
            fSplit = os.path.splitext(f)
            os.rename(d + fSplit[0] + fSplit[1], d + 'n-' + fSplit[0] + fSplit[1])

def shift(v, d, r=False, /):
    d = p + d
    if r == False:
        for f in os.listdir(d):
            fSplit = os.path.splitext(f)
            os.rename(d + fSplit[0] + fSplit[1], d + fSplit[0][5:] + fSplit[1])
