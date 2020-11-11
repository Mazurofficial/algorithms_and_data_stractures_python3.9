from _collections import deque


def search(graph):
    graph_deque = deque()
    graph_deque += graph['you']
    searched = []
    while graph_deque:
        person = graph_deque.popleft()
        if person not in searched:
            if search_term(person):
                print(person + ' is found person')
                return True
            else:
                graph_deque += graph[person]
                searched.append(person)
    return print('Person not found')


def search_term(name):
    return name[-1] == 'm'


my_graph = {
    'you': ['alice', 'bobby', 'din'],
    'alice': ['claire', 'bob', 'gad'],
    'bobby': ['faire', 'jimmy', 'pug'],
    'din': ['pug'],
    'gad': ['bob'],
    'claire': [],
    'bob': [],
    'faire': ['gad'],
    'jimmy': ['bobby', 'you'],
    'pug': []
}
search(my_graph)
