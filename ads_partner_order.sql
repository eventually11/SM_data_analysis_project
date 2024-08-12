SET SESSION sql_mode = '';

CREATE TABLE IF NOT EXISTS ads_partner_order (
    start_time VARCHAR(255),
    end_time VARCHAR(255),
    service_mins INT,
    order_volume INT,
    complete_order_volume INT,
    courier_pick_up INT
);

INSERT INTO ads_partner_order (start_time, end_time, service_mins, order_volume, complete_order_volume, courier_pick_up)
SELECT 
    substr(start_time, 1, 16) AS start_time, 
    substr(end_time, 1, 16) AS end_time,
    FLOOR((unix_timestamp(end_time) - unix_timestamp(start_time)) / 60) AS service_mins,
    COUNT(order_id) AS order_volume,
    SUM(CASE WHEN tags <> 0 THEN 0 ELSE 1 END) AS complete_order_volume,
    SUM(CASE WHEN start_task_validation <> 0 THEN 0 ELSE 1 END) AS courier_pick_up
FROM 
    sm.saas_partner_order
GROUP BY 
    substr(start_time, 1, 16), 
    substr(end_time, 1, 16), 
    FLOOR((unix_timestamp(end_time) - unix_timestamp(start_time)) / 60);
