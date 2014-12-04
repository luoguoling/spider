#coding:utf-8
__author__ = 'rolin'
import rsa
#生成密钥为pem格式
(pubkey,privkey) = rsa.newkeys(1024)
pub = pubkey.save_pkcs1()
print 'pub is %s',pub
pubfile = open('public.pem','w+')
pubfile.write(pub)
pubfile.close()

pri = privkey.save_pkcs1()
prifile = open('private.pem','w+')
prifile.write(pri)
prifile.close()

#load公钥和私钥
message = 'helloiwriwrewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwiwreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeew'
with open('public.pem') as publicfile:
    p = publicfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(p)
with open('private.pem') as privatefile:
    p = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p)

#用公钥加密，在用私钥解密
crypto = rsa.encrypt(message,pubkey)
print type(crypto)
print 'crypto is ',crypto
message = rsa.decrypt(crypto,privkey)
print message


#sign用私钥签名，在用公钥验证签名
#signature = rsa.sign(message,privkey,'SHA-1')
#rsa.verify('hello',signature,pubkey)
