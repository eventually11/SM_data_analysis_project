CREATE TABLE saas_partner_task (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    tenant INT UNSIGNED NOT NULL,
    `order` INT UNSIGNED,
    sender INT UNSIGNED NOT NULL,
    hub INT UNSIGNED NOT NULL,
    zone VARCHAR(10),
    flow INT UNSIGNED NOT NULL,
    task_pool INT UNSIGNED NOT NULL,
    partner INT UNSIGNED NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    `date` DATE NOT NULL,
    time_slot TIME NOT NULL,
    `type` ENUM('type1', 'type2', 'type3') NOT NULL,
    service_time TINYINT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);


select * from sm.saas_partner_task;


SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE saas_partner_order_type;
SET FOREIGN_KEY_CHECKS = 1;

-- Create the table
CREATE TABLE saas_partner_order_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code INT NOT NULL,
    type_name VARCHAR(255) NOT NULL,
    languages VARCHAR(255) NOT NULL

);

-- Insert a row with random values
INSERT INTO saas_partner_order_type (code, type_name, languages) VALUES (6595, 'XY', 'XYD');


select * from sm.saas_partner_order_type;

-- CREATE TABLE saas_partner_order (
--     id INT NOT NULL PRIMARY KEY,  -- Primary key, integer, not null
--     tenant INT NOT NULL,  -- Integer, not null
--     flow INT NOT NULL,  -- Integer, not null
--     sender VARCHAR(255) NOT NULL,  -- String, not null
--     hub VARCHAR(255) NOT NULL,  -- String, not null
--     dispatch_pool INT NOT NULL,  -- Integer, not null
--     vehicle_type JSON NOT NULL,  -- List of strings, stored as JSON
--     start_time DATETIME,  -- Datetime, nullable
--     end_time DATETIME,  -- Datetime, nullable
--     title VARCHAR(255) NOT NULL,  -- String, not null
--     route_description VARCHAR(255) NOT NULL,  -- String, not null
--     tags VARCHAR(255),  -- String, nullable
--     overview VARCHAR(255) NOT NULL,  -- String, not null
--     content VARCHAR(255) NOT NULL,  -- String, not null
--     type JSON NOT NULL,  -- Dictionary with code, type_name, and name, stored as JSON
--     start VARCHAR(255),  -- String, nullable
--     end VARCHAR(255),  -- String, nullable
--     service_fee FLOAT,  -- Float, nullable
--     start_task_validation VARCHAR(255) NOT NULL,  -- String, not null
--     end_task_validation VARCHAR(255) NOT NULL,  -- String, not null
--     status_group INT NOT NULL  -- Integer, not null
-- );

CREATE TABLE saas_partner_order (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT ,
    tenant INT,
    flow INT,
    sender VARCHAR(255),
    hub VARCHAR(255),
    dispatch_pool INT,
    vehicle_type VARCHAR(255),
    start_time DATETIME,
    end_time DATETIME,
    title VARCHAR(255),
    route_description VARCHAR(255),
    tags VARCHAR(255),
    overview VARCHAR(255),
    content VARCHAR(255),
    type VARCHAR(255),
    start VARCHAR(255),
    end VARCHAR(255),
    service_fee DECIMAL(10, 2),
    start_task_validation VARCHAR(255),
    end_task_validation VARCHAR(255),
    status_group INT
);


select * from sm.saas_partner_order;



CREATE TABLE sm.saas_work_order (
    work_id INT PRIMARY KEY, 
    tenant INT, -- tenant id

    sender VARCHAR(500), -- saas_sender type

    flow VARCHAR(500), -- saas_flow type

    hub VARCHAR(500), -- saas_hub type

    zone INT, -- zone ID

    start_date DATE, -- pickup date
    start_time VARCHAR(10), -- pickup time or time range
    end_date DATE, -- delivery date
    end_time VARCHAR(10), -- delivery time or time range

    start VARCHAR(500), -- common_simple_contact or common_address or sm_sender_address type
    end VARCHAR(500), -- common_simple_contact or common_address or sm_sender_address type

    items VARCHAR(500), -- saas_work_order_item_basic_box or saas_work_order_item_basic_description type

    `references` VARCHAR(500), -- saas_order_reference type

    fee VARCHAR(500), -- saas_work_order_fee_basic_parcel or saas_work_order_fee_basic_parcel_item type

    reviewed VARCHAR(20), -- common_yn_not_applicable type

    scheduled_time TIMESTAMP, -- TYPE_TIMESTAMP type
    auto_publish_time TIMESTAMP, -- TYPE_TIMESTAMP type

    status_code VARCHAR(20), -- saas_work_order_status type

    estimation VARCHAR(500), -- saas_work_order_estimation type
    distance VARCHAR(500), -- saas_work_order_distance type

    channel VARCHAR(20) -- saas_work_order_channel_type type
);




CREATE TABLE saas_partner_task (
    task_id INT PRIMARY KEY, -- task id
    tenant INT, -- tenant id

    order INT, -- partner order id, optional

    sender VARCHAR(500), -- sender id

    hub INT, -- hub managing the task

    zone VARCHAR(50), -- zone id or postal code, optional

    flow INT, -- flow id

    task_pool INT, -- task pool id

    partner INT, -- partner id

    title VARCHAR(255), -- task title

    content TEXT, -- content of the task

    date DATE, -- task date

    time_slot VARCHAR(50), -- time slot for the task, optional

    type VARCHAR(50), -- task type

    service_time INT, -- service time, default is 0

    start VARCHAR(500), -- ds_start_address type, stored as VARCHAR
    end VARCHAR(500), -- ds_end_address type, stored as VARCHAR

    service_fee VARCHAR(500), -- common_service_fee type, stored as VARCHAR

    items VARCHAR(500), -- saas_work_order_item_basic_box or saas_work_order_item_basic_description type, stored as VARCHAR

    start_task_validation VARCHAR(500), -- saas_flow_standard_task_validation_sequence or saas_flow_tenant_task_validation_sequence type, stored as VARCHAR
    end_task_validation VARCHAR(500), -- saas_flow_standard_task_validation_sequence or saas_flow_tenant_task_validation_sequence type, stored as VARCHAR

    status_code VARCHAR(50), -- saas_partner_task_status type

    status_group VARCHAR(50) -- saas_partner_task_status_group type
);
