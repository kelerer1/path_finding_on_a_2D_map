#%%
from search_algs.astar_search import astar_search
from search_algs.greedy_search import greedy_search
from search_algs.bfs_search import bfs_search
from maps import *
from funcs import find_character_position


#%%
maps = [lava_map1, lava_map2, map_300x300, map_600x600, map_900x900]
funcs = [bfs_search, greedy_search, astar_search]


if __name__ == '__main__':
    result = []
    for func in funcs:
        path_lengths = []
        for cave in maps:
            path_to_diamond, _ = func(cave, find_character_position(cave, 's'))
            print(len(path_to_diamond))
            path_lengths.append(len(path_to_diamond))
        result.append(path_lengths)
