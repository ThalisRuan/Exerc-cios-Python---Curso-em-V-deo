
cid = str(input("Em que cidade vc nasceu  "))
cidade1 = "Santos"
if cid == cidade1:
    print("Verdadeiro")
else:
    print("False")
    
cid = str(input('Em que cidade vc nasceu')).strip()
print(cid[:5].upper() == "Santos")

