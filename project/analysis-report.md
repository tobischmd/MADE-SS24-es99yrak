---
papersize: a4
geometry: margin=2.5cm
fontsize: 12pt
header-includes:
    - \linespread{1.5}
---

# Analysis Reprt

## Introduction

Climate change is a pressing global issue. An often-cited argument is that individual lifestyles can significantly contribute to an environmentally friendly economy. This premise leads to an intriguing question: "Does the concentration of air pollutants vary according to the population density of a country". Intuitively, one might expect that more densely populated countries would emit more air pollutants, given the amount of human activities. This report aims to investigate this question by analyzing the hypothesis of a correlation between the popolation density and air pollutant concentrations of a country. 

## Used Data

**Population Density Data:**
This dataset includes the poluation density of all countries worldwide, presented in a structured CSV file. Despite being last updated in 2018, it accurately reflects real-world data, covering nearly all countries.

**Pollution Data:**
This dataset provides extensive data on multiple air pollutants, across 65 countires, avaible in a CSV file. While some records contain anomalies like negative or unusually high values, these issues can be adressed in the data pipeline. 

The data for this project originates from open sources and has been further transformed to meet the specific needs of the project. The air pollution data is updated every time the pipeline is executed. The data is trainsformed inside of a datapipeline. Through a Jayvee pipeline the data is downloads and tranforms the pollution data by filtering only necessary columns and ensuring that the data is within a reasonbale range. Also only records with specific units are kept. It also processes the pre-downloaded dataset containting the population density data, by filtering out the needed columns. Finally, a Python script creates the final datatset by averaging the pollutants values for each country and converting units where necessary. The Python script also joins the two datasets into a final dataset. The final dataset includes information on air pollutant concentrations and population density for various countries.

I would like to acknowledge [OpenAQ](https://public.opendatasoft.com/explore/dataset/openaq/information/) for providing access to the air pollution data used in this project.

## Analysis

The analysis involved several steps to examine the correlation between population density and air pollutant concentrations:

1. **Data visualization:** A python script (plot.py) was used to create plots of the air pollutants concentrations against the population densities for each pollutant 
2. **Linear regression:** In the same script, a linear regression was performed, in order to see a trend in the given data
3. **Slope interpretation** The slope of the regression lines was printed for each pollutant. The slope indicates the rate of change as a numerical value, which is more useful for analysis

### Results

The output of executing the pipeline and the plotting script on July the 2nd produced the plot that can be seen in figure 1: 

![plots](./project/PlotJuly2.png)

Notably, the slopes were either very small or negative, suggesting a weak or nonexistent correlation.
    
+ **CO**: 0.0286
+ **NO2**: 0.0048
+ **SO2**: -0.0064
+ **O3**: 0.0082

## Conclusions

The analysis indicates that population density does not have a significant impact on air pollutant concentrations. This finding contradicts the initial hypothesis, suggesting that other factors may play a more critical role in determining air quality.

### Critical Reflection

Several factors could explain the weak correlation found in this analysis: 

1. **Data limitations:** The simplification of averaging pollutant concentrations across monitoring stations may obscure local variations and lead to inaccurate conclusions. Additionally, some data points appeared unrealistic, potentially indicating data quality issues.
2. **Industrial impact:** The analysis did not account for industrial activities, which likely have a substantial impact on air pollution. Future studies could explore the correlation between the number of industrial sites and pollutant levels.
3. **Geographical and environmental factors:** Factors such as topography, climate, and vegetation can also influence air quality, and these were not considered in this analysis.

In order to conclude the completed analysis. The given hypothesis that the concentration of air pollutants varies according to the population density of a country seems to be false, which is also a meaningful results of this analysis.
