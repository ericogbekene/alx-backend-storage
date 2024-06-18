-- creating a stored trigger
--CREATE TRIGGER decrease_value AFTER INSERT ON orders
--FOR EACH ROW
--	BEGIN
--UPDATE items(quantity)
--SET NEW.items.quantity = NEW.items.quantity - 1;
--END
--TRIGGER TO UPDATE ITEMS
DELIMETER $$
CREATE TRIGGER decrease_trigger AFTER INSERT ON orders
BEGIN
UPDATE items SET quantity = quantity - NEW.number

END;

DELIMETER 
