from operator import index

import pandas as pd
from datetime import    datetime
# create simple inventory
def create_inventory():
    data = {
        'item_id': [],
        'name': [],
        'quantity': [],
    }
    return pd.DataFrame(data)

# Add new items
def add_item(df,name, quantity):
    new_item = {
        'item_id' : len(df) + 1,
        'name' : name,
        'quantity': quantity,
        'last_updated' : datetime.now()
    }
    return pd.concat([df, pd.DataFrame([new_item])], ignore_index=True)

# Update item amount
def update_quantity(df, item_id, new_quantity):
    if item_id in df['item_id'].values:
        df.loc[df['item_id'] == item_id, 'quantity'] = new_quantity
        df.loc[df['item_id'] == item_id, 'last_updated'] = datetime.now()
    return df

#remove item
def remove_item (df, item_id):
    return df[df['item_id'] != item_id].reset_index(drop=True)

#Show inventory
def display_inventory(df):
    print("\nCurrent Inventoyr:")
    print(df.to_string(index=False))
