# Contents

- [Data Introduction](#data-introduction)
- [Project Content](#project-content)
- [Project scope](#project-scope)



# Data Introduction
## Table Structure
saas_partner_order.d.ts

    saas_partner_order
  
    saas_partner_order_type


saas_partner_task

    saas_partner_task
    
    saas_partner_task_event_log
    
    saas_partner_task_partner_fee
    
    saas_partner_task_validation_step
    

saas_work_order


    
  
## Table description

saas_partner_order: Main order table, contains each order information 

saas_partner_order_type: Dim table, order type

saas_partner_task：Represents individual tasks within a partner order. Each task details the specific actions required

saas_partner_task_event_log：Logs events and status changes for tasks

saas_partner_task_partner_fee：Tracks financial details specific to the task 

saas_partner_task_validation_step： Details validation steps

saas_work_order: work order detials, each person each delivery


## Process
Order collection----Task distribution-----Work completion


## Table Relationship
The order id is unique.

An order may have more than one tasks.

A sender has only one work id but may contain more than one tasks.
![image](https://github.com/eventually11/SM_data_analysis_project/blob/main/SM_ERD.jpg)


# Project Content
- mysql_conn: write your query into queries.sql then run the mysql_conn. 

It will generate a query result query_results.csv 

- data generation: generation fake data

- OSRM API：Return distance information

- open street API : address search

- BI dashboard：https://app.powerbi.com/view?r=eyJrIjoiOWI3OWViZTktMWEwYy00OTVlLWI2ODgtNmVjMGU4NGMzMzRmIiwidCI6IjlmMjQ4NzY3LThlMWEtNDJmMy04MzZmLWMwOTJhYjk1ZmY3MCJ9

- 
![image](https://github.com/eventually11/SM_data_analysis_project/blob/main/overview.png)
![image](https://github.com/eventually11/SM_data_analysis_project/blob/main/map.png)
![image](https://github.com/eventually11/SM_data_analysis_project/blob/main/daily%20monitoring.png)

The BI dashboard shown in the images can be described as follows:

    1. Order Overview Dashboard:Displays key metrics like update time, order volume, YTD orders, and completion rate.
    
    2. Delivery Range and Order Distribution Map: This heatmap visualizes delivery ranges and order density, highlighting high-activity zones.
    
    3. Daily Order Performance Dashboard:Includes order status breakdown, hourly distribution, order volume by status, and service fee comparisons across different delivery stages.

# Project Scope
- Build a visual dashboard to show the important metrics.

- Order volume detection: The daily order volume needs to show three peaks throughout the day; otherwise, it indicates a potential issue with the system or the business operations

- Delivery metrics detection: The delivery distance and time for orders with the same starting and ending points should follow a normal distribution. If these metrics do not conform to a normal distribution, it could indicate a potential issue.

- Cost analysis: Calculate the delivery cost for each order based on the distance, time, and fee fields to identify high-cost orders

- courier performace analysis：Through delivery time, order completion rate, customer feedback to hierarchy level.if the delivery time is too long, it could be a potential issue.

- Predicting Canceled and Failed Orders：Unsuccessful orders, such as canceled or failed deliveries, can increase operational costs. To mitigate this, we can develop predictive models to identify problematic orders in advance.


- Map visualization Order heatmap

- food-delivery operation review  real-time dashboard

- how many order is waiting for partner to accept
- how many order is waiting for courier to pick up
- how many order is on the way
- how many order is delivered



# Overall Flow of the Project

This module contains the analytical tools and methods for data monitoring, prediction, alerting, and visualization. It uses the data stored in SQLite and applies various analytical techniques to derive insights, monitor trends, and forecast future outcomes.

- Define Data Structure (MockOrderDataStructured): Establishes the fields, types, and rules for the data.
- Generate Data (MockOrderDataGenerator): Creates synthetic data according to the defined structure.
- Import Data (MockOrderDataImporter): Inserts the generated data into a SQLite database.
- Analyze Data (SM_Data_Analysis_Project): Performs monitoring, alerting, prediction, and visualization based on the stored data.

## Related Git
- MockOrderDataStructured: https://github.com/eventually11/MockOrderDataStructured

This module is responsible for defining the structure of the data, including the fields and data types. The configuration file could be changed for different creation.


- MockOrderDataGenerator: https://github.com/eventually11/MockOrderDataGenerator

This module relies on the structure provided by MockOrderDataStructured and generates the data that will later be imported into the database by MockOrderDataImporter.

- MockOrderDataImporter: https://github.com/eventually11/MockOrderDataImporter

This module takes the generated data from MockOrderDataGenerator and imports it into a SQLite database. It includes functionality to connect to SQLite, manage tables, and insert the generated data. It acts as the bridge between data generation and data storage, ensuring that the mock data is persisted in a database. Imports the data generated by MockOrderDataGenerator and stores it in a SQLite database. This stored data is then available for further analysis.
