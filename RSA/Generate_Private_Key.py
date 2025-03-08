from Crypto.PublicKey import RSA

from Crypto.Util.number import inverse

import base64

# n=p*q, where p and q are the factor of n
n =188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059

# p is a co-prime number of n
p=398075086424064937397125500550386491199064362342526708406385189575946388957261768583317

# q is a co-prime number of n
q=472772146107435302536223071973048224632914695302097116459852171130520711256363590397527

# e is a exponent of n
e =65537

# phi is φ(n) = (p - 1) * (q - 1)
phi = (p - 1) * (q - 1)

# d is the inverse of e mod phi
d = inverse(e, phi)

# Generating a private key
key = RSA.construct((n, e, d, p, q))

# file name
fn = "privatekey.pem"

# Storing key in a file
with open(fn, "wb") as f:
    f.write(key.exportKey())
