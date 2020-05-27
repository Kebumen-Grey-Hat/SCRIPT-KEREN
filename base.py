from base64 import b64encode
import os

os.system("python tam.py")
r = raw_input("\033[92mMasukan Text: \033[0m")

fo = b64encode(r)

print "[+] RESULT => {}".format(fo)
