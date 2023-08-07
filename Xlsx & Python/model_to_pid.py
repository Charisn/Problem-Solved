import pandas as pd

# Load the Excel file
xls = pd.ExcelFile('new_products.xlsx')

dfs = pd.read_excel(xls, sheet_name=None)

id_mapping = dfs['Products'].set_index('model')['product_id'].to_dict()

for sheet_name in ['AdditionalImages', 'ProductOptionValues', 'ProductFilters', 'ProductOptions']:
    dfs[sheet_name]['product_id'] = dfs[sheet_name]['product_id'].map(id_mapping).fillna(dfs[sheet_name]['product_id'])

with pd.ExcelWriter('new_products.xlsx') as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
