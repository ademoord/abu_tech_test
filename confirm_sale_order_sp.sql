CREATE OR REPLACE FUNCTION confirm_sales_order() RETURNS VOID AS
$$
DECLARE
    order_rec RECORD;
BEGIN
    FOR order_rec IN
        SELECT * FROM sale_order WHERE state = 'draft'
    LOOP
        UPDATE sale_order SET state = 'sale' WHERE id = order_rec.id;
        INSERT INTO stock_picking (origin, picking_type_id)
        VALUES (order_rec.name, your_picking_type_id);
    END LOOP;
END;
$$
LANGUAGE plpgsql;
