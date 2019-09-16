# Formatting string outputs

String1 = "{} {} {}".format('Hello', ',', 'World')
print("Print String in default order: ", end='')
print(String1)

String2 = "{1} {0} {2}".format('Hello', ',', 'World')
print("Print String in Positional Order: ", end='')
print(String2)

String3 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("Print String in Order of Keywords: ", end='')
print(String3)

String4 = "{0:b}".format(16)
print("Binary representation of 16 is: ", end='')
print(String4)

String5 = "{0:e}".format(165.253)
print("Exponential representation of 165.253 is: ", end='')
print(String5)

String6 = "{0:.2f}".format(1/3)
print("One-third is: ", end='')
print(String6)

String7 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'For', 'Geeks')
print("Left, center and right alignment with formatting: ", end='')
print(String7)
