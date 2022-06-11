# **Week 4: Intro to ML**

## *Resources*

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

## *Assignment*

- Attempt all the calculations given in the resources.
- Formulate the problem of playing the Mini Motorways game as an ML problem. Think along the following lines:-

    1. What features and data points will your **dataset** comprise? Keep in mind this data should be easy to collect.
    2. Which **distribution** will you use to model different quantities in the dataset?
    3. What will be the **objective function** that needs to be optimised? Try to derive this rather than just guessing.
    4. How will you **optimise** the objective function? If it is possible to get a mathematical solution then solve it.
    5. How will this model be useful for **predicting** the most optimal moves?
