{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel Data Visualization

## Exercises

---

### Exercise 1

Load the [Food Emissions](https://www.kaggle.com/datasets/amandaroseknudsen/foodproductemissions?resource=download) dataset from Kaggle.

Create a column chart for the `Total Global Average GHG Emissions per kg` per `food product`.

Create the column chart on a new worksheet.
Annotate the axis and add a proper title.

What food product creates the highest Emission value?


### Exercise 2

As the differences in the values are rather high, it is wise to use a log scale to display your data. Log scales have their advantages and are often used to display data that cover a wide range of values. Use a 2log scale to display your data.

### Exercise 3

From the previous dataset, filter the data that contain oil in the name.  
Create a clustered column chart representing the Emissions per kg from `Farm`, `Processing`, `Transport`, `Packaging` and `Retail`. Make sure to add proper axis titles, a title and a legend.

### Exercise 4

Use the same data as from exercise 3 to create a stacked column chart. Filter the data that contain oil in the name.  
Create a stacked column chart representing the Emissions per kg from `Farm`, `Processing`, `Transport`, `Packaging` and `Retail`. Make sure to add proper axis titles, a title and a legend.

### Exercise 5

Use the same data as from exercise 3 to create a relative stacked column chart. Filter the data that contain oil in the name.  
Create a relative stacked column chart representing the Emissions per kg from `Farm`, `Processing`, `Transport`, `Packaging` and `Retail`. Make sure to add proper axis titles, a title and a legend.


### Exercise 6

Use the same data to create a Pie chart. Filter the data that contain `palmoil` in the name.  
Create a pie chart representing the Emissions per kg from `Farm`, `Processing`, `Transport`, `Packaging` and `Retail`.  
Show the percentages as labels.

Also create a Pie chart for all the oil types showing the Total Global Average GHG Emissions per kg. 
Show the values as labels.  


### Exercise 7

Download the [data set about](https://www.kaggle.com/datasets/kkhandekar/calories-in-food-items-per-100-grams) food calories per 100 g. 

The data set contains units in the cells.  
First clean the dataset.  
Create a box plot for `Energy per 100 g in KJ` plotted against the `Food Categories`.  

Which two Food Categories show the highest energy per weight?

### Exercise 8

In [this dataset](./files_12_data_visualization_exercises/exercise08/ChickWeight.csv) you can find Chick Weight data. It shows the weight (in grams) on day 42 for various chickens that were fed with various diets during 42 days.

Create a radar chart for the various diets on day 42.  
Calculate the average weight per diet.

Two Chickens on a certain diet clearly gained the most weight.  
Wich two chickens on which diet generated the highest weight gains?  

### Exercise 9

Have look at the data [here](./files_12_data_visualization_exercises/exercise09/data.csv)
It contains data about Potassium and Sodium content (in mg/100 g) as well as calories (in kcal/100 g).  

The World Health Organization (WHO) recommends ingestion of less than 2000 mg of sodium per day and more than 3510 mg of potassium per day, resulting in a Na-to-K ratio of ≤1.0, which is believed to be optimal for preserving cardiovascular health.

In addition, high caloric food is often bad for cardiovascular health.  

As you can see, only the K-to-Na ratio is calculated.   
Create a bubble chart with the Na concentration as a function of the K concentration.  
The bubble size should be based on the calorie values.  

Which two food items would be considered most healthy food items based on the information above?  

### Exercise 10

In [this dataset](./files_12_data_visualization_exercises/exercise10/meat-production-tonnes.csv) you can find World wide meat production from 1961 to 2021 expressed in tonnes. It includes cattle, poultry, sheep/mutton, goat, pig meat, and wild game (source: https://ourworldindata.org/meat-production). 

Create a XY-scatter plot with the total production of meat (in tonnes) plotted against time for the asian continent.  

Use Scientific notation for the mass meat production.  

### Exercise 11

For this exercise, we will use the dataset from exercise 7 again. This time, to create a pivot table and plot.

Download the [data set about](https://www.kaggle.com/datasets/kkhandekar/calories-in-food-items-per-100-grams) food calories per 100 g. 

The data set contains units in the cells.  
First clean the dataset.  
Create a pivot plot for the **mean** `Energy per 100 g in KJ` plotted against the `Food Categories`.  

Which two Food Categories show the highest mean energy per weight?
 

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

