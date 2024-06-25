USE sportswiftdb;
DELIMITER //

CREATE TRIGGER update_blocked_status
BEFORE UPDATE ON customer
FOR EACH ROW
BEGIN
    IF NEW.failed_attempts >= 3 THEN
        INSERT INTO check_blocked (customer_id, blocked) VALUES (NEW.Customer_ID, true);
    END IF;
END;
//

DELIMITER ;