-- Creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER desc_items_after_order_trigger
AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
