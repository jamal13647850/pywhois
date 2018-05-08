import re
import whois

domain = input("Please enter your domain: ")
matchObj = \
    re.match(r'(?:http|https):\/\/((?:[\w-]+)(?:\.[\w-]+)+)(?:[\w.,@?^=%&amp;:\/~+#-]*[\w@?^=%&amp;\/~+#-])?',
             domain, re.I)
if matchObj:
    w = whois.whois(domain)
    print(w)
else:
    print("Your domain is not valid!")

'''look'''
