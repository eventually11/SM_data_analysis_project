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


## Relationship
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



# Project scope
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


