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

saas_work_order: work order detials, each person each delivery


## Process
Order collection----Task distribution-----Work completion


## Relationship
The order id is unique.

An order may has more than one tasks.
A sender has only one work id but may included more than one tasks.


# Content
mysql_conn: write your query into queries.sql then run the mysql_conn. 
It will generate a query result query_results.csv 
