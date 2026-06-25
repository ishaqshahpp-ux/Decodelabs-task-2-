total_spent = 0

print("=== WELCOME TO DECODELABS PROCESSING PHASE ===")
print("Project 2: The Expense Tracker Engine\n")

while True:
    print(f"Current Status -> Total Spent: {total_spent}")
    user_input = input("Enter your expense amount (or type 'exit' to stop): ").strip()
    
    if user_input.lower() == 'exit':
        print(f"\nFinal Closing Statement -> Total Spent: {total_spent}")
        print("Milestone 2 Qualified! Powered by DecodeLabs.")
        break
        
    try:
        expense = int(user_input)
        
        if expense < 0:
            print("Error: Expense amount cannot be negative!")
            continue
            
        total_spent = total_spent + expense
        print(f"Success: {expense} has been added to your tracker.")
        print("-" * 30)
        
    except ValueError:
        print("Invalid Data: Please enter valid numbers only!")
        print("-" * 30)
expense_tracker.py
