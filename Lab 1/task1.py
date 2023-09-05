from collections import defaultdict
from queue import PriorityQueue
inp = open("/content/input.txt", 'r')




def a_star(source):
  for key in heu:
    dist[key] = 100000

  dist[source] = 0

  fringe = PriorityQueue()

  fringe.put((heu[source], source))

  while not fringe.empty():
    pair = fringe.get()
    cost = pair[0]
    node = pair[1]

    for adj_pair in adj_lst[node]:
      adj_cost = adj_pair[0]
      adj_node = adj_pair[1]

      if cost + adj_cost + heu[adj_node] - heu[node] < dist[adj_node]:
        dist[adj_node] = cost + adj_cost + heu[adj_node] - heu[node]
        fringe.put((dist[adj_node], adj_node))
        parent[adj_node] = node




















adj_lst = defaultdict(list)
heu = dict()

for line in inp:
  lst = line.split()

  heu[lst[0]] = int(lst[1])
  for i in range(2, len(lst)-1, 2):
    adj_lst[lst[0]].append((int(lst[i+1]), lst[i]))


print(adj_lst)
print(heu)

start = input("Enter the starting point: ")
end = input("Enter the ending point: ")

parent = dict()
dist = dict()

a_star(start)

path = []

current = end
while current != start:
  path.append(current)
  current = parent[current]
path.append(start)

path.reverse()

print(path)
print(dist[end])

print(dist)

