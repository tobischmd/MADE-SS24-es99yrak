# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation between population densitiy and air polution

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Is the air quality dependant from the population density in the surrounding area

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Air polution is an important problem, because it not only affects the contribution to climate change, but also the health of the environment and the people living in a given area.
This projects analyzes the correlation between population density and air polution, by combining both data sets and analysing them. The results can give insights into which air pollutants are more or less effected by the population density.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: PopulationDensity
* Metadata URL: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html
* Data URL: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.xlsx?__blob=publicationFile
* Data Type: XLSX

This datasource gives inside into the population density by "Landkreis"


### Datasource1: Airpolution
* Metadata URL: https://www.umweltbundesamt.de/daten/luft/luftdaten/jahresbilanzen/eJxrWpScv9BwUWXqEiMDI2MAMLAFtA==
* Data URL: https://www.umweltbundesamt.de/api/air_data/v3/annualbalances/csv?component=1&year=2023&lang=de
* Data Type: CSV

This datasource gives the data from the measuring stations in germany. In this case it is the datasource for particulate matter, but you can get many different values from this datasource for example CO or SO2
## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Determine which air pollutants should be considered
2. Select the corresponding data sources
3. Clean the data by filtering only the data needed
4. Create a way to associate the measuring stations to the corresponding "Landkreis"es
5. Build the Data Pipeline
6. Analyze the output and build visualisations
7. Analyze the output by looking and the research question
8. Finish the project and finalyze the analysis and gather a conclusion
