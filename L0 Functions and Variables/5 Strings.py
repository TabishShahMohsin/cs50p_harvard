#str stands for string
#Can see documentation
#if someone enters spaces accidently or capatalization is a bit off
name="   Tabish SHah"
t="  Some THing is GOOd.   "
name=name.strip()
name=name.capitalize() #makes the first char capital and others small
print(name)
name=name.title() #title capitalization
print(name)
t=t.strip().title()# Or do it directly
print(t)
print(input("Enter your name: ").strip().title())
#can use lsrtip() and rstrip() seperately as well
a, b=name.split(" ")
print(a)