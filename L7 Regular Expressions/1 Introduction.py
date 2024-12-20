# Regular expression, or regrexes
# To check the inputed values correspond to out expectations
# To check that the user entered a proper email



# Trying without regex
email=input("Enter E-Mail Address: ").strip()

domains=["gmail.com", "ymail.com", "hotmail.com", "rediffmail.com"]

alphanum={"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}



if email.count("@")==1 and email.endswith(".com"):
    username, domain = email.split("@")

    if (set(username)).issubset(alphanum) and domain in domains:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
    
