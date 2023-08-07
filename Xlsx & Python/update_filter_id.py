import pandas as pd

new_options = pd.read_excel('new_filters.xlsx', sheet_name='Filters')
new_products = pd.read_excel('new_products.xlsx', sheet_name='ProductFilters')

mapping = new_options.set_index('old')['filter_id'].to_dict()

new_products['filter_id'] = new_products['filter_id'].map(mapping).fillna(new_products['filter_id'])

with pd.ExcelWriter('new_products.xlsx') as writer:
    new_products.to_excel(writer, sheet_name='ProductOptionValues', index=False)
