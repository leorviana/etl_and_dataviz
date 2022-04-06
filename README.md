# ETL and Data Visualization

ETL, which stands for extract, transform and load, is a data integration process that combines data from multiple data sources into a single, consistent data store that is loaded into a data warehouse or other target system.

ETL provides the foundation for data analytics and machine learning workstreams. Through a series of business rules, ETL cleanses and organizes data in a way which addresses specific business intelligence needs, like monthly reporting, but it can also tackle more advanced analytics, which can improve back-end processes or end user experiences.

But an ETL process does not mean anything by itself, it only serves to help us generate value for the company with the accumulation of an asset as important as data, and to generate value with data we need to extract knowledge from it. From this, as defined in the later section, we will generate some reports and dashboards that help in making decisions based on the data.

# Business Problem

You are a Data Analyst at PowerMasterLearning, a retail chain that sells electronics and home appliances with stores spread across several cities in Brazil. The company started its operation in Brazil in 2012 and operates in the four states of the Southeast region plus the states of Paraná and Bahia.

The company is setting up its sales strategy for the next year and needs to know which of the manufacturers of the products sold has the best sales performance. The objective is to discard manufacturers whose products have few sales and try to negotiate better conditions with the main manufacturers. In parallel with this, the company would like to have different views of sales made in the last 4 years (period from 2012 to 2015). 
It should be possible to segment sales reports by different information and from different angles. This information will support the company's strategies for the coming year. 

The data was extracted from different tables of a transactional database and as the company will use the reports every month, some consultants recommended the use of a Data Warehouse.

There will be several meetings to define the sales strategy and reports can be extracted on demand, according to the managers' needs. Because of this, you must create a data model that allows you to extract reports at any time and that allows you to extract data from different views and angles. The data must be fed into a consolidated database, which will be updated monthly with new data. Your job is to make it happen!

# Project Planing

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

## Final Users
- StakeHolders
- Other Data Scientists and Data Analystis

## Available Data
We have at our disposal some csv files with information about sales, sellers, stores, products and customers.

## Tools 
 <p>
  <ul>
    <li><a href="https://www.python.org/">Python 3.9</a></li>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
    <li><a href="https://www.spyder-ide.org/">Spyder IDE</a></li>
    <li><a href="https://powerbi.microsoft.com/pt-br/">Microsoft Power BI</a></li>
  </ul>
 </p>

# Results

## Data Ware House

After the project is completed, we have a Data Warehouse built and ready for use, with some data already available. Below, we can check the schema of our database:

<p align="left">
  <img src="">
</p>

## Dashboard

<p align="left">
  <img src="">
</p>

## Analysis Report

<p align="left">
  <img src="">
</p>

<p align="left">
  <img src="">
</p>

<p align="left">
  <img src="">
</p>

<p align="left">
  <img src="">
</p>

# Conclusion

From the Data WareHouse and the scripts created we can now update our database monthly, thus updating our reports and dashboards. And from these reports and dashboards, the stackholders will be able to make better decisions about the business. Finally, we managed to develop a solution that helps the company to profit.

## Next Steps

Keep updating the database with more and more data, in order to accumulate as much informational value as possible.

Improve the ETL process, replacing python with specific tools like AirFlow or Pentaho.

## References

Instituição “Data Science Academy”. Disponível em: <https://www.datascienceacademy.com.br/>.
