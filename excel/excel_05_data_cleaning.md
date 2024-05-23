{% include head.html %}
![Hanze](../hanze/hanze.png)

[Go back to the main page](../index.md)


# Excel: Data Cleaning


## Introduction

In data science, data is typically organized in a structured format, such as a table or a spreadsheet. This allows for easy manipulation and analysis of the data.

However, a lot of data coming from external sources such as lab equipment and factory equipment will not be directly suitable for data analysis. In that case, data cleaning en reorganization might me required.

Excel lacks behind Python and R in capabilities of data reorganization and cleaning. Nevertheless, Excel has some features that are worth explaining. We will discuss them here.

## Text to column feature

If your csv data import fails, you can manually parse your text to various columns. Take a look at the following example:

![food](./pics_05_data_cleaning/fig1.png)
*<sub>Figure 1: All data in a single column</sub>*

As you can see, all data is loaded in the first column. You can use the `text to columns` functionality that can be found on the data tab in the ribbon.

![food2](./pics_05_data_cleaning/fig2.png)
*<sub>Figure 2: Select the delimiter</sub>*

Here the correct column separator is selected to parse the text. The result is as follows:

![food3](./pics_05_data_cleaning/fig3.png)
*<sub>Figure 3: Text separated to columns</sub>*

As you can see from the picture above, the text is now separated in different columns based on the correct column separator.


## Remove duplicates

On the data tab in the ribbon, you will find an option to remove duplicate rows:

![duplicates](./pics_05_data_cleaning/fig4.png)
*<sub>Figure 4: Remove duplicates feature</sub>*

As can be seen from the picture below, row ID 2 is a duplicate.

![duplicates](./pics_05_data_cleaning/fig5.png)
*<sub>Figure 5: Two duplicate rows</sub>*

You can select columns to compare. In the case below, all columns were selected.

![duplicates](./pics_05_data_cleaning/fig6.png)
*<sub>Figure 6: Columns selected to compare</sub>*

Excel reports the removal of 1 duplicate row.

![duplicates](./pics_05_data_cleaning/fig7.png)
*<sub>Figure 7: 1 duplicate value removed.</sub>*

And the result is 1 duplicate row removed.

![duplicates](./pics_05_data_cleaning/fig8.png)
*<sub>Figure 8: 1 duplicate row removed.</sub>*

## Trimming text

Often, data will contain extra whitespace such as spaces. Extra spaces are notoriously difficult to spot, especially those at the end. Those extra spaces may interfere with later analysis. 

![extra spaces](./pics_05_data_cleaning/fig9.png)
*<sub>Figure 9: Only 1 Milk counted as one cell contains Milk with a tailing space.</sub>*

The `TRIM` function will remove trailing whitespace:

![extra spaces](./pics_05_data_cleaning/fig10.png)
*<sub>Figure 10: The TRIM function in action.</sub>*

As a result, the tailing whitespace is now removed and the `COUNTIF` function returns the expected result.

## Find and replace

Find and replace is useful to clean data. This example shows some HTML tags in cells:

![find replace](./pics_05_data_cleaning/fig11.png)
*<sub>Figure 11: HTML tags in cells.</sub>*

Removing them is easy using find and replace:

![find replace](./pics_05_data_cleaning/fig12.png)
*<sub>Figure 12: Remove HTML tags in cells.</sub>*

The `*` is a wildcard that represents any text. Note that you do not need to explicitly specify an empty string in the `replace with` field. Excel will take care of this.

![find replace](./pics_05_data_cleaning/fig13.png)
*<sub>Figure 13: HTML tags removed.</sub>*

There are some other handy functions that work on strings that can help you:

| **Function** | **Explanation**                                                                                                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIND         | FIND and FINDB locate one text string within a second text string, and return the number of the starting position of the first text string from the first character of the second text string.                                 |
| SEARCH       | The SEARCH and SEARCHB functions locate one text string within a second text string, and return the number of the starting position of the first text string from the first character of the second text string.               |
| REPLACE      | REPLACE replaces part of a text string, based on the number of characters you specify, with a different text string.                                                                                                           |
| SUBSTITUTE   | Substitutes new_text for old_text in a text string. Use SUBSTITUTE when you want to replace specific text in a text string; use REPLACE when you want to replace any text that occurs in a specific location in a text string. |
| LEFT         | LEFT returns the first character or characters in a text string, based on the number of characters you specify.                                                                                                                |
| RIGHT        | RIGHT returns the last character or characters in a text string, based on the number of characters you specify.                                                                                                                |
| LEN          | LEN returns the number of characters in a text string.                                                                                                                                                                         |
| MID          | MID returns a specific number of characters from a text string, starting at the position you specify, based on the number of characters you specify.                                                                           |

