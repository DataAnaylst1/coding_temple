CREATE TABLE IF NOT EXISTS bank(
	customer_id INT NOT NULL, -- NOT NULL alerts SQL that this category cannot have an empty value, this is a constraint
    account_number INT NOT NULL,
    balance NUMERIC(10,2),
    age INT,
    PRIMARY KEY (customer_id),
    CHECK (balance >=0), -- The check is a conditional statement that tells SQL to make sure the balance is never under 0
    CONSTRAINT account_eligibility CHECK (age >= 18 AND balance >=0), -- CONSTRAINT ensure a denial or error occurs if the check within the constraint is not met
    CONSTRAINT pri_key_bank PRIMARY KEY (customer_id, account_number)
    );
    
    ALTER TABLE bank
    ADD first_name VARCHAR(255);
    
    ALTER TABLE bank
    ADD last_name VARCHAR(255);
    
    ALTER TABLE bank
    MODIFY COLUMN last_name INT;
    
    ALTER TABLE bank
    DROP COLUMN first_name;
    
    ALTER TABLE bank
    DROP COLUMN laast_name;
    SELECT *
    FROM bank;
    select *
    from bank;
    ALTER TABLE bank
    DROP COLUMN last_name;
    -- Inserts HOW TO ADD DATA INTO A TABLE
    INSERT INTO bank
    VALUES (02, 1567894465, 10000.00, 17);
    -- Updates
    UPDATE bank
    SET balance = 1200000.00
    WHERE age = 18;