from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

balance = 0.0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    global balance
    data = request.get_json()
    amount = data['amount']
    balance -= amount
    return jsonify({'balance': balance})

@app.route('/add_deposit', methods=['POST'])
def add_deposit():
    global balance
    data = request.get_json()
    amount = data['amount']
    balance += amount
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)


#import tkinter as tk
# import os
# from tkhtmlview import HTMLLabel

# class ChildExpenseTracker:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Child Expense Tracker")

#         self.balance = 0.0
#         self.transactions = []

#         self.html_label=HTMLLabel(root, background="white", html="")
#         self.html_label.pack(expand=True, fill="both")

#         html_file_path = os.path.join("templates","index.html")

#         self.root.geometry("400x400")

#         with open(html_file_path, "r") as html_file:
#             html_content = html_file.read()
#         self.html_label = tk.Label(root, text=html_content)
#         self.html_label.pack(pady=10)

#         # Connect HTML elements to Python
#         self.balance_label = tk.Label(root, text="Balance: $0.00", font=("Helvetica", 16))
#         self.balance_label.pack(pady=10)

#         self.amount_entry = tk.Entry(root, width=20)
#         self.amount_entry.insert(0, "0.00")
#         self.amount_entry.pack(pady=10)

#         self.description_entry = tk.Entry(root, width=30)
#         self.description_entry.insert(0, "Description")
#         self.description_entry.pack(pady=10)

#         self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
#         self.add_expense_button.pack(pady=5)

#         self.add_deposit_button = tk.Button(root, text="Add Deposit", command=self.add_deposit)
#         self.add_deposit_button.pack(pady=5)

#         self.view_transactions_button = tk.Button(root, text="View Transactions", command=self.view_transactions)
#         self.view_transactions_button.pack(pady=5)


#         # Labels
#         self.balance_label = tk.Label(root, text="Balance: $0.00", font=("Helvetica", 16))
#         self.balance_label.pack(pady=10)

#         # Entry widgets
#         self.amount_entry = tk.Entry(root, width=20)
#         self.amount_entry.insert(0, "0.00")
#         self.amount_entry.pack(pady=10)
#         self.description_entry = tk.Entry(root, width=30)
#         self.description_entry.insert(0, "Description")
#         self.description_entry.pack(pady=10)

#         # Buttons
#         self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
#         self.add_expense_button.pack(pady=5)
#         self.add_deposit_button = tk.Button(root, text="Add Deposit", command=self.add_deposit)
#         self.add_deposit_button.pack(pady=5)
#         self.view_transactions_button = tk.Button(root, text="View Transactions", command=self.view_transactions)
#         self.view_transactions_button.pack(pady=5)

#     def add_expense(self):
#         amount = float(self.amount_entry.get())
#         description = self.description_entry.get()
#         if amount <= 0:
#             return
#         self.balance -= amount
#         self.transactions.append(f"Expense: {description} - ${amount:.2f}")
#         self.update_balance_label()

#         # Update the HTML page using JavaScript
#         js_code = f'document.getElementById("balance").innerHTML = "{self.balance:.2f}";'
#         self.root.eval(js_code)

#     def add_deposit(self):
#         amount = float(self.amount_entry.get())
#         description = self.description_entry.get()
#         if amount <= 0:
#             return
#         self.balance += amount
#         self.transactions.append(f"Deposit: {description} - ${amount:.2f}")
#         self.update_balance_label()

#          # Update the HTML page using JavaScript
#         js_code = f'document.getElementById("balance").innerHTML = "{self.balance:.2f}";'
#         self.root.eval(js_code)


#     def view_transactions(self):
#         if not self.transactions:
#             return
#         transactions_window = tk.Toplevel(self.root)
#         transactions_window.title("Transactions")
#         transactions_text = tk.Text(transactions_window)
#         transactions_text.pack()
#         for transaction in self.transactions:
#             transactions_text.insert(tk.END, transaction + "\n")

#         # Update the HTML page using JavaScript
#         js_code = f'document.getElementById("balance").innerHTML = "{self.balance:.2f}";'
#         self.root.eval(js_code)


#     def update_balance_label(self):
#         self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
#         self.amount_entry.delete(0, tk.END)
#         self.amount_entry.insert(0, "0.00")
#         self.description_entry.delete(0, tk.END)
#         self.description_entry.insert(0, "Description")

# def main():
#     root = tk.Tk()
#     app = ChildExpenseTracker(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()