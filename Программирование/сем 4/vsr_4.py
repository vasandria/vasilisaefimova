import json
import unittest


class NameTestCase(unittest.TestCase):
    def test_json(self):

        try:
            open('users.json')
        except FileNotFoundError:
            print("FileNotFound")

    if __name__ == "__main__":
        unittest.main()


def create_string(elem):
    n = 0
    for i in elem:
        elem[n] = str(i)
        n += 1
    return elem


with open('users.json') as table:
    t = json.load(table)
    table.close()

keys = create_string(list(dict.keys(t)))
values = create_string(list(dict.values(t)))

n = 0
print('------------------------------')
for i in dict.keys(t):
    print(f'| {keys[n].center(10)} | {values[n].center(10)} |')
    n += 1
    print('------------------------------')

