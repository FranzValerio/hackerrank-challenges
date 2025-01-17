/* Query all columns for all American cities in the CITY table with populations larger than 100,000.
The CountryCode for America is USA. 

The CITY table is described as follows:

|-----CITY-----|
| Field | Type |
|--------------|
| ID |  NUMBER |
| NAME | VARCHAR2(17) |
| COUNTRYCODE | VARCHAR2(3) |
| DISTRICT | VARCHAR2(20) |
| POPULATION | NUMBER | */

SELECT *
    FROM CITY
        WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;