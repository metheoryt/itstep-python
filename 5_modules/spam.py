
MODULE_GLOBAL_VAR = []


def hello_from(where=None):
    if not where:
        where = __name__
    print(f'hello from {where}')


hello_from()


if __name__ == '__main__':
    print('this is a spam module')
    print('it only contains a few useful functions')
