import json
import os
import csv  # Import the csv module

# User info
name = input("What is your name? ")
print("Welcome " + name + " to your net worth calculator.")
print("Let's start by calculating your assets.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")

# JSON dump
def save_to_json_file(data):
    json_filename = "networth.json"
    json_file_location = f"/storage/emulated/0/download/Net Worth/{json_filename}"
    os.makedirs(os.path.dirname(json_file_location), exist_ok=True)
    counter = 1
    while os.path.exists(json_file_location):
        json_file_location = f"/storage/emulated/0/download/Net Worth/net_worth({counter}).json"
        counter += 1
    with open(json_file_location, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(name + f" your JSON file has been saved in the Download folder.")

# TXT dump
def save_to_txt_file(data):
    txt_filename = "networth.txt"
    txt_file_location = f"/storage/emulated/0/download/Net Worth/{txt_filename}"
    os.makedirs(os.path.dirname(txt_file_location), exist_ok=True)
    counter = 1
    while os.path.exists(txt_file_location):
        txt_file_location = f"/storage/emulated/0/download/Net Worth/networth({counter}).txt"
        counter += 1
    
    content = f"Net Worth Summary for {data['name']}\n\n"
    content += "Assets:\n"
    for asset, value in data['assets'].items():
        content += f"- {asset.capitalize()}: K {value}\n"
    
    total_assets = sum(data['assets'].values())
    content += f"\nTotal Assets: K {total_assets:.2f}\n"
    
    content += "\nLiabilities:\n"
    for liability, value in data['liabilities'].items():
        content += f"- {liability.capitalize()}: K {value}\n"
    
    total_liabilities = sum(data['liabilities'].values())
    content += f"\nTotal Liabilities: K {total_liabilities:.2f}\n"
    content += f"\nNet Worth: K {data['net worth']:.2f}\n"
    
    with open(txt_file_location, "w") as txt_file:
        txt_file.write(content)
    print(name + f" your TXT file has been saved in the Download folder.")

# CSV dump
def save_to_csv_file(data):
    csv_filename = "networth.csv"
    csv_file_location = f"/storage/emulated/0/download/Net Worth/{csv_filename}"
    os.makedirs(os.path.dirname(csv_file_location), exist_ok=True)
    counter = 1
    while os.path.exists(csv_file_location):
        csv_file_location = f"/storage/emulated/0/download/Net Worth/networth({counter}).csv"
        counter += 1
    
    with open(csv_file_location, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["Category", "Item", "Value"])
        # Write assets
        for asset, value in data['assets'].items():
            writer.writerow(["Asset", asset.capitalize(), value])
        # Write liabilities
        for liability, value in data['liabilities'].items():
            writer.writerow(["Liability", liability.capitalize(), value])
        # Write net worth
        writer.writerow(["Net Worth", "", data['net worth']])
    
    print(name + f" your CSV file has been saved in the Download folder.")

def calculate_net_worth():
    # Input assets
    cash = get_float_input("Cash: K")
    bank = get_float_input("Bank: K")
    
    
    # Calculate total assets
    assets = cash + bank

    print("Let's now calculate your liabilities.")
    debts = get_float_input("Debts: K")
    loans = get_float_input("Loans: K")
    
    # Calculate total liabilities
    liabilities = debts + loans

    # Calculate net worth
    net_worth = assets - liabilities
    print(name + ", your net worth is K", net_worth)
    if net_worth > 0:
        print(name + " you've a positive net worth.")
    else:
        print(name + " you've a negative net worth.")

    # Data to save
    data = {
        "name": name,
        "assets": {
            "cash": cash,
            "bank": bank,
        },
        "liabilities": {
            "debts": debts,
            "loans": loans,
        },
        "net worth": net_worth
    }

    # Ask the user for their preferred format
    print(name + " choose a file format to save your data:")
    print("Enter 1 to save in JSON") # JSON option 
    print("Enter 2 to save in TXT")  # TXT option 
    print("Enter 3 to save in CSV")  # CSV option
    choice = input("Enter the number of your choice: ")
    if choice == '1':
        save_to_json_file(data)
    elif choice == '2':
        save_to_txt_file(data)
    elif choice == '3':
        save_to_csv_file(data)
    else:
        print("Please select 1, 2, or 3")

# Call your main function
calculate_net_worth()
