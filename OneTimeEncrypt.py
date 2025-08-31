import random

print("Input the file you would like to be encrypted") 
inputfile = input()
key = random.randint(0,100)

def OneTimePad():

    with open (inputfile, "r") as file:
        content = file.read()

        for char in content:

            with open ("keyfile.txt","w") as file:
                file.write(str(key))

                enc = ord(char)^ord(str(key))

                with open("encfile.txt", "w") as file:
                    file.write(ord(str(enc)))




OneTimePad()
             
#NOTES: XOR is an operation that computes different bases, python produces base 10 decimals 
#when XOR-ing ASCII characters

#XOR strings by converting them to ascii using ord() 
      

#Encryption.encrypt()

#enc = Encryption(u)
   # def decrypt(self):
    #def decrypt(self):
