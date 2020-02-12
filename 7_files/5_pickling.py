# pickle - сериализация/десериализация объектов python
import pickle


class Tasker:
    def __init__(self, name):
        self._name = name
        self.tasks = ['go to gym', 'feed the cat', 'learn python']

    def greet(self):
        print(f'hello, {self._name}, your tasks for now: {";".join(self.tasks)}')


vasya = Tasker('Vasya')
vasya.greet()

with open('vasya.pickle', 'wb') as f:
    pickle.dump(vasya, f, pickle.HIGHEST_PROTOCOL)


with open('vasya.pickle', 'rb') as f:
    content = f.read()
    print(content)

new_vasya = pickle.loads(content)
new_vasya.greet()

assert new_vasya is not vasya
