# Path finding on a 2D map

Homework described under: https://moodle.taltech.ee/mod/assign/view.php?id=622030

Search algorythms are implemented under /search_algs and are placed in separate files. 
Additional functions are available within the funcs.py file. Cave maps are created and prepared in the maps.py file. 

A short comparison of search algorythms in scope of this homework is made within measuring_exec.py file. 
Feel free to run it directly. 

The output should look something like this:

The dimond is located at (13, 1) found in 962 iterations.
time elapsed in bfs_search: 0.001178800011985004
The dimond is located at (13, 1) found in 554 iterations.
time elapsed in bfs_search: 0.0007761000015307218
The dimond is located at (257, 295) found in 167385 iterations.
time elapsed in bfs_search: 0.8531680000014603
The dimond is located at (595, 598) found in 700943 iterations.
time elapsed in bfs_search: 6.644246700016083
The dimond is located at (895, 898) found in 1598634 iterations.
time elapsed in bfs_search: 21.888129700004356
The dimond is located at (13, 1) found in 71 iterations.
time elapsed in greedy_search: 0.00021169998217374086
The dimond is located at (13, 1) found in 147 iterations.
time elapsed in greedy_search: 0.0002986000035889447
The dimond is located at (257, 295) found in 8096 iterations.
time elapsed in greedy_search: 0.04971629998181015
The dimond is located at (595, 598) found in 38204 iterations.
time elapsed in greedy_search: 0.39806410000892356
The dimond is located at (895, 898) found in 44306 iterations.
time elapsed in greedy_search: 0.6660502999729943
The dimond is located at (13, 1) found in 175 iterations.
time elapsed in astar_search: 0.0003404000017326325
The dimond is located at (13, 1) found in 337 iterations.
time elapsed in astar_search: 0.0005694999999832362
The dimond is located at (257, 295) found in 29674 iterations.
time elapsed in astar_search: 0.16296539999893866
The dimond is located at (595, 598) found in 215070 iterations.
time elapsed in astar_search: 2.227946200000588
The dimond is located at (895, 898) found in 335830 iterations.
time elapsed in astar_search: 4.811136600008467

Overall path lengths seem optimal for BFS and A* search algorythms with the later being much quicker. 
Greedy search fails to find the most optimal path, but does render its solution quicker than the other two algorythms.   
