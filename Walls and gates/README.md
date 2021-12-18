# Practice-Question-REPL

We have a m x n 2D grid initialized with three possible values:
-1 - An obstacle.
0 - An exit.
INF - An empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to an exit is less than 2147483647.

We want to fill each empty room with the distance to its nearest exit. If it is impossible to reach an exit, it should be filled with INF.
<pre>
Example:
Given the 2D grid:

INF -1 0 INF
INF INF INF -1
INF -1 INF -1
0 -1 INF INF

We expect the output 2D grid as:

3 -1 0 1
2 2 1 -1
1 -1 2 -1
0 -1 3 4

