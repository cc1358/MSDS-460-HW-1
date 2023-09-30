# MSDS-460-HW-1
The Diet Problem Revisited (version 6)

Developed by Thomas W. Miller. Revised September 2, 2023.

Introduced by Stigler (1945) and discussed by Dantzig (1990), the diet problem is a classic problem in constrained optimization often used to introduce linear programming concepts. The diet problem has been studied extensively through the years (van Dooren 2018).

For this assignment, you need to construct a personalized diet using current recommended dietary allowances from the U.S. Food and Drug Administration, updated to account for recent research on sodium intake and health (Mente, O'Donnell, and Yusuf 2021). Interested in learning more about nutrition and healthy living? Check out Nutrients, an open-access journal, at its home page https://www.mdpi.com/journal/nutrients Links to an external site. .

The constraints for this linear programming problem, should consider seven components of nutrition, as shown in the following table:

Component

Max/Min

Amount and measure

Sodium

Maximum

5,000 milligrams (mg)

Energy

Minimum

2,000 Calories (kilocalories, kcal)

Protein

Minimum

50 grams (g)

Vitamin D

Minimum

20 micrograms (mcg)

Calcium

Minimum

1,300 milligrams (mg)

Iron

Minimum

18 milligrams (mg)

Potassium

Minimum

4,700 milligrams (mg)

Set this up as a standard linear programming problem with decision variables taking any non-negative values. In other words, partial servings are permitted.  

Nutrition labels on packaged foods should contain information about these eight components of nutrition along with other components. Each of the components represents a constraint in the linear programming problem you are developing.

To adapt the problem to your personal diet, collect nutrition facts from five packaged food items in your household. Use packaged foods that are part of your normal diet and for which you have prices. Also, ensure that the across the set of food items there are positive values for each of the eight components of nutrition. Adjust the price for each food item so that it represents one serving size, as defined on the nutrition facts label. Each food item represents a decision variable in the linear programming problem.

The goal or objective of this problem is to find the minimum-cost diet (servings of food items) that satisfies the eight nutritional requirements. Use Python Pulp to solve this linear programming problem
