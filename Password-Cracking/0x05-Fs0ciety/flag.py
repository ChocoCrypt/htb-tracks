import base64

with open("sshcreds_datacenter.txt" , "r") as fp:
    fucktext = fp.read()


not_b64fuck = str(base64.b64decode(fucktext))[2:-1]
bins = not_b64fuck.split(" ")
nums = [int(i,2) for i in bins]
chars = [chr(i) for i in nums]
flag = "HTB{"+"".join(chars)+ "}"
print(flag)
