import heapq


# needed for both parts
# dijkstra algorithm from https://en.wikipedia.org/wiki/Dijkstra's_algorithm
# for part two it takes a few minutes: probably bad implementation of dijkstra from my side
def get_distance(graph, target_id):
    dist = dict()
    que_list = [True] * len(graph.keys())  # mark nodes
    que_item_count = len(graph.keys())
    priority_que = list()  # use priority-que to decrease lookup time for minimum

    dist[0] = 0 # source node

    for vid, edge_list in graph.items():
        if vid != 0:
            dist[vid] = 10e10  # set distance to infinity

        heapq.heappush(priority_que, (dist[vid], vid))  # build heap

    while que_item_count != 0:
        if que_item_count % 500 == 0:
            # cleanup priority queue every 500 steps
            priority_que = [p for p in priority_que if p[1] != 10e10]
            heapq.heapify(priority_que)

        # get node with shortest distance and remove from queues.
        min_dist, min_id = heapq.heappop(priority_que)
        que_list[int(min_id)] = False
        que_item_count -= 1

        if min_id == target_id:
            # shorted path for target node is known -> abort
            break

        for neighbor in graph[min_id]:
            nid = neighbor["id"]
            if que_list[nid]:
                alt = min_dist + neighbor["weight"]
                if alt < dist[nid]:
                    dist[nid] = alt
                    # update value for priority queue
                    for i in range(len(priority_que)):
                        if priority_que[i][1] == nid:
                            priority_que[i] = (10e10, 10e10) # invalidate entry in priority_que (you cant remove elements)
                            heapq.heappush(priority_que, (alt, nid)) # reinsert node with updated distance
                            break

    return dist[target_id]  # target distance


# needed for both parts
# creates the weighted graph from the input
# costs to enter a field are represented as a weighted edge
def create_graph(array):
    graph = dict()
    length = len(array)
    for y in range(length):
        for x in range(length):
            node_id = y * length + x
            neighbors = list()
            if x > 0:
                # connect with previous node
                neighbors.append({"id": y * length + x - 1, "weight": int(array[y][x - 1])})
                # add back edge
                graph[y * length + x - 1].append({"id": y * length + x, "weight": int(array[y][x])})

            if y > 0:
                # connect with previous node
                neighbors.append({"id": (y - 1) * length + x, "weight": int(array[y - 1][x])})
                # add back edge
                graph[(y - 1) * length + x].append({"id": y * length + x, "weight": int(array[y][x])})

            graph[node_id] = neighbors

    return graph


# create array for part 1 and part 2
lines = open('input.txt', 'r').readlines()
length = len(lines)
array1 = [[0 for x in range(length)] for y in range(length)]
array2 = [[0 for x in range(5 * length)] for y in range(5 * length)]
for y in range(length):
    for x in range(length):
        array1[y][x] = int(lines[y][x])
        for i in range(5):
            for k in range(5):
                array2[y + i * length][x + k * length] = (int(lines[y][x]) + i+k - 1) % 9 + 1

print("Part 1:", get_distance(create_graph(array1), length**2 - 1))
print("Part 2:", get_distance(create_graph(array2), (5 * length)**2 - 1))
