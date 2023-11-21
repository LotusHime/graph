from collections import deque

graph = dict()

graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ['rustam']


graph["bob"] = ["anuj", "peggy"]

graph["alice"] = ["peggy"]

graph["claire"] = ["thom", "jonny"]

graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(graph)
print(graph["you"])

search_queue = deque()
search_queue += graph['you']


print(search_queue)


def person_is_seller(name): # функция проверяет заканчивается ли имя на определенную букву
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(
                    f'\n{person.title()} is a mango seller!')  # Условие выполняется верно-> это продавец, выводит на консоль
            else:
                search_queue += graph[person]
                searched.append(person)

search('you')

