str3 = ':'.join(["first", "second", "third"])
print(str3)

str4 = "HHHabcdHHH"
print(str4.strip("H"))

str5 = "Hello World"
print(str5.split())

str6 = str5.replace("l", "LL")
print(str6)

print(str6.find("L"))
print(str6.find("l"))

str_format = "This is value {} and this is value {}"

print(str_format.format(5, "six"))