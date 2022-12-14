#!/usr/bin/python3

from common import *

e1 = b"""Rb%P^-k=8]Jfb^@.q(/n"=-Q!prH_q53 HSa:.5fOLPJ3P-O3Qh?%8#K[cAQI\\5:>%94g+jX$j3g$SIKphV_oq/0L?>,AY<-`KP"""
w1 = b"""pb%P^-k=8]Jfb^@.q(/n"=-Q!=+>Tq53 9:V4.5fOLPJ3P-O3QL:[m`Ko<h`!>i7c&A9`qdN1D-15d-)NcYB^r/*i^"+ahEL*Kd^)B2"""
e2 = b"""Db%P^-k=8]Jfb^@.q(/n"=-Q!elT)Pbp6`YHQn#0X3OHp&-`=Q`_&Q?-0*M8:m*\\q]BVf5/$bmJE>6 +IhY47YaI72hJ%#:n(%VMm9`]0LVS4_9+:MU\\FB"""
w2 = b"""lb%QkVeN@!J\\:PRp@8W]O,5,QVB9D/XW4)(^-r)L=\\UrJp%Kg#pmOnB9^2*Q^`Tq+b^-O1Tf:7@?`7C@R&!9(EOK:ladp1'M_.U_\\0"""
e3 = b"""_b%QkV"\\=HnO\\kcg\\"a'O.Mj[Ip-\\-q6CRHG"[P?l"pk!Xc+5(HaMkWG\\J-#6Y"&Z)f!ZX_d9o'43`"bi>g0,>aE4-6_2N`[Iqr6nDO1$&1%Do_!`e/K$ZX?.`Z2Lne! N4gi9C(8"""
w3 = b"""Bb%QkV7j+-<:3PcYE\\B<j*1@+23K3qJ$^)NQ@SlZ$KO1co5@L0>E:<IdYBS*ef(&NK2GOK/-A>C^E E%FWE-H9)5+`%oJd+g+P#c]H6.CR]G+"bQSU1iDkjV8>Vf"""
e4 = b""";b%QkV"\\=H"W)/[2d#D%OmLF!2<l$B\\_Zp1VokPVW3^`.OSfk%+OMZdeo9FMiOdRBMn:oY$X6\\2kK\\[c_JQAHaom'#:^?n:YeH$7:-cJFh+Ga\\9&pbdm[n3"""
w4 = b"""mb%QkV"\\=H"W)/[2d#D%O\\5p!hW0rCY3!b2;G1jqG.n 9aKb`Fq78RY>gk:dVYXRgi.5(@:_%E3KbOUBb7i?VFmc+_o&65Sej5%1cE=5\\.rL>$4JC!?VN4H>"""
e5 = b"""Ab%QkV"\\=H"W)/[2d#D%OA5[L2<l[B\\_o;,V%QPVWT^he*Y6ZPcU'B@>?3:(BN'>gWBkV)&\\%79MJp9,6l4S^5H)I*Li(Afi&?5h%H]SJb`j]9_J8I"""

messages = [e1, w1, e2, w2, e3, w3, e4, w4, e5]
messages_bytes = [bytes([x - READABLE_OFFSET for x in m]) for m in messages]

if __name__ == "__main__":
    for m in messages:
        print(m.decode())
