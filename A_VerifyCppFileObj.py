#!/usr/bin/python
# -*- coding: utf-8 -*-
#python 2.7.10
#加密解密过程
import sys, getopt, os, fileinput
import json, re, binascii
import hashlib
import datetime
import base64
import sys
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from pprint import pprint


def read_file_object(filePath):
   file = open(filePath, "r")
   text = file.read()
   #print (text)
   file.close()
   return text

def splitString(strBegin, strEnd, content):
	result = ""
	indexBegin = content.find(strBegin, 0)
   	indexEnd = content.find(strEnd, 0)
   	result = content[indexBegin+len(strBegin) : indexEnd]
   	result = result.replace(" ", "")
   	result = result.replace("\n", "")
   	result = result.replace("\r", "")
   	result = result.replace("\"", "")
   	print result
   	print len(result)
	return result

def generate_hash(contentStr):
    h = hashlib.md5()
    h.update(str(contentStr).encode('utf8'))
    return h.hexdigest()
 
def main(argv):
   print "ooooooo"
   print argv
   filePath = argv[0]
   content = read_file_object(filePath)

   if(content.find("//hash =") and content.find("//signature =")):
   		strBegin = "//hash ="
   		strEnd = "//signature ="
   		hashFromFile = splitString(strBegin, strEnd, content)
   		
   		strBegin = "//signature ="
   		strEnd = "//begin<"
   		signatureFromFile = splitString(strBegin, strEnd, content)
   		signatureFromFile = signatureFromFile.decode('hex')

   if(content.find("//begin<") and content.find("//>end")):
   		strBegin = "//begin<"
   		strEnd = "//>end"
   		indexBegin = content.find(strBegin, 0)
   		indexEnd = content.find(strEnd, 0)
   		content = content[indexBegin+len(strBegin) : indexEnd]
   		hashStr = generate_hash(content)

   if hashStr == hashFromFile:
      print "hash matches"
   else:
      print False 

#generate privateKey publicKey
   random_generator = Random.new().read
   rsa = RSA.generate(1024, random_generator)
   privkey = rsa.exportKey()
   print privkey
   print len(privkey)
   with open('master-private.pem', 'w') as f:
   		f.write(privkey)

   pubkey = rsa.publickey().exportKey()
   print pubkey
   print len(pubkey)
   with open('master-public.pem', 'w') as f:
   		f.write(pubkey)

#Master use the privateKey for signing 
   with open('master-private.pem') as f:
   		key = f.read()
   		rsakey = RSA.importKey(key)
   		signer = Signature_pkcs1_v1_5.new(rsakey)
   		digest = SHA.new()
   		digest.update(content)
   		sign = signer.sign(digest)
   		signature = base64.b64encode(sign)
   		signature = binascii.b2a_hex(signature.encode("utf8"))
   		print "----signature hex--"
   		print signature
   		#a5hK9mUNcAS/Mv/D7hYHAGjuR6oJiv+KQgRHmMDEBE5Dmp4eUEYL6Jyo+JMVkxoHSusdDcFdlSEI2GywW0ym7AtZzP4w0w1z/J52GIMgnCJrnsOaUAhbwDXdfu89qzJGSIc5n0oZmq9qGCVnxoMEenV7ZZYIztMs8llZRNyf8IY=

#Ghost use Master's publicKey for verifying signature
   with open('master-public.pem') as f:
   		key = f.read()
   		rsakey = RSA.importKey(key)
   		verifier = Signature_pkcs1_v1_5.new(rsakey)
   		digest = SHA.new()
   		digest.update(content)
   		is_verify = verifier.verify(digest, base64.b64decode(signature.decode('hex')))
   		print is_verify
   if is_verify:
      	print "signature matches"
   else:
      	print "signature does not match"



if __name__ == "__main__":
   default_encoding = 'utf-8'
   if sys.getdefaultencoding() != default_encoding:
		reload(sys)
		sys.setdefaultencoding(default_encoding)

   main(sys.argv[1:])



