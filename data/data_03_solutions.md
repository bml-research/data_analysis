{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Data

## Exercises Solutions

---

### Exercise 1

|Column           |Data type       |Scale            |
|:----------------|:---------------|:----------------|
|Food Name        |Nominal         |Nominal          |
|Fat factor       |Continuous      |Ratio            |
|Analyzed Portion |Continuous      |Ratio            |


### Exercise 2

|Item             |Calories (kcal/g)|
|:----------------|----------------:|
|Granola          |489              |
|Salmon           |206              |
|Chicken Leg      |184              |
|Avocados         |160              |
|Tofu             |144              |


### Exercise 3

Note that fahrenheit scale has no absolute zero (0 °F, was established as the freezing temperature of a solution of brine made from a mixture of water, ice, and ammonium chloride). As a result, we can not directly calculate a ratio as the fahrenheit scale is an interval scale. We first need to convert the data to Kelvin.

We can use the formula:  

$K = (F − 32) × \frac{5}{9} + 273.15$  

So we will get the following data:  

recommended minimum temperature	145°F = 336 K  
medium	160°F = 344 K  
well done	170°F = 350 K  

Ratio medium/recommended minimum temperature = 344/336 = 1.025  
Ratio well done/recommended minimum temperature = 350/336 = 1.041  

### Exercise 4

The rule "Each variable must have its own column." has not been met. In the untidy table, there are two columns related to the volume. Thus, the column names are not names of variables, but values of a variable. Thus, we need to create a column "year" in order to solve this.

|Country        |Year|Volume (l)|
|:--------------|:---|---------:|
|Albania        |1996|2.59      |
|Albania        |2016|7.50      |
|Algeria        |1996|0.27      |
|Algeria        |2016|0.90      |
|Netherlands    |1996|9.80      |
|Netherlands    |2016|8.70      |

### Exercise 5

The rule "Each value must have its own cell." has not been met. In the untidy table, there are two values related to the volume in one cell. Thus, we need to separate them over two records (rows) in order to solve this. Note that we should not separate these values in two columns as this will create the situation as shown in Exercise 4.

|Country        |Year|Volume (l)|
|:--------------|:---|---------:|
|Albania        |1996|2.59      |
|Albania        |2016|7.50      |
|Algeria        |1996|0.27      |
|Algeria        |2016|0.90      |
|Netherlands    |1996|9.80      |
|Metherlands    |2016|8.70      |

### Exercise 6

The wider data table:

|Country        |Year|Volume Alcohol (l) |Volume Bottled Water (l)|
|:--------------|:---|------------------:|-----------------------:|
|Albania        |1996|2.59               |120                     |
|Albania        |2016|7.50               |131                     |
|Algeria        |1996|0.27               |144                     |
|Algeria        |2016|0.90               |154                     |

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

