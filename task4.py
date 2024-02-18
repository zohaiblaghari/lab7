Item_dict = {'item_1': 45.50, 'item_2': 35, 'item_3': 41.30, 'item_4': 55, 'item_5': 24}

def find_highest_price_item(item_dict):
    max_price = max(item_dict.values())
    highest_price_items = [item for item, price in item_dict.items() if price == max_price]
    return highest_price_items, max_price

def find_smallest_price_item(item_dict):
    min_price = min(item_dict.values())
    smallest_prices_items = [item for item, price in item_dict.items() if price == min_price]
    return smallest_prices_items, min_price

if __name__ == "__main__":
    highest_price_items, max_price = find_highest_price_item(Item_dict)
    print(f"Item(s) with highest price: {highest_price_items}, price: {max_price}")

    smallest_price_items, min_price = find_smallest_price_item(Item_dict)
    print(f"Item(s) with smallest price: {smallest_price_items}, price: {min_price}")
