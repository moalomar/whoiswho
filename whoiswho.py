import json, os


DIRPATH = os.path.dirname(os.path.abspath(__file__))
ORIGINAL = os.path.join(DIRPATH, 'original.json')
DELETED = os.path.join(DIRPATH, 'changes.deleted.json')
ADDED = os.path.join(DIRPATH, 'changes.added.json')


def scan():
    items = set()
    for dirpath, _, filenames in os.walk('/'):
        for filename in filenames:
            items.add(os.path.join(dirpath, filename))
        if not filenames:
            items.add(dirpath)
    return items


def set_orginal():
    current = scan()
    with open(ORIGINAL, 'w', encoding='utf-8') as file:
        json.dump(list(current), file, indent=4)


def get_changes():
    current = scan()
    with open(ORIGINAL, 'r', encoding='utf-8') as file:
        original = set(json.load(file))
    deleted = original - current
    with open(DELETED, 'w', encoding='utf-8') as file:
        json.dump(list(deleted), file, indent=4)
    added = current - original
    with open(ADDED, 'w', encoding='utf-8') as file:
        json.dump(list(added), file, indent=4)


if __name__ == '__main__':
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
