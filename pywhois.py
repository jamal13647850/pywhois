import getopt
import re
import whois
import sys

domain = ''
argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "d:", ["domain="])
except getopt.GetoptError:
    print('python pywhois.py -d <domain> ')
    print('python pywhois.py --domain <domain> ')
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-d", "--domain"):
        domain = arg

if domain == '':
    domain = input("Please enter your domain: ")

matchObj = \
    re.match(r'(?:http|https):\/\/((?:[\w-]+)(?:\.[\w-]+)+)(?:[\w.,@?^=%&amp;:\/~+#-]*[\w@?^=%&amp;\/~+#-])?',
             domain, re.I)
if matchObj:
    w = whois.whois(domain)
    whereOut = input("Save to file or display on monitor? f/m ")
    if whereOut.lower() == "f" or whereOut.lower() == "file":
        filename = matchObj.group(1).replace(".", "") + ".txt"
        myfile = open(filename, 'w')
        myfile.write(w.text)
        myfile.close()
    else:
        print(w)
else:
    print("Your domain is not valid!")
