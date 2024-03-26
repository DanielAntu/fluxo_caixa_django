import re

regex = r'^[0-9]+([,][0-9]{1,2}?$)'

test_string = ['123', '123.45', '123,45', '123,456', '123,4', 'abc', '123abc', '12.34.56']

for test in test_string:
    match = re.match(regex, test)
    if match:
        print(f'a expressão {test} deu match')
    else:
        print(f'a expressão {test} não deu match')