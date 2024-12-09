def cyber():
    a = 10
    class_a = "kingdom"
    print(f"Hello from Cyber Block {class_a}")

# banking model:

user_data = {
    "data": [
        {
            "name": "kannan",
            "account_number": 95,
            "bank_details":{
                "account_type": "savings",
                "balance": 80000,
                "withdraw_limit": 10000
            }
        },
        {
            "name": "anshul",
            "account_number": 40,
            "bank_details":{
                "account_type": "savings",
                "balance": 100000,
                "withdraw_limit": 10000
            }
        },
        {
            "name": "Dhanush",
            "account_number": 68,
            "bank_details":{
                "account_type": "current",
                "balance": 48000,
                "withdraw_limit": 10000
            }
        },
        {
            "name": "vairavel",
            "account_number": 56,
            "bank_details":{
                "account_type": "savings",
                "balance": 62000,
                "withdraw_limit": 10000
            }
        },
    ]
    
}
data = user_data["data"]

def view_balance(acc_num):
    for user in data:
        if user["account_number"] == acc_num:
            balance = user["bank_details"]["balance"]
            print(user["name"],"and your balance is,",balance )
            return balance, 100, 200, "thanks"

# view_balance(56)
# view_balance(95)

def banking():
    print("welcome to Dubai Banking Application")
    acc_num = int(input("Please enter your account number:"))
    is_valid_acc = False
    for value in data:
        if value["account_number"] == acc_num:
            is_valid_acc = True
            response = view_balance(acc_num)
            print(response[-1])
    if is_valid_acc == False:
        print("Invalid account number")

banking()