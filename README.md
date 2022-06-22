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

---

## **Week 3: Traffic Sciences**

### *Resources*

An incorrect assumption made last week was that only vertical or horizontal roads can be drawn. At that time there were a single kind of square cells that spanned the entire grid and these cells were connected 4 neighbouring cells.

But in the game there can also be diagonal roads. So every cell has 8 neighbours. Since each of this 8 directions behave identically, we model every cell as an octogon. This would create 2 kinds of cells as per the [octagon-square tesselation](https://geometricolor.files.wordpress.com/2012/06/einfach-octragonquadrat.jpg):

1. *Octagonal cells*: These cells replace the old square cells. They can be connected in all 8 directions. Each one of these cells has 4 octagon and 4 diamond neighbours.
2. *Diamond cells*: These cells are present at the corners of the old square cells. They are basically tilted squares that have 4 octagon neighbours.

This model is just an idea that I had while thinking about an 8-neighbourhood system. If you can think of a cleverer way to model the diagonal roads in the game, we would be happy to #discuss.

**Network Flow**: These are two videos to brief through what does Flow mean in graphs and algorithm for Maximizing the flow in a graph :

- Ford Fulkerson  : <https://www.youtube.com/watch?v=LdOnanfc5TM>
- Edmonds-Karp : <https://www.youtube.com/watch?v=RppuJYwlcI8>

You should also go through the texts given in this book on pages :
709-712  Flow Network
714-717 : Ford Fulkerson including residual networks
719 : Augmenting Paths
724-727 : Ford Fulkerson and Edmonds-Karp Algorithm

### *Assignment*

This week's assignment will go into how traffic works in the game. Last week we had assumed no other car will get in a car's while it's journey. Sadly this doesn't always happen in the game ||or irl :(||. So we will see how the cars change their behaviour when they encounter such conditions.

Good news is this week's assignment needs you to only play the game a few times and do experiments with the game. Whenever you see something interesting happen don't forget to pause and take screenshot.

Using the octagon-square tesselation model we will study different kinds of road structures that are present in the game as given bellow.

- Octagonal cell connected to a single neighbour (A dead end)

- Octagonal cell connected to 2 neighbours (A straight road or a simple turn with 3 possible angles)

- Octagonal cell connected to 3 or 4 neighbours (A crossroad)
    When multiple cars from different entry roads are in contention, which one goes first? Is it completely random? Does it depends on something?

- Octagonal cell connected to 5 or more neighbours (Generalise the simple crossroad case)

- Octagonal cell with a traffic lights (A signal)
    How does this change the overall behaviour compared to the case without traffic lights?

- Motorway connecting 2 octagonal cells (A flyover)
    Do the cars go faster on a motorway?

- Diamond cell connected to 2 neighbours (A diagonal road)

- Diamond cell connected to 3 or more neighbours (Another kind of crossroad)

- Roundabout connecting multiple cells (A classic roundabout)
    Which octagonal and diamond cells are involved in the roundabout because it seems to take more space than an octagonal cell?
    Which octagonal cells are neighbours to the roundabout?

For each of the above structure we must do the following tasks,

1. Identify all the distinct entry/exit roads in this structure. Label them as R1, R2, ... and so on.
2. Identify the paths that the cars take on entering from road Ri and exiting to road Rj for all possible pairs of i and j. Label these paths as P1, P2, ... and so on.
3. In case of a traffic jam, how many cars can get stuck on each of the paths P1, P2, ...? This could be determined by the actual length of that path and how many cars it can accommodate.
4. Find out all the sets of paths S1, S2, ..., where all the paths in a particular set Si can operate simultaneously. Meaning if there is a car on each of these paths, they won't have to wait for others.
5. Now with all this information from previous parts, lets say we want to model this road structure as a directed graph G where every entry/exit point is already assigned a vertex. You can either add vertices or directed edges to G. Goal is to get a G such that it has a set of edges that connect and model each one of the paths P1, P2, ... and so on.
6. Now to each edge we need to assign a weight so that it represents it's length. Another check could be that for every path Pi, the sum of weights on the edges in G making up Pi must be equal to the number of cars that can block Pi as found in (3).
7. Lastly, make sure that for any set Si, all the sets of edges modelling different paths in Si should be *disjoint*.

If there is any other road structure you can see in the game, go ahead and solve for it too.

---

## **Week 4: Intro to ML**

### *Resources*

Woohoo, ML is starting finally. So what is ML? Well, it stands for *Machine Learning* and as the name suggests it involves teaching the computer to learn to do stuff on its own. Although this field has tons of practical real-life applications and programming techniques, it has its roots within Probability theory, Linear Algebra and Statistics which are often overlooked. This week we will get an introduction to how ML models are created from scratch using these math concepts.

[Here](https://www.cs.toronto.edu/~urtasun/courses/CSC411_Fall16/tutorial1.pdf) is a link to some slides covering most of the material we would need this week.

1. Before diving into ML, let's start by refreshing concepts of Probability from JEE days. It is given on slides 4 to 15.

    Make sure to read all of the slides from Sample Space to Bayes Theorem properly.

2. Another important tool for ML is statistics. This may be somewhat new to many of you.

    Go through slides 16-18. It has an introduction to Random Variables, both continuous and discrete.

    Beyond slide 18 up to slide 25, several statistical distributions are given. These distributions are commonly used to model the probability function of random variables. For now, we only need [Gaussian](https://en.wikipedia.org/wiki/Normal_distribution) and [Multivariate Gaussian](https://en.wikipedia.org/wiki/Multivariate_normal_distribution) distributions given on slides 23 to 25.

3. A typical ML problem starts with a **dataset** with some N readings. This dataset can have many features related to every reading. For example,

    - Dataset containing the initial temperature of coffee made from a coffee machine has only 1 feature.

    - Dataset containing the height of a plant from your garden over time has 2 features (height and time).

    - Dataset containing the housing prices along with several features such as area of the house, no. of bedrooms, no. of floors, etc. has multiple features.

    Once we have a dataset we can model it to be drawn from a probability **distribution** having some parameters. This is a crucial design step as every distribution has its own characteristics.

    Now to solve for the parameters of the distribution that represent the given dataset we determine an estimator which leads to an **objective function**.

    This objective function now needs to be optimised. Sometimes this can be done mathematically to get a closed-form solution of the parameters. But while coding these are not accurate or fast so we need various **optimisation** techniques.

    With the solved parameters that optimise the cost function, we can now make **predictions** regarding future outcomes of the experiment.

    With all this background we are ready to tackle our first ML problem using Maximum Likelihood Estimation. This is given in the slides from 28 to 32. Try doing the calculations on your own.

    - Dataset: Single feature like the first example
    - Distribution: 1-dimensional Gaussian distribution
    - Objective Function: Likelihood function
    - Optimisation: Closed-form solution by finding maxima
    - Prediction: Most likely future outcome is the mean of the distribution with an error proportional to the standard deviation

4. Now let's solve a more useful problem. Consider the 2nd dataset of the height of a plant over time.

    A possible and popular technique to model such a problem would be [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression) i.e. y = a*x + b where x is time and y is height.
    Here a and b are the parameters that need to be predicted using a Squared error objective function.

    Let's solve this by a different approach as given in the slides from 33 to 39. Note that here w = [a b]^T. You'll need to do the calculations for this.

    - Dataset: 2 features like the second example
    - Distribution: 2-dimensional Multivariate Gaussian distribution
    - Objective Function: Likelihood function
    - Optimisation: A property of Gaussian distributions is that their MLE for mu and sigma is just the sample mean and sample covariance. Use this property and move ahead.
    - Prediction: For a given future time x0 you can predict height, y0 as the y for which P(x0,y) is maximised. Do this calculation.

    Once you find the relation between y0 and x0 compare it to the linear regression expression and find a and b in terms of mu and sigma.

5. Till now we were using Maximum Likelihood Estimate but many times while predicting the parameters we have certain prior beliefs regarding these parameters. Basically not every possible value of the parameter is equally likely. So we add a prior distribution. Read slides 13 and 26.

    As done earlier, let's derive a new objective function by assuming a 1-dimensional Gaussian prior on the parameter mu. This prior will have mu0 as the mean and sigma0^2 as the variance.

    - Dataset: Single feature like the first example
    - Distribution: 1-dimensional Gaussian distribution with a 1-dimensional Gaussian prior on mu parameter.
    - Objective Function: Posterior Function
    - Optimisation: Another property of Gaussian distributions is that the [product of two Gaussian distributions is another gaussian](https://math.stackexchange.com/a/114425). With this knowledge try to solve for the Maximum Aposterior Estimates aka the MAP estimates. Do this calculation.
    - Prediction: Most likely outcome is the mean of the distribution with an error proportional to the standard deviation

6. When implementing Linear Regression a common issue is [over-fitting](https://en.wikipedia.org/wiki/Overfitting). To avoid this a regularisation term is added to the Squared Error function which is basically the sum of squares of all the parameters. This can also be modelled using a prior on the parameters [a b]^T from the 4th task. Try to get the closed-form estimate for mu and capital Sigma if possible. This is optional.

### *Assignment*

- Attempt all the calculations given in the resources.
- Formulate the problem of playing the Mini Motorways game as an ML problem. Think along the following lines:-

    1. What features and data points will your **dataset** comprise? Keep in mind this data should be easy to collect.
    2. Which **distribution** will you use to model different quantities in the dataset?
    3. What will be the **objective function** that needs to be optimised? Try to derive this rather than just guessing.
    4. How will you **optimise** the objective function? If it is possible to get a mathematical solution then solve it.
    5. How will this model be useful for **predicting** the most optimal moves?

---

## **Week 5: Coding begins**

### *Resources*

This week we begin coding the solver. Both of us are currently working on the getting inputs/outputs of the Mini Motorways game from/to the solver. By the time that work is finished others can go through the some basic libraries and softwares in python.

Each of following libraries have their purposes and vast documentations. So for now you can quickly go over each of them getting some idea about their features and syntax and later when you actually require them in your code then you can refer the docs.

1. [**Numpy**](https://numpy.org/) : Used for fast Linear Algebra related or Statistical computation.

    [W3Schools Tutorial](https://www.w3schools.com/python/numpy/numpy_intro.asp)

2. [**Scipy**](https://scipy.org/) : Has many scientific computing modules.

    [W3Schools Tutorial](https://www.w3schools.com/python/scipy/index.php)

3. [**Pandas**](https://pandas.pydata.org/) : Used for reading and formatting data from CSVs or spreadsheets.

    [W3Schools Tutorial](https://www.w3schools.com/python/pandas/default.asp)

4. [**Matplotlib**](https://matplotlib.org/) or [**Plotly**](https://plotly.com/): Used for plotting graphs.

    [W3Schools Tutorial](https://www.w3schools.com/python/matplotlib_intro.asp)

5. [**Scikit-learn**](https://scikit-learn.org/) : Has many algorithms related to data science and commonly used datasets. Kind of like a learning laboratory for data science.
6. [**Pytorch**](https://pytorch.org/), [**Keras**](https://keras.io/), [**Tensorflow**](https://www.tensorflow.org/) : These are some of the industry level frameworks for working with Neural Networks. We will take a better look at these later on.
7. **Jupyter Notebook** : This is not a library but a modified version of python generally used to create pretty notebooks that display code and outputs together. There is VSCode extension for this so no need to install.
8. [**Google Colab**](https://research.google.com/colaboratory/) : Similar to Jupyter this also creates notebooks but also provides remote runtimes with powerful processors.
9. **Matlab, Octave, etc.** : Now these are entire software that have all the above mentioned capabilities but have different languages than python so steep learning curves.
