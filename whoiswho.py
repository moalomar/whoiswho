import os, json


def scan():
    content = []
    for dirpath, _, filenames in os.walk('/'):
        for filename in filenames:
            content.append(os.path.join(dirpath, filename))
        if not filenames:
            content.append(dirpath)
    return content


def set_orginal():
    with open('original.json', 'w', encoding='utf-8') as file:
        json.dump(scan(), file, indent=4)


def get_changes():
    current = scan()
    with open('original.json', 'r', encoding='utf-8') as file:
        original = json.load(file)
    deleted = []
    for item in original:
        if item not in current:
            deleted.append(item)
    with open('changes.deleted.json', 'w', encoding='utf-8') as file:
        json.dump(deleted, file, indent=4)
    added = []
    for item in current:
        if item not in original:
            added.append(item)
    with open('changes.added.json', 'w', encoding='utf-8') as file:
        json.dump(added, file, indent=4)


print()
print('    WHO IS WHO?!')
print()
print('[1] SET ORIGINAL')
print('[2] GET CHANGES')
while True:
    option = input('\nOPTION? ')
    if option not in ('1', '2'):
        break
    print('PROCESSING ...')
    if option == '1':
        set_orginal()
    if option == '2':
        get_changes()
    print('DONE')
