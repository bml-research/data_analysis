{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel: Data Visualization


![impression](./pics_11_data_visualization/fig1.png)
*<sub>Figure 1: Data visualization of bacteria grown in the presence of anthocyanins isolated from red grapes.</sub>*


## Introduction

Though not as powerful as R or Python, Excel is a user friendly tool for data analysis and visualization. Whether you're working in the food industry or conducting research on nutrition, Excel can help you make sense of your data and present your findings in a clear and compelling way. By using Excel's built-in charting features, you can easily create a variety of charts and graphs that visualize key trends and patterns in your data, such as changes in nutrient levels over time, differences between different food products, or correlations between different variables. With Excel, you can create professional-looking charts and graphs that are easy to understand and can help you communicate your insights to others. Excel offers a wide range of tools and capabilities that can help you make sense of your food-related data and present it in a way that is meaningful and informative.


## Data visualization charts in Excel

Excel offers a wide variety of chart types, which can be customized to suit your data and presentation needs. Some of the most commonly used chart types in Excel include:
- Column charts: Used to compare values across different categories or to show changes over time.
- Line charts: Used to show trends over time or to compare trends between multiple data sets.
- Pie charts: Used to show how different categories contribute to a whole.
- Bar charts: Similar to column charts, but with horizontal bars instead of vertical columns.
- Scatter charts: Used to show the relationship between two variables.
- Area charts: Similar to line charts, but with the area between the line and the x-axis filled in.
- Radar charts: Used to compare multiple data sets across different categories.
- Surface charts: Used to show trends in three-dimensional data.
- Bubble charts: Similar to scatter charts, but with bubbles of different sizes to represent the data points.

These are just a few of the chart types available in Excel. With its robust set of charting features, Excel offers a wide range of options for visualizing your data and communicating your insights to others.


## What makes a good chart?

A good chart is one that effectively communicates your data in a clear and concise manner. Here are some key characteristics of a good chart:
- Accuracy: The data in the chart should be accurate and clearly labeled. Any sources of error or uncertainty should be clearly indicated.
- Clarity: The chart should be easy to read and understand. The axes and labels should be clearly labeled (with units), and any legends or annotations should be concise and to the point.
- Simplicity: The chart should be simple and straightforward, avoiding unnecessary clutter or complexity (such as colored bars when they are not informative). The message of the chart should be clear and easily - understandable at a glance.
- Relevance: The chart should be relevant to the audience and the purpose of the presentation. It should highlight the key insights or trends in the data, and should be designed with the audience's needs and interests in mind.
- Aesthetics: The chart should be visually appealing and professional-looking, with clear, readable fonts and colors that complement the data being presented.

By focusing on these key characteristics, you can create charts that effectively communicate your data and insights, and help you to make better-informed decisions based on your data.

## Some chart examples

### Column charts

Column charts are suitable for comparing values across different categories or for showing changes in data over time. They are a popular and effective way to visually represent categorical data, and are often used to display data in the form of vertical bars.

>In Excel, charts with vertical bars are called column charts and bars with horizontal bars are called bar charts.

Column charts are particularly useful for:
- Comparing data: Column charts make it easy to compare data across different categories or groups, and to identify trends or patterns in the data.
- Showing changes over time: Column charts can be used to show changes in data over time, such as changes in sales or revenue from one year to the next.
- Highlighting differences: Column charts can be used to highlight differences between groups or categories, making it easy to see which values are larger or smaller than others.
- Displaying large amounts of data: Column charts can be used to display large amounts of data in a clear and concise manner, making it easy to interpret and analyze the data.

Overall, Column charts are a versatile and effective way to visualize categorical data and to communicate important insights and trends to others.

So let's take the pivot table from the fast food restaurant menu data as an example. See [this dataset](https://www.kaggle.com/datasets/mcdonalds/nutrition-facts).
We have the average amount of total calories as well as the calories from fat of the different food categories.

![pivot](./pics_11_data_visualization/fig2.png)
*<sub>Figure 2: Pivot table showing the average amount of total calories as well as the calories from fat of the different food categories.</sub>*

What the data tell you is that meet and fish are high in fat and beverages are low (they are high in sugar). Not very surprising, but useful as an example. 

Let's first start with a Column chart for the average amount of calories from fat for the different food categories:

If you need more help (each individual step explained), have a look [here](https://support.microsoft.com/en-us/office/present-your-data-in-a-column-chart-d89050ba-e6b6-47de-b090-e9ab353c4c00).

![Column chart](./pics_11_data_visualization/fig3.png)
*<sub>Figure 3: Column chart representing the average amount of calories from fat per serving for different food categories in a fast food restaurant.</sub>*

>Note that providing different colors for each different bar does not provide extra information. It will confuse the reader.

Now if you would like to compare this to the total amount of calories, you could create a clustered column chart for this:

![Column chart](./pics_11_data_visualization/fig4.png)
*<sub>Figure 4: Clustered column chart representing the average amount of calories from fat per serving related to the total amount of calories for different food categories in a fast food restaurant.</sub>*

>Note that providing different colors for each different set does provide extra information. Thus, it is highly recommended in this case.

But these data are difficult to compare. You could use a stacked column chart to have it all in one overview:

![Stacked column chart](./pics_11_data_visualization/fig5.png)
*<sub>Figure 5: Stacked column chart representing the average amount of calories from fat per serving related to the total amount of calories for different food categories in a fast food restaurant.</sub>*


But how do these calories from fat relate relatively to the total calories?
We could calculate this but Excel provides a plot type that takes this work out of your hands:

![Relative Stacked column chart](./pics_11_data_visualization/fig6.png)
*<sub>Figure 6: Relative stacked column chart representing the relative average amount of calories from fat per serving related to the total amount of calories for different food categories in a fast food restaurant.</sub>*

Like the relative stacked column chart, the pie chart is another chart type that is suitable for such a representation.

## Pie Chart

Pie charts are suitable for displaying data that can be broken down into categories or parts that add up to a whole. They are often used to show proportions or percentages of a whole.

Pie charts are effective for conveying information quickly and intuitively, as the size of each slice corresponds to its percentage of the whole. They are also useful for highlighting the relative sizes of each category or part, making it easy to compare them at a glance.

However, pie charts may not be the best choice for all types of data. For example, they can become difficult to read when there are too many categories or when the differences between the sizes of the slices are small. In these cases, a bar chart or other visualization (Pie of Pie) may be more appropriate.

We take our previous example as an example to create a pie chart:

![Pie chart](./pics_11_data_visualization/fig7.png)
*<sub>Figure 7: Pie chart representing the relative average amount of calories from fat per serving related to the total amount of calories for different food categories in a fast food restaurant.</sub>*

Or with the data labels and percentages shown connected to the pie slices (choose: chart design > chart elements > Data labels > Outside End):


![Pie chart](./pics_11_data_visualization/fig8.png)
*<sub>Figure 8: Pie chart representing the relative average amount of calories from fat per serving related to the total amount of calories for different food categories in a fast food restaurant. Data labels and percentages are connected to the pie slices.</sub>*



## Pie of Pie

Pie of Pie charts can become handy if the individual slices become small and the Pie chart becomes cluttered. 

Here is an example of a Pie of Pie chart:

![Pie of Pie chart](./pics_11_data_visualization/fig9.png)
*<sub>Figure 9: Pie of Pie chart representing the relative average amount of calories from fat per serving related to the total amount of calories for different food categories in a fast food restaurant. Data labels and percentages are connected to the pie slices.</sub>*

As you can see, the second Pie is created from the smallest Pie slices from the first Pie chart. This creates less clutter when the individual slices become to small. Although in this case, the original Pie chart would do well.

You can format the secondary Pie by right-clicking it > Format Data Series and then use the drop down to select the appropriate Split Series (percentage value was used here).

## Radar charts

A radar chart, also known as a spider chart or a star chart, is a graphical representation of data in which values are plotted along a set of axes that radiate from a central point. Each axis represents a different variable, and the data points are connected to form a polygon shape, which can be filled in with color to represent the area covered by the data.

Radar charts are often used to compare multiple variables or data sets, particularly when the values have different units or scales. 

Let's view some (imaginary) data from three fast food restaurants. These data show the average of calories of fat per serving from different Categories (like the previous data). But compared to the previous data, we now have these numbers from three different vendors.

You can download the data [here](./files_11_data_visualization/file01_radar_data.csv).

![Data for a radar chart](./pics_11_data_visualization/fig10.png)
*<sub>Figure 10: Data suitable for a radar chart. Calories from fat for different food Categories purchased from different vendors.</sub>*

The resulting radar chart is shown below:

![Radar chart](./pics_11_data_visualization/fig11.png)
*<sub>Figure 11: Radar chart created from the previous data set. Calories from fat for different food Categories purchased from different vendors.</sub>*


Note that it becomes clear that restaurant B sells desserts with a lot of calories from fat. So either the fat percentage of fat is high or the portions are very large. 

## Box plots

A box plot, also known as a box and whisker plot, is a graphical representation of a dataset that shows the distribution of the data through its quartiles, outliers and extremes. It is called a box plot because it uses a box to represent the second and third quartiles (the inter-quartile range or IQR), and lines to represent the first and fourth quartiles (the lowest and highest data points within the IQR), as well as the outliers, if any.

Box plots are useful for visualizing the distribution and spread of data, as well as for identifying potential outliers. They can also be used to compare the distribution of data between different groups or datasets. Box plots are particularly useful when the data is non-parametric (not normally distributed) or when the distribution is skewed or multi-modal.

Overall, box plots are a useful tool for summarizing and visualizing complex data sets, and for providing insights into the distribution of data and potential outliers.

Let's have a look at the following dataset:

![Box plot data](./pics_11_data_visualization/fig12.png)
*<sub>Figure 12: Data about calories from fat for different food categories.</sub>*

And compare the different categories for calories from fat and total calories.

The questions that can be asked are:
- What is the median value per category? 
- What are the minimum and maximum values per category?
- What are the 25% and 75% percentile values per category?
- Are there any outliers?

A box plot will answer all these questions at once:

We choose the columns `Calories from fat` and `Calories` for the series. The food categories are selected as labels. See the result below.

![Box plot](./pics_11_data_visualization/fig13.png)
*<sub>Figure 13: Box plot about calories from fat for different food Categories.</sub>*

The above picture is the standard layout of the box plot in Excel. However, you could argue that it would be better to tweak some things in the plot. First of all, the mean is shown as a cross. Box plots are often used in combination with nonparametric statistics and quantile (including median) values are much more appropriate to use. In addition, inner points are visible and we can not discriminate them from outliers. Finally, we should look if our number of values (N) are odd or even. The median is included in the calculation if N is odd. The median is excluded from the calculation if N is odd. Since this varies per food category, we will choose the excluded method. We can tweak each series (select the series and choose: `Format Data Series`) accordingly. See the result below:

![Box plot](./pics_11_data_visualization/fig14.png)
*<sub>Figure 14: Tweaked box plot about calories from fat for different food categories.</sub>*


## Line and XY-scatter plots


Line charts are useful when you want to visualize trends or changes in data over time or another continuous variable. They are particularly good for showing how a particular variable changes over time or in response to another variable. For example, a line chart can be used to show how a persons weight has changed over time. 

On the other hand, XY scatter plots are useful when you want to visualize the relationship between two variables. They are particularly useful for showing the degree of correlation between two variables or identifying outliers in the data. For example, a scatter plot can be used to show the relationship between a person's height and weight. 

In summary, line charts are best used when you want to show trends or changes over time, while XY scatter plots are best used when you want to visualize the relationship between two variables.


As an example, we take some fictive data about a weight loss program for 3 individuals (taking 3 different diets).

The data can be downloaded [here](./files_11_data_visualization/file02_weight_loss.csv).

The data loaded in excel looks as follows:

![data](./pics_11_data_visualization/fig15.png)
*<sub>Figure 15: Fictive data for a weight loss program for three different diets over the course of 1 year.</sub>*

The corresponding line plot looks as follows:

![line plot](./pics_11_data_visualization/fig16.png)
*<sub>Figure 16: Line plot of fictive data for a weight loss program for three different diets over the course of 1 year.</sub>*

As you can see, diet 2 is relatively ineffective. Not much weight loss. Diet 1 could be considered a crash diet with a sharp initial decline that halts later in the year. Diet 3 shows a very linear weight loss for a much larger period of time and could be considered the dietary intervention of choice.

Of course, one should take into account that only three persons are included in this dietary intervention.

Realize that a line chart is only plotted well if the data points are inter-spaced evenly.

Consider the following mini dataset:

![small data set](./pics_11_data_visualization/fig17.png)
*<sub>Figure 17: Dietary intervention for 365 days.</sub>*

As you can see, the data points for x are not evenly distributed.
Plotting this with a line plot will go wrong:

![line plot](./pics_11_data_visualization/fig18.png)
*<sub>Figure 18: Line plot for dietary intervention for 365 days.</sub>*

As you can see, the data points on the x-axis are just labels and do not correspond to their actual value. Thats why we need an XY-scatter plot for this purpose:

![line plot](./pics_11_data_visualization/fig19.png)
*<sub>Figure 19: XY-scatter plot for dietary intervention for 365 days.</sub>*

As you can see from the above chart, the data on the x-axis are now separated according to their value.

To show the use of an XY-scatter plot to visualize a correlation, the [ChickWeight dataset](https://github.com/selva86/datasets/blob/master/ChickWeight.csv) from R was used. The weight column represents the body weight of the chick (g). The time column represents the number of days since birth when the measurement was made.

![Chicken Weight](./pics_11_data_visualization/fig20.png)
*<sub>Figure 20: Chicken weight data set. Dataset was filtered for Diet 1</sub>*

The data of all chickens from diet 1 plotted as XY-scatter:
A linear regression model was added as trendline and the equation is shown on the chart (together with the r^2 value).

![Chicken Weight](./pics_11_data_visualization/fig21.png)
*<sub>Figure 21: Chicken weight data set plotted as XY-scatter. Dataset was filtered for Diet 1</sub>*



## Bubble chart

If you have data that is most suitable to present in a XY-grid but you have an extra dimension, bubble charts might be a good chart type.

Bubble charts are a great way to display data that includes three variables. In the context of food science, here is an example of a dataset that could be presented in a bubble chart:

Suppose you have collected data on the nutritional content of different types of fruits. Specifically, you have measured the sugar content (in grams per serving) and the vitamin C content (in milligrams per serving) of six different types of fruit: apples, bananas, oranges, strawberries, blueberries, and grapes. In addition, you have collected the number of servings per year for a particular person.

The fictive dataset can be downloaded [here](./files_11_data_visualization/file04_bubble_chart.csv).

To display this data in a bubble chart, you could use the following format:

X-axis: Sugar content (grams per serving)
Y-axis: Vitamin C content (milligrams per serving)
Bubble size: Represents the number of servings per year of each fruit that were tested.
By using a bubble chart to display this data, you can quickly see patterns and trends among the different types of fruits based on their sugar and vitamin C content, as well as their number of servings per years.

![Fruit data](./pics_11_data_visualization/fig22.png)
*<sub>Figure 22: data set suitable to display in a bubble chart. Note that these are fictive data.</sub>*

Below is a bubble chart of this dataset:

![Fruit data](./pics_11_data_visualization/fig23.png)
*<sub>Figure 23: Bubble chart of fruit data. Note that the bubble size (and the numbers in the labels) represents the number of servings per year.</sub>*

The Chart includes the following:

X-axis: Sugar content (grams per serving)
Y-axis: Vitamin C content (milligrams per serving)
Bubble size: Represents the number of servings per year of each fruit that were tested.

An extra dimension could be included by using colors. For example you could add categorical data (ordinal data in this case) such as high vitamin B9 (folate) data points in green color, intermediate vitamin B9 content as orange dots and low vitamin B9 content in red.


## Pivot charts

In the [data analysis](./excel_08_data_analysis.md) section, we have seen the use of pivot tables. Pivot tables come in handy to analyze data quickly and in an organized manner. We can use pivot charts to directly visualize the data from pivot tables.

We will use the example from the data analysis section to create a pivot chart.

Let’s pretend that we are mainly interested in comparing the average amount of calories from fat (both total and saturated) of each food category from the earlier used dataset [Nutrition facts](https://www.kaggle.com/datasets/mcdonalds/nutrition-facts) data.

![Nutritional food data](./pics_11_data_visualization/fig24.png)
*<sub>Figure 24: Nutritional facts data about different food categories of a fast food restaurant</sub>*

The corresponding pivot table was as follows:

![Nutritional food data pivot table](./pics_11_data_visualization/fig25.png)
*<sub>Figure 25: Pivot table of average calories and average calories from fat from nutritional facts data.</sub>*

So first we choose pivot chart from the ribbon and select the data source as well as the sheet for the output data:

![Pivot chart](./pics_11_data_visualization/fig26.png)
*<sub>Figure 26: Data source and the output sheet selected.</sub>*

Next, we select the correct fields and the calculations on the data (we use average for this example).

![Pivot chart](./pics_11_data_visualization/fig27.png)
*<sub>Figure 27: Select the correct fields and calculation types.</sub>*

This results in the following chart. 

![Pivot chart](./pics_11_data_visualization/fig28.png)
*<sub>Figure 28: Pivot chart. Average calories and average calories from fat from different food categories.</sub>*

Note that you can dynamically select or unselect specific categories. We can for example deselect the drinks:

![Pivot chart](./pics_11_data_visualization/fig29.png)
*<sub>Figure 29: Pivot chart. Average calories and average calories from fat from different food categories. Drinks deselected. </sub>*


The result of the pivot chart (drinks deselected):

![Pivot chart](./pics_11_data_visualization/fig30.png)
*<sub>Figure 30: Pivot chart. Average calories and average calories from fat from different food categories. Drinks deselected. </sub>*

Remember that we also need to include axis titles (now with all categories selected).

![Pivot chart](./pics_11_data_visualization/fig31.png)
*<sub>Figure 31: Pivot chart. Average calories and average calories from fat from different food categories. Axis labels and chart title included. </sub>*

---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

