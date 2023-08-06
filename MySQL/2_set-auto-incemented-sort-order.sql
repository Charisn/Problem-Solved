UPDATE oc3xtbl_option_value AS t
JOIN (
  SELECT option_id, option_value_id,
    CASE
      WHEN option_id != @prev_option_id THEN @sort_order := 1
      ELSE @sort_order := @sort_order + 1
    END AS new_sort_order,
    @prev_option_id := option_id
  FROM oc3xtbl_option_value
  CROSS JOIN (SELECT @sort_order := 1, @prev_option_id := NULL) AS vars
  ORDER BY option_id, option_value_id
) AS s ON t.option_id = s.option_id AND t.option_value_id = s.option_value_id
SET t.sort_order = s.new_sort_order;