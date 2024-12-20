name="Tabish Shah Mohsin"
for i in range(len(name)):
    if name[i]=="a":
        name=name[:i]+"e"+name[i+1:]
    elif name[i]=="e":
        name=name[:i]+"i"+name[i+1:] 
    elif name[i]=="i":
        name=name[:i]+"o"+name[i+1:] 
    elif name[i]=="o":
        name=name[:i]+"u"+name[i+1:] 
    elif name[i]=="u":
        name=name[:i]+"a"+name[i+1:] 
print(name)