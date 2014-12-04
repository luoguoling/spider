import rsa
with open('private.pem') as privatefile:
    p = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p)
crypto = raw_input('please input')
message = rsa.decrypt(crypto,privkey)
    


