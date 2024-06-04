import sqlite3 as sq

database = sq.connect(".\\data\\population.sqlite")

p = database.cursor()

p.execute('''
          CREATE TABLE finalData (
                Country TEXT,
                PolutionType TEXT,
                Polution REAL,
                Density REAL
          );
          ''')

p.execute('''
          WITH PolutionByCountry AS (
              SELECT Pollutant as Pollutant, "Country Label" as Country, avg(Value) as Value
              FROM polution 
              GROUP BY Pollutant, "Country Label"
          ),
          JoinedData AS (
              SELECT p.Country as Country, p.Pollutant as Pollutant, p.Value as Polution, g.Density as Density
                FROM PolutionByCountry p, population g
                WHERE p.Country = trim(g.Country)
          )
          
          INSERT INTO finalData SELECT
           p.Country AS Country, p.Pollutant as PolutionType, p.Polution as Polution, p.Density as Density
          FROM JoinedData p
          ''')
