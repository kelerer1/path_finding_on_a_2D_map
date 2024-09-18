from funcs import *


@timing_decorator
def greedy_search(map_data: list, start: tuple):

    goal = find_character_position(map_data, 'D')
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    diamond_location = None
    number_of_iterations = 0

    while not frontier.empty():
        _, current = frontier.get()

        if map_data[current[1]][current[0]] == 'D':
            diamond_location = current
            print(f'The dimond is located at {diamond_location} found in {number_of_iterations} iterations.')
            break

        for next_node in find_neighbours(current, map_data):
            number_of_iterations += 1
            if next_node not in came_from:
                priority = heuristic(next_node, goal)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    path_of_travel = []
    path_found = False
    came_from_node = came_from[diamond_location]
    while not path_found:

        if came_from_node != start:
            path_of_travel.append(came_from_node)
            map_data = mark_path_point(came_from_node, map_data, '.')
            came_from_node = came_from[came_from_node]

        else:
            path_found = True

    return path_of_travel, map_data


#%%