## Splitting and concatenating strings

Sometimes tou want to split data on a certain character:

![split](./pics_05_data_cleaning/fig14.png)
*<sub>Figure 14: Split on a character.</sub>*

The TEXTSPLIT function can handle this:

![split](./pics_05_data_cleaning/fig15.png)
*<sub>Figure 15: Split on a character.</sub>*

The reciprocal function is CONCAT.
Here you can see it in action:

![concat](./pics_05_data_cleaning/fig16.png)
*<sub>Figure 16: Concatenate text strings.</sub>*

## Dealing with missing data

Often, data analysts are dealing with missing data in datasets. Data fields may be simply empty, contain a dash (-) or may contain an `#N/A` error. There are various approaches one can take when dealing with missing data. For example, you can throw out all the data for any sample missing one or more data elements. However, be aware that missing data might not be randomly distributed. 

The approaches that can be taken are:
- Delete the samples (rows) with one or more missing data elements;
- Input values for missing data elements;
- Remove a complete variable (column) that has a lot of missing values.

Plain Excel does not have a lot of support to drop rows or columns with missing values. A simple approach would be to create a table, filter the data and then manually delete rows that contain empty values. 

You can find empty cells using the `COUNTBLANK` function:

![countblank](./pics_05_data_cleaning/fig17.png)
*<sub>Figure 17: Counting blank cells.</sub>*

Likewise, it is also possible to count the `#N/A` values:

![count na](./pics_05_data_cleaning/fig18.png)
*<sub>Figure 18: Counting #N/A cells.</sub>*

Or check if they are equal to #N/A using the `ISNA` function:

![count na](./pics_05_data_cleaning/fig19.png)
*<sub>Figure 19: Validate if cell equals #N/A.</sub>*


This is, cumbersome and error prone. You can work with third party add-ons, use VBA script or just use R or Python instead. Both R and Python do have powerful functions to deal with missing data.

In any case, it is best to convert cells with "empty" values (whether it is truly blank, contains a dash or any other character to mark empty) to #N/A. #N/A is the error value of Excel that means "no value is available." To avoid accidentally including empty cells in your calculations, enter #N/A in the cells where you are missing information. (A formula that references a cell that contains #N/A will return the #N/A error value). Read more about #N/A [here](https://support.microsoft.com/en-gb/office/na-function-5469c2d1-a90c-4fb5-9bbc-64bd9bb6b47c#:~:text=Returns%20the%20error%20value%20%23N,empty%20cells%20in%20your%20calculations.).

Use simply find and replace to insert #N/A in "empty" cells.


![dealing with na](./pics_05_data_cleaning/fig20.png)
*<sub>Figure 20: The `SUM` function still works, ignoring missing data.</sub>*

As you can see, the `SUM` function still works. This might look appealing at first sight, but it also can cause a lot of troubles when you deal with larger datasets. It masks missing data!

So convert to #N/A:

![dealing with na](./pics_05_data_cleaning/fig21.png)
*<sub>Figure 21: The `SUM` function does not work when #N/A is included.</sub>*

As a result, the `SUM` function does not work. It does notify you that there are missing data. Now you can deal with the #N/A using the `SUMIF` function:

![dealing with na](./pics_05_data_cleaning/fig22.png)
*<sub>Figure 22: The `SUMIF` function does work when #N/A is included.</sub>*

In the above example, `<>` is a shorthand for the `NOT` operator. So the formula reads as: Only sum cells that are not equal to #N/A and ignore the #N/A's. This is a strategy that is very similar to what is used in R and Python. Your are dealing with missing data in an explicit way instead of implicit.

>Like many things in real life, datasets are often imperfect. Very often, data points will be missing. This is just reality and there is not much that you can do about the fact that you will encounter missing data. What is important though, is how you deal with missing data. Make it explicit that data is missing in your analysis and deal with it in a transparent way.


---


>This web page is distributed under the terms of the Creative Commons Attribution License which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
>Creative Commons License: CC BY-SA 4.0.

