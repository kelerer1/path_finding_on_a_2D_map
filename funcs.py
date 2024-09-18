#%%

from queue import Queue, PriorityQueue


import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        original_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print("time elapsed in ", func.__name__, ": ", end - start, sep='')
        return original_return_val

    return wrapper


def find_map_dimensions(map_data: list) -> tuple:
    max_idx_length = len(map_data) - 1
    max_idx_width = max([len(x) for x in map_data]) - 1

    return max_idx_width, max_idx_length


def find_character_position(map_data: list, char: str) -> tuple:
    location = None
    for key, x in enumerate(map_data):
        try:
            position = x.find(char)
            if position > 0:
                location = (position, key)
        except ValueError:
            pass

    return location


def find_neighbours(current: tuple, map_data: list) -> list:

    dimensions: tuple = find_map_dimensions(map_data)

    left = (current[0] - 1, current[1])
    right = (current[0] + 1, current[1])
    up = (current[0], current[1] - 1)
    down = (current[0], current[1] + 1)

    neighbours = [left, right, up, down]
    neighbours = [x for x in neighbours if (0 <= x[0] <= dimensions[0]) & (0 <= x[1] <= dimensions[1])]

    return [x for x in neighbours if map_data[x[1]][x[0]] != '*']


def mark_path_point(location: tuple, map_data: list, character) -> list:

    string_to_replace = map_data[location[1]]
    string_list = list(string_to_replace)
    string_list[location[0]] = character
    string_to_replace = ''.join(string_list)
    map_data[location[1]] = string_to_replace
    return map_data


def heuristic(node: tuple, goal: tuple) -> int:

    result = abs(node[1]-goal[1]) + abs(node[0]-goal[0])

    return result
