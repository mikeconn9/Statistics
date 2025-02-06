Statistical tests:

1. Chi-square test
Used for: Categorical(nominal or ordinal) data represented as counts or frequencies. Requires large expected frequencies (At least 5).
Purpose: Independence? e.g., is gender associated with voting preferences?
Assumption: No normality assumption, observations are independent.

2. Correlation coefficient

3. T-test
Used for: Continuous (interval or ratio) data.
Purpose: Compare means to determine whether there is a statistically significant difference between them. e.g., comparing test scores between two classes.
Assumption: Approximately normally distributed. Variances of two groups are equal (In the independent t-test) or appropriately adjusted if unequal.

4. ANOVA
Used for: Continuous data.
Purpose: Compare the means across three or more groups to see if at least one group mean is statistically different from the others. if showing a significant result, follow-up tests(post hoc tests) are typically used to identify which groups differ.
One-Way ANOVA: For one independent variable with three or more levels(groups).
Two-Way ANOVA: For studying the effect of two independent variables, including any interaction between them.
Assumption: Normally distributed within each group. homogeneity of variances (each group has a similar variance). Observations are independent.


5. Paired t-test
Purpose: For comparing means from the same subjects measured at different times or under different conditions.

6. Runs test
Used for: Assess the randomness of a sequence. It counts the number of runs - continuous sequences of similar items (for example, a run of 0's or 1's in a binary string), and compares the observed number of runs to what would be expected if the data were produced randomly.
H0: Randomness.

7. Spearmanr
Use when you need to assess the strength and direction of a monotonic relationship between two continuous or ordinal variables (especially when data are not normally distributed or contain outliers). Spearman’s tells you about the rank-based association between two variables.
A monotonic relationship implies that variables move together, either both increasing or decreasing over time, without any directional reversal, even if the rate of change varies.

8. Kstest
H0: The data follows the specified distribution, no significant difference.

9. Mann-Whitney U test
Null Hypothesis (H₀): The distributions of the two groups are the same (no significant difference).
Alternative Hypothesis (H₁): One group has "systematically higher (or lower)" values than the other.
Instead of comparing means, it compares ranks of the combined data from both groups.
Unlike the t-test, it does not assume normality; instead, it uses the ranks of the data rather than the raw values.

10. Kruskal-Wallis H test
The Kruskal-Wallis H test is a non-parametric statistical test used to determine if there are statistically significant differences between the medians of three or more independent groups. It's an extension of the Mann-Whitney U test to multiple groups and serves as a non-parametric alternative to one-way ANOVA. This test is particularly useful when the assumptions of normality required for ANOVA are not met.