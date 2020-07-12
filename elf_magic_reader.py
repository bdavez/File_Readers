import os

name = input("Please enter a filez name: ")

filez = open(name,"rb")

print("filez Name : {}".format(os.path.basename(name)))
print("Magic: ",end="")
for x in range (0,4):
    magic = filez.read(1).hex()
    print(magic,end=' ')

print("")

formats = filez.read(1).hex()

if formats == '01':
    print("Format: 32 bit")
elif formats == '02':
    print("Format: 64 bit")
else: 
    print("Format: Cannot be determined")

endian = filez.read(1).hex()

if endian == '01':
    print("Endian: little")
elif endian == '02':
    print("Endian: Big")
else:
    print("Endian: Undetermined")

seek = int(0x12) # converts hex to decimal
filez.seek(seek) # seeks to hex 0x12
machine = filez.read(2).hex() #According to Wikipedia, the e_machine is 2 bytes big

if machine == '0000':
    print("Machine: No specific instruction set")
elif machine == '0200':
    print("Machine: SPARC")
elif machine == '0300':
    print("Machine: x86")
elif machine == '0800':
    print("Machine: MIPS")
elif machine == '1400':
    print("Machine: PowerPC")
elif machine == '1600':
    print("Machine: S390")
elif machine == '2800':
    print("Machine: ARM")
elif machine == '2A00':
    print("Machine: SuperH")
elif machine == '3200':
    print("Machine: IA-64")
elif machine == '3e00':
    print("Machine: amd64")
elif machine == 'b700':
    print("Machine: AArch64")
elif machine == 'f300':
    print("Machine: RISC-V")
else: 
    print("Machine: Could not be determined")

