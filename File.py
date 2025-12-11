try:
    file = open("info.txt", "r")
    content = file.read()
    print("File Content:\n", content[109])
    file.close()

except Exception as TyagiG:
    print(TyagiG)