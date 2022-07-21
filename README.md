# amazon_coding_challenge

Solving the Amazon self driving car delivery challenge using Markov Decision Process.
# Bright Network Internship Task 1 - Amazon Coding Challenge

### Berin Berchmans

### 1️⃣ Phase 1

To create a pathfinding algorithms for Amazon’s self-driving delivery vehicles,  I propose a solution to find the 2D path between the starting point and delivery point by framing the problem as a **MDP or Markov Decision Process**. In MDP, an agent is supposed to decide the best action to select based on his current state. This step is taken on each state the agent is in. An MDP has states, actions and rewards. The states here are the cells of the grid. The actions are the set of all possible actions the delivery car can take, here it is [UP, DOWN, LEFT, RIGHT, TOP-LEFT, TOP-RIGHT, BOTTOM-LEFT, BOTTOM-RIGHT] . The rewards are values that it gets for moving to a particular state. I created a 10x10 grid and then created the transition table and reward table for the problem. I assigned a reward value of 5 for the delivery point and -3 for the obstacles.  Using value-iteration we can get a set of values for each cell of the grid. These values can be used to map the ideal route the delivery car can take to reach the delivery point. 

Having generated the ideal route, I have represented this route on the grip graphically as follows :-

The path, obstacles and delivery point are represented as the following colors:-

🟨 - The path for delivery

🟦 - The obstacles

🟩 - Delivery Point

![Figure_10.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3e9a861-ac62-4870-a86a-690b7551356d/Figure_10.png)

The output of the algorithms is as follows (starting from initial cell to the cell right before delivery) :-

```python
[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
No of Steps : 9
```

---

### 2️⃣ Phase 2

In phase 2, I increased the number of obstacles to 20. The obstacles are randomly generated. It can be seen that the algorithm find the optimal route with just a small increase in the number of steps. The following are two different runs with the same number of obstacles.

**Run 1 :**

![Figure_1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0bd8cb30-59bd-461f-9f74-b1d864e1fd4a/Figure_1.png)

```python
[[0, 0], [1, 1], [2, 2], [2, 3], [2, 4], [3, 5], [4, 6], [5, 7], [5, 8], [6, 9], [7, 9], [8, 9]]
No of Steps : 12
```

**Run 2 :**

![222.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d2d73d4e-b29c-4a7c-b1c3-acf27a69f6cb/222.png)

```python
[[0, 0], [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [7, 7], [8, 8]]
No of Steps : 10
```

For a third run, I am increased the number of obstacles to 30. It can be seen that the algorithm still preforms well as it reaches the delivery point with almost the same number of steps as the previous cases.

![fig 3- 30 obs.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/932199ca-8179-4a1a-8ea7-aadd1ef692f0/fig_3-_30_obs.png)

```python
[[0, 0], [0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 5], [5, 6], [6, 6], [7, 7], [7, 8], [8, 9]]
No of Steps : 12
```

---

### 🅱️ Bonus

In the case that the delivery point is blocked off, I print out that the delivery wasn’t possible. Due, to time constraints I was not able to concentrate of finding the obstacles that need to be removed.
