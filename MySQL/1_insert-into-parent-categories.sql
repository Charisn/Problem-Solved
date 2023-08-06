INSERT INTO oc3xtbl_product_to_category (product_id, category_id)
SELECT ptc.product_id, c.parent_id
FROM oc3xtbl_product_to_category ptc
INNER JOIN oc3xtbl_category c ON ptc.category_id = c.category_id
WHERE c.parent_id != 0
AND NOT EXISTS (
    SELECT 1
    FROM oc3xtbl_product_to_category ptc2
    WHERE ptc2.product_id = ptc.product_id
    AND ptc2.category_id = c.parent_id
)