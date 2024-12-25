# Statistics

What is the Mann-Whitney U Test?
The Mann-Whitney U test is a non-parametric statistical test used to compare two independent groups. Unlike the t-test, it does not assume normal distribution of the data and is especially useful when:

The data is not normally distributed.
The data is ordinal (e.g., rankings or scores).
The sample size is small.
It evaluates whether one group tends to have higher values than the other, based on the ranks of the data rather than their actual values.

Key Concepts
Null Hypothesis (H₀): The distributions of the two groups are the same (no significant difference).
Alternative Hypothesis (H₁): One group has systematically higher (or lower) values than the other.
Instead of comparing means, it compares ranks of the combined data from both groups.

Example Scenario
Let’s revisit the A/B test scenario for Repeat Rate comparison between the Control Group (standard delivery time) and Test Group (long delivery time). Assume the Repeat Rates are not normally distributed, making the Mann-Whitney U test a suitable option.

Data
| Control Group | Test Group |
| 25% | 20% | 
| 30% | 22% |
| 28% | 18% |
| 29% | 21% |
| 27% | 19% |


