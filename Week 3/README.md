# **Week 3: Traffic Sciences**

## *Resources*

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

## *Assignment*

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
