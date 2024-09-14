from funcs import *


def my_bfs_search(map_data: list, start: tuple):

    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    diamond_location = None

    while not frontier.empty():
        current = frontier.get()

        if map_data[current[1]][current[0]] == 'D':
            diamond_location = current
            print(f'The dimond is located at {diamond_location}')
            break

        for next_node in find_neighbours(current, map_data):
            if next_node not in came_from:
                frontier.put(next_node)
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

path_to_diamond_lava_map1, result_lava_map1 = my_bfs_search(lava_map1, find_character_position(lava_map1, 's'))

path_to_diamond_lava_map2, result_lava_map2 = my_bfs_search(lava_map2, find_character_position(lava_map2, 's'))

path_to_diamond_300x300, result_300x300 = my_bfs_search(map_300x300, find_character_position(map_300x300, 's'))

path_to_diamond_600x300, result_600x600 = my_bfs_search(map_600x600, find_character_position(map_600x600, 's'))

path_to_diamond_900x900, result_900x900 = my_bfs_search(map_900x900, find_character_position(map_900x900, 's'))
