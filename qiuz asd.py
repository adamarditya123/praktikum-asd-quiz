import re

#nomer 1
##username = '@adamarditya123’
##username = '@adamarditya123’
username = '@adamarditya123'
cocok = re.findall(r'@+[a-z]+[0-9]+\w', username)
if cocok:
    print(cocok ,'True') 
else:
    print('False')


#nomer 2
f = open('qiuz.txt')
teks = f.read()
f.close()
p = r'\w+@+[\w.-]+'
strings = re.findall(p,teks)
print(strings)

#nomer 3
class _SimpulPohonBiner(object):
    def __init__( self, data ):
        self.data = data
        self.kiri = None
        self.kanan = None

# Membuat simpul-simpul dan mengisi data
A = _SimpulPohonBiner('1')
B = _SimpulPohonBiner('2')
C = _SimpulPohonBiner('3')
D = _SimpulPohonBiner('4')
E = _SimpulPohonBiner('5')
F = _SimpulPohonBiner('6')
G = _SimpulPohonBiner('7')
H = _SimpulPohonBiner('8')
I = _SimpulPohonBiner('9')
J = _SimpulPohonBiner('10')

# Menghubungkan simpul ortu-anak
A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I
