import re


reg_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{5,8}$"

password = "RedColour3"

print(re.match(reg_pattern, password))
# re.match()