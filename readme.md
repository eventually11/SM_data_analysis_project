- [Data Introduction](#data-introduction)
- [Project Content](#project-content)



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
mysql_conn: write your query into queries.sql then run the mysql_conn. 

It will generate a query result query_results.csv 



# Project scope
