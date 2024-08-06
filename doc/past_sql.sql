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

