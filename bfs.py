import collections
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return visited


graf = {}
liste = []
a, b = map(int, input().split(" "))
for j in range(1,a+1):
    liste.append(j)
    graf[j] = []
for i in range(b):
    num1, num2 = map(int, input().split(" "))
    graf[num1].append(num2)
    graf[num2].append(num1)
