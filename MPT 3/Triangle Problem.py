'''
A triangle of numbers
cost = current cost + number you're going to
get from top to bottom with least cost

(1)
9(5)
6(7)8
45(3)8
236(5)8
projcteuler 18, 67
'''


from queue import PriorityQueue

def heuristic(px, py):
    return abs(px[0]-py[0]) + abs(px[1]-py[1])

    def neighbors(self,point):
        py, px = point
        for y in (py-1,py,py+1):
            for x in (px-1,px,px+1):
                if (y,x) != point and \
                   0 <= y < self._size and \
                   0 <= x < self._size and \
                   self._grid[y][x]:
                    yield (y,x)

    def cost(self,px,py):
        return abs(complex(*px)-complex(*py))



def path(came_froms,point):
    while True:
        yield point
        try:
            point = came_froms[point]
        except KeyError:
            break


def search(start, goal, graph):
    frontier = PriorityQueue()
    frontier.put((0,start))
    came_from = {}
    cost_so_far = {}
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()


        if current == goal:
            print(''.join(graph._draw(set(path(came_from,current)))))
            return list(reversed(list(path(came_from,current))))

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((priority,next))
                came_from[next] = current

    return None






