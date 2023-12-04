from PIL import Image
from numpy import asarray

a=131
p=263
pkey=9
y=(a**pkey)%p
print("Y Value is ",y)
#e4.insert(0,str(y))
print(p)
print(a)
print(pkey)
img = Image.open("test.jpg")
numpydata = asarray(img)
print(len(numpydata)*len(numpydata[0]))
k=1
fsk=[]
bp=[]
enc=[]
for row in numpydata:
    ec=[]
    for col in row:
        sk=(y**k)%p
        fsk.append(sk)
        d=(a**k)%p
        bp.append(d)
        ec.append(col^sk)
        k=k+1
        print(k)
    enc.append(ec)
print(fsk)

print(bp)

im=Image.fromarray(enc)
im.save('enc.jpg')

eimg = Image.open("enc.jpg")
edata = asarray(eimg)

sdk=[]

i=0
dec=[]
for row in edata:
    de=[]
    for col in row:
        sk=(bp[i]**pkey)%p
        sdk.append(sk)
        de.append(col^sk)
        i=i+1
    dec.append(de)


im=Image.fromarray(dec)
im.save('decr.jpg')



    



