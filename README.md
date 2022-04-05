# Power Master Learning

You are a Data Analyst at PowerMasterLearning, a retail chain that sells electronics and home appliances with stores spread across several cities in Brazil. The company started its operation in Brazil in 2012 and operates in the four states of the Southeast region plus the states of Paraná and Bahia.

# Business Problem

The company is setting up its sales strategy for the next year and needs to know which of the manufacturers of the products sold has the best sales performance. The objective is to discard manufacturers whose products have few sales and try to negotiate better conditions with the main manufacturers. In parallel with this, the company would like to have different views of sales made in the last 4 years (period from 2012 to 2015). 
It should be possible to segment sales reports by different information and from different angles. This information will support the company's strategies for the coming year. 

The data was extracted from different tables of a transactional database and as the company will use the reports every month, some consultants recommended the use of a Data Warehouse.

There will be several meetings to define the sales strategy and reports can be extracted on demand, according to the managers' needs. Because of this, you must create a data model that allows you to extract reports at any time and that allows you to extract data from different views and angles. The data must be fed into a consolidated database, which will be updated monthly with new data. Your job is to make it happen!

# Project Planing

## Final Users
- CEO
- Decision Makers

## Available Data
We have at our disposal some csv files with information about sales, sellers, stores, products and customers.

## Solution
The solution conceived for this case was to model the data available in a data warehouse to facilitate the extraction of data on demand for the generation of dashboards and reports and to facilitate the monthly update of the data.

First of all, with SQL language we define the general structure of dw. We define the schema, establish the constraints, all according to the business rules.

Second, two python scripts were developed to do the ETL, one script loads the csv tables, cleans them and then saves them in a folder, the second script loads this clean data directly into the built data warehouse through mysqlconnector with python.

Finally, with the data clean and available in the DW, we can connect Power BI to this database and thus generate the dashboards and reports requested by the business area.

As new data is generated monthly, our python script will run every month when the new csvs files become available, and update the data warehouse.

## Integration and Use
Decision makers will use dashboards and reports to make the best decisions based on available data, the dashboads will avaible in the Power BI Cloud and the reports will be send by email.

## Sucess Criteria
Stakeholders must be able to easily see and understand reports and dashboards so they can make better data-driven decisions. That is, our project must be able to generate intelligence for the business and decision making.
