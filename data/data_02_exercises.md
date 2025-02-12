{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Data

## Exercises

---

### Exercise 1

Download the [this dataset](https://www.kaggle.com/datasets/vinitshah0110/food-composition).
Open it with a text editor (or Excel).

Describe for the following columns what kind of data it holds. Also describe the scale.

|Column           |Data type       |Scale            |
|:----------------|:---------------|:----------------|
|Food Name        |                |                 |
|Fat factor       |                |                 |
|Analyzed Portion |                |                 |


### Exercise 2

Have a look at some raw data below:

Item: Granola, Chicken Leg, Tofu, Salmon, Avocados
Calories (kcal) per 100 g: 489, 184, 144, 206, 160

Create a data table of the above data.
Make sure that the observations (or records) and variables (or features) are organized appropriately. Also sort the data based on the amount of calories.

### Exercise 3

Proper cooking temperatures are important for food safety.
The advice is to use proper cooking temperatures to ensure safe food.
See the data below for recommended temperatures:

Fresh beef, veal, lamb, pork, deer, moose, elk or caribou steaks, chops and roasts
recommended minimum temperature	145°F
medium	160°F
well done	170°F

What is the ratio for "medium" and "well done" compared to the recommended minimum temperature?  

Hint: calculate temperature in Kelvin.  

$K = (F − 32) × \frac{5}{9} + 273.15$  

### Exercise 4

The R library Tidyverse will work best with tidy data.
Remember that there are three interrelated rules which make a dataset tidy:
- Each variable must have its own column.
- Each observation must have its own row.
- Each value must have its own cell.

Convert the data table below to a data table that is tidy.

Alcohol consumption in litres per year over time.

|Country        |1996  |2016  |
|:--------------|-----:|-----:|
|Albania        |2.59  |7.50  |
|Algeria        |0.27  |0.90  |
|Netherlands    |9.80  |8.70  |

Also mention, which of the three interrelated rules which make a dataset tidy have not been met.

### Exercise 5

Another untidy data table. Describe which of the three interrelated rules which make a dataset tidy have not been met and convert the data table to a data table that is tidy.

|Country        |1996, 2016   |
|:--------------|------------:|
|Albania        |2.59, 7.50   |
|Algeria        |0.27, 0.90   |
|Netherlands    |9.80, 8.70   |

### Exercise 6

Here we have a tidy data table data table. Spread it in order to make it wider (and untidy).

|Country        |Year|Consumption type   |Volume (l)|
|:--------------|:---|:------------------|---------:|
|Albania        |1996|Alcohol            |2.59      |
|Albania        |1996|Bottled water      |120       |
|Albania        |2016|Alcohol            |7.50      |
|Albania        |2016|Bottled water      |131       |
|Algeria        |1996|Alcohol            |0.27      |
|Algeria        |1996|Bottled water      |144       |
|Algeria        |2016|Alcohol            |0.90      |
|Algeria        |2016|Bottled water      |154       |



---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

