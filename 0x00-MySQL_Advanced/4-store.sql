-- creating a stored trigger
CREATE TRIGGER decrease_value AFTER INSERT ON items
FOR EACH ROW
	BEGIN
SET NEW.quantity = NEW.quantity - 1;
END
