import pandas as pd

new_options = pd.read_excel('new_options.xlsx', sheet_name='OptionValues')
new_products = pd.read_excel('new_products.xlsx', sheet_name='ProductOptionValues')

mapping = new_options.set_index('old_value')['option_value_id'].to_dict()

new_products['option_value_id'] = new_products['option_value_id'].map(mapping).fillna(new_products['option_value_id'])

with pd.ExcelWriter('new_products.xlsx') as writer:
    new_products.to_excel(writer, sheet_name='ProductOptionValues', index=False)
