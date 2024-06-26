import sqlite3, pandas, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect(".\\data\\population.sqlite")
sqlCO = """select Polution, Density from finalData where PolutionType = 'CO' order by Density asc"""
sqlNO2 = """select Polution, Density from finalData where PolutionType = 'NO2' order by Density asc"""
sqlSO2 = """select Polution, Density from finalData where PolutionType = 'SO2' order by Density asc"""
sqlO3 = """select Polution, Density from finalData where PolutionType = 'O3' order by Density asc"""

data = pandas.read_sql(sqlCO, conn)
dataCO = pandas.read_sql(sqlCO, conn)
dataNO2 = pandas.read_sql(sqlNO2, conn)
dataSO2 = pandas.read_sql(sqlSO2, conn)
dataO3 = pandas.read_sql(sqlO3, conn)

fig, axs = plt.subplots(4)
# make linear regression for each pollutant
regCO = LinearRegression().fit(dataCO['Density'].values.reshape(-1, 1), dataCO['Polution'].values)
bCO = regCO.intercept_
mCO = regCO.coef_[0]
axs[0].axline((0, bCO), slope=mCO, color='r', label='CO')

regNO2 = LinearRegression().fit(dataNO2['Density'].values.reshape(-1, 1), dataNO2['Polution'].values)
bNO2 = regNO2.intercept_
mNO2 = regNO2.coef_[0]
axs[1].axline((0, bNO2), slope=mNO2, color='b', label='NO2')

regSO2 = LinearRegression().fit(dataSO2['Density'].values.reshape(-1, 1), dataSO2['Polution'].values)
bSO2 = regSO2.intercept_
mSO2 = regSO2.coef_[0]
axs[2].axline((0, bSO2), slope=mSO2, color='g', label='SO2')

regO3 = LinearRegression().fit(dataO3['Density'].values.reshape(-1, 1), dataO3['Polution'].values)
bO3 = regO3.intercept_
mO3 = regO3.coef_[0]
axs[3].axline((0, bO3), slope=mO3, color='y', label='O3')

fig.suptitle('Polution vs Density')
axs[0].plot(dataCO['Density'], dataCO['Polution'], 'ro', label='CO')
axs[1].plot(dataNO2['Density'], dataNO2['Polution'], 'bo', label='NO2')
axs[2].plot(dataSO2['Density'], dataSO2['Polution'], 'go', label='SO2')
axs[3].plot(dataO3['Density'], dataO3['Polution'], 'yo', label='O3')

axs[0].set_xlim(0, 400)
axs[1].set_xlim(0, 400)
axs[2].set_xlim(0, 400)
axs[2].set_ylim(0, 50)
axs[3].set_xlim(0, 400)

for ax in axs:
    ax.set_xlabel('Density (people/mi²)')

axs[0].set_ylabel('CO (µg/m³)')
axs[1].set_ylabel('NO2 (µg/m³)')
axs[2].set_ylabel('SO2 (µg/m³)')
axs[3].set_ylabel('O3 (µg/m³)')

fig.set_size_inches(7, 7)

plt.savefig('.\\project\\Plots\\PolutionVsDensity.png')
