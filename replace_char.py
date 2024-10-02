import re

with open('test/C1HKVI01_T_N.txt', 'r+') as file:
    content = file.read()
    new_content = re.sub(r'�', '', content)
    file.seek(0)
    file.write(new_content)