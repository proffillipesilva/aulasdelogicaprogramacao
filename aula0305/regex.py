import re

email = "<p>Aloha</p>"
valido = re.search("^<p>(.*)</p>$", email )
print(valido.group(1))