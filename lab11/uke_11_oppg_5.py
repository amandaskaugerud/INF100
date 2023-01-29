from decimal import *

def read_file(path):
    with open(path, "rt", encoding='utf-8') as f:
        return f.read()

def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""
    price_dict = {}
    prices_file = read_file(prices_filename)
    cash_register_file = read_file(cash_register_filename)
    
    total_list_with_tuple = []
    for groceries_bought in cash_register_file.splitlines():
        bought_tuple = tuple()
        action, b_grocery = groceries_bought.split(";")
        if action == "buy":
            bought_tuple = bought_tuple + (b_grocery,)
    print(bought_tuple)
    for groceries_store in prices_file.splitlines():
        s_grocery, price = groceries_store.split(";")
        price_dict[s_grocery] = float(price)


receipt_content("lab11\prices.txt", "lab11\cash_register.txt")

# def receipt(prices_filename, cash_register_filename):
#     """Construct a receipt of the cash register events,
#     given the store prices."""

#     # get receipt content from receipt_content()
#     purcases_returns, total, vat, payment, change = receipt_content(
#         prices_filename, cash_register_filename
#     )

#     # the formatted lines of the receipt
#     receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]

#     for nr, item, price in purcases_returns:
#         receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")

#     receipt_lines.append(f"Total: {total}")
#     receipt_lines.append(f"Of which VAT: {vat:.2f}")
#     receipt_lines.append(f"Payment: {payment}")
#     receipt_lines.append(f"Change {change}")

#     # add some dividers
#     max_len = max(len(line) for line in receipt_lines)
#     divider = "-" * max_len
#     receipt_lines.insert(1, divider)
#     receipt_lines.insert(-4, divider)
#     receipt_lines.insert(-2, divider)

#     return "\n".join(receipt_lines)
