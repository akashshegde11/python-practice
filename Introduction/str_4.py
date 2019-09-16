# Use of escape sequences

String1 = '''Hello World'''
print("Initial String using triple quotes: ", end='')
print(String1)

String2 = 'I\'m a "Geek"'
print("Escaping Single Quotes: ", end='')
print(String2)

String3 = "I'm a \"Geek\""
print("Escaping Double Quotes: ", end='')
print(String3)

String4 = "C:\\Python\\Geeks\\"
print("Escaping backslashes: ", end='')
print(String4)

String5 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("Printing in HEX with the use of Escape Sequences: ", end='')
print(String5)

String6 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("Printing Raw String in HEX Format: ", end='')
print(String6)
