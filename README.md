# MiniMotorwaysSolver - Material

Project undertaken as a part of WnCC SoC '22 to create a solver for the game "Mini Motorways".

---

## **Week 0 : Getting started with Git!**

### *Resources*

1. Git

    Go through one of the first two links, shouldn't take more than an hour. Make sure you cover atleast add, commit, push, pull, status, config and branch. The third link is a good animation of Git workflow. Last two links are just for referring syntax.

    - This video is all you need to get along with Git ...atleast it's basics : <https://youtu.be/8JJ101D3knE>
    - In case you're more of a reader follow this : <https://www.w3schools.com/git/>
    - This is also a small playlist which will help you understand some advanced git concepts like Merging, Rebasing, Git Flow : <https://www.youtube.com/playlist?list=PLqTmkYd8_EoJM77eZDFHAS-2Z2rxEmyOP>
    - Official Git docs (Cover everything here before the weekend, ||Just kidding :0||) : <https://git-scm.com/docs>
    - Git cheat-sheet for quick reference : <https://training.github.com/downloads/github-git-cheat-sheet.pdf>

2. GitHub

    - Cover from GitHub GET STARTED upto GitHub SEND PULL REQUEST : <https://www.w3schools.com/git/git_remote_getstarted.asp?remote=github>

### *Assignment*

1. First things first, configure git with your name and email id. We recommend using Visual Studio Code (VSC) editor and config it as your default editor.
2. (Optional cool commit messages) Append these lines at the end of your ~/.gitconfig file.

    ```bash
    [alias]
        cap = "!f() { git add .; git commit -m "$@"; git push; }; f"
        new = "!f() { git commit -m "📦 NEW: $@"; }; f"        # NEW.
        imp = "!f() { git commit -m "👌 IMPROVE: $@"; }; f"    # IMPROVE.
        fix = "!f() { git commit -m "🐛 FIX: $@"; }; f"        # FIX.
        rlz = "!f() { git commit -m "🚀 RELEASE: $@"; }; f"    # RELEASE.
        doc = "!f() { git commit -m "📖 DOC: $@"; }; f"        # DOC.
        tst = "!f() { git commit -m "✅ TEST: $@"; }; f"    # TEST.
        publish = "!git push origin $(git branch --show-current)"
    ```

3. You have to now fork the project repository and clone it to your local system. Checkout the material branch and copy this week's resources message to the README.md file. Add, commit and push those changes to the material branch of your fork. Finally create a pull request from your fork's material branch to the main repo's material branch.
Repo link : <https://github.com/adityakadoo/MiniMotorwaysSolver>

---

## **Week 1 : hello_world.py**

### *Resources*

1. w3schools: <https://www.w3schools.com/python/>

2. YouTube playlist: <https://youtube.com/playlist?list=PLzMcBGfZo4-mFu00qxl0a67RhjjZj3jXm>

Make sure to cover:-

- Data types: string, list, tuple, dictionary and set
- New operators like x**y, x //y, list slicing, etc.
- If-elif-else statement
- for and while loops
- Iterators like range() and enumerate()
- Functions definitions
- Classes and Objects in Python
- Importing and working with basic libraries such as math, random, time and datetime

### *Assignment*

This week's assignment: <https://codeforces.com/contest/1674>
It has 7 questions in total but you need to do as many as you can. Challenge is to write the smallest possible codes in python. Attempt problems alphabetically(beware of E) and in case you are stuck, move on to the next question. You can try submitting your solutions on codeforces by selecting Python 3.8 as the compiler.

---

## **Week 2: Graphs**

### *Resources*

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

### *Assignment*

In this week's assignment we will explore what every car does in the game to reach it's destination.

More formally, let's say we are given a road layout, followed by a bunch of queries representing car journeys. For now we can assume only one car travels at a time. We need to understand the behaviour of the cars while choosing their paths.

While traveling, a car might try to minimize the total distance travelled or the total time of the journey (Can there be some other parameter?). But since there is no other traffic, we can assume that the speed of the car will remain constant throughout the journey. This means minimizing the time is same as minimizing the distance!

So to minimise the distance travelled, we go over 2 strategies for finding out the shortest possible path that a car can take from it's source to it's destination. Each strategy has 2 steps:

1. Model the given road layout as a graph.
2. For every journey, given by a source and a destination, get the shortest path.

- **Strategy Uno**:

    *Task 0*: For step 1, we simply assign a node to every cell on the road layout, which has at least 1 road connecting to it. Then we add a bidirectional edge for every unit road connecting two neighbouring cells.

    *Task 1*: For step 2, we implement BFS algorithm to find the path with least number of edges from the given source to the given destination.

- **Strategy Dos**:

    *Task 2*: For step 1, we use DFS algorithm cleverly to reduce the number of nodes and edges in the graph. We do this by assigning nodes to every cell with exactly 1 OR at least 3 roads connecting to it. Now for all the direct paths(should not pass through any other node) connecting a pair of nodes(as defined before), we add an edge with weight equal to the length of the path. Note that here we will also have to store all the cells making up the direct path within the edge.

    *Task 3*: For step 2, we have a weighted graph. Using this weighted graph we must implement the infamous Dijkstras algorithm for finding shortest path for graphs with edge weigths.
