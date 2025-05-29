# Wordle Bot: An Information Theory Approach

This project explores the application of **information theory** to solve Wordle.

This project takes significant inspiration from the 3Blue1Brown video, "Solving Wordle using information theory," which beautifully visualizes and explains the core concepts applied here. You can watch the video [here](https://www.youtube.com/watch?v=v68zYyaEmEA).

---
## How it Works

The core of this Wordle bot lies in its application of **information theory**. For each potential guess, the bot calculates the expected information gain. This involves:

1.  **Calculating the probability distribution** of possible Wordle answers given the current state of knowledge (previous guesses and scores).
2.  **Determining the "score"** (feedback pattern) for each possible guess against every remaining potential answer.
3.  **Calculating the entropy** of the remaining possible answers before and after a hypothetical guess. The difference represents the information gained.

The bot then selects the word that maximizes this expected information gain, effectively narrowing down the possibilities most efficiently.

---
## Scoring Convention

The bot uses a simple and intuitive scoring convention for Wordle feedback: a list of 5 integers where **0 is grey, 1 is yellow, and 2 is green**.

For eg. if CRANE has a score of (2,2,0,1,0), this indicates that 'C' and 'R' are in the right place, 'N' is in the answer word but not in the right position and 'A' and 'E' are not in the answer word.

---
## Scalability

The words are filtered from the official list of possible answers of the NY Times Wordle. However, the code is **scalable** to be used with a dataset of any size and can be expanded or contracted to be used for any word sizes, assuming hardware isn't a limiting factor.

---
## Potential Bottlenecks

There may be a case where the bot might lead into a **bottleneck** (no next best guess). This is often solved by using a different word from the last best guess list.

---
## Theoretical Basis

This project was made to research the idea of **Entropy** and **Information gain** based on the studies of **Claude Shannon**. And in the broader sense, **information theory** as a whole.

The information content of a message or event can be quantified using **Shannon entropy**, denoted as $H(X)$. For a discrete random variable $X$ with possible outcomes $x_1, x_2, \dots, x_n$ and probabilities $P(x_1), P(x_2), \dots, P(x_n)$, the entropy is defined as:

$$H(X) = -\sum_{i=1}^{n} P(x_i) \log_b P(x_i)$$

Where:
* $P(x_i)$ is the probability of outcome $x_i$.
* $\log_b$ is the logarithm with base $b$.
