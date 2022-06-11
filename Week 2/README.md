# **Week 2: Graphs**

## *Resources*

1. Introduction video for Graph: <https://www.simplilearn.com/tutorials/data-structure-tutorial/graphs-in-data-structure>

2. Brief revision on :
Stacks: <https://www.youtube.com/watch?v=77GDiGd1_UU>
Queues: <https://www.youtube.com/watch?v=Y7wZO2tMjnY>
Priority Queues: <https://www.youtube.com/watch?v=wptevk0bshY>

3. Abdul Bari's videos for :
Graph Traversal algorithms : DFS and BFS : <https://www.youtube.com/watch?v=pcKY4hjDrxk>
Dijkstra's Algorithm : <https://www.youtube.com/watch?v=XB4MIexjvY0>

    If you prefer to read instead of watching videos :
    <https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/>
    <https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/>

4. The attached book(CLRS-Introduction to Algorithms) is  also a good read on Dijkstra's algorithm but if you wanna read you can go through DFS and BFS too:
Dijkstra's algorithm pages : 658-662,
Breadth-First-Search: pages: 594-597,
Depth-First-Search: pages: 603-606.
<https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf>

## *Assignment*

This week's assignment will explore what every car does in the game to reach its destination.

More formally, let's say we are given a road layout, followed by a bunch of queries representing car journeys. For now, we can assume only one car travels at a time. We need to understand the behaviour of the cars while choosing their paths.

While travelling, a car might try to minimize the total distance travelled or the total time of the journey (Can there be some other parameter?). But since there is no other traffic, we can assume that the speed of the car will remain constant throughout the journey. This means minimizing the time is the same as minimizing the distance!

So to minimise the distance travelled, we go over 2 strategies for finding out the shortest possible path that a car can take from its source to its destination. Each strategy has 2 steps:

1. Model the given road layout as a graph.
2. For every journey, given by a source and a destination, get the shortest path.

- **Strategy Uno**:

    *Task 0*: For step 1, we simply assign a node to every cell on the road layout, which has at least 1 road connecting to it. Then we add a bidirectional edge for every unit road connecting two neighbouring cells.

    *Task 1*: For step 2, we implement the BFS algorithm to find the path with the least number of edges from the given source to the given destination.

- **Strategy Dos**:

    *Task 2*: For step 1, we use the DFS algorithm cleverly to reduce the number of nodes and edges in the graph. We do this by assigning nodes to every cell with precisely 1 OR at least 3 roads connecting to it. Now for all the direct paths(which should not pass through any other node) connecting a pair of nodes(as defined before), we add an edge with a weight equal to the length of the path. Note that here we will also have to store all the cells making up the direct path within the edge.

    *Task 3*: For step 2, we have a weighted graph. Using this weighted graph we must implement the infamous Dijkstra's algorithm for finding the shortest path for graphs with edge weights.

While implementing BFS, DFS and Dijkstra's algorithms you would need queue, stack and heap data structures respectively. To get these data structures in python, from the module queue you can use Queue as a queue, LifoQueue as a stack and PriorityQueue as a heap. Documentation for this module is at <https://docs.python.org/3/library/queue.html>
