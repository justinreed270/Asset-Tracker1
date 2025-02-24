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

# Save inventory to CSV
def save_to_csv(df, filename='inventory.csv'):
    df.to_csv(filename, index=False)
    print(f"\nInventory saved to {filename}")

# Load inventory from CSV
def load_from_csv(filename='inventory.csv'):
    try:
        # Try to read existing CSV file
        return pd.read_csv(filename)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print(f"No existing inventory file found or empty file. Creating new inventory.")
        # Create and save a new empty inventory
        new_inventory = create_inventory()
        save_to_csv(new_inventory, filename)
        return new_inventory


def main():
    inventory = load_from_csv(filename="inventory.csv")

    #examples
    inventory = add_item(inventory, "laptop", 10,)
    inventory = add_item(inventory, "mouse", 6)
    inventory = add_item(inventory, "keyboard", 37,)

    display_inventory(inventory)

    # update inventory
    #inventory = update_quantity(inventory, 1, 298)
   # print("\nAfter updating laptop quantity:")
    #display_inventory(inventory)

    #Remove an item
    #inventory = remove_item(inventory, 2)


    save_to_csv(inventory)

if __name__ == "__main__":
    main()