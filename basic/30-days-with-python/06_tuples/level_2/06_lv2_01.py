### 1. Unpack siblings and parents from family_members
siblings = ('Eduardo', 'Juan', 'Eduardo Jr', 'Marco', 'Eva', 'Delia', 'Camila', 'Constantine')

siblings = list(siblings)
print('siblings before unpack : ', siblings)
parents = tuple(siblings[6:])
brothers = tuple(siblings[:4])
sisters = tuple(siblings[4:6])
siblings = tuple(siblings)
print('parents : ', parents)
print('brothers : ', brothers)
print('sisters : ', sisters)
print('siblings after unpack : ', siblings)

""" output
siblings before unpack :  ['Eduardo', 'Juan', 'Eduardo Jr', 'Marco', 'Eva', 'Delia', 'Camila', 'Constantine']
parents :  ('Camila', 'Constantine')
brothers :  ('Eduardo', 'Juan', 'Eduardo Jr', 'Marco')
sisters :  ('Eva', 'Delia')
siblings after unpack :  ('Eduardo', 'Juan', 'Eduardo Jr', 'Marco', 'Eva', 'Delia', 'Camila', 'Constantine')
"""