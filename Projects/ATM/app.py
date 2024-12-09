from flask import Flask, render_template, request, redirect, url_for
from atmmodule import ATM

app = Flask(__name__)

# Initialize the ATM with a sample account holder and balance
atm = ATM("Nawal D", 10000)


@app.route("/")
def index():
    holder = atm.account_holder  # Get the account holder's name from the ATM object
    return render_template("index.html", account_holder=holder)

@app.route("/check_balance")
def check_balance():
    balance = atm.check_balance()
    return render_template("balance.html", balance=balance)

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        amount = float(request.form["amount"])
        atm.deposit(amount)
        return redirect(url_for("check_balance"))
    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        amount = float(request.form["amount"])
        result = atm.withdraw(amount)
        if result:
            return redirect(url_for("check_balance"))
        else:
            return render_template("withdraw.html", error="Insufficient funds.")
    return render_template("withdraw.html")

@app.route("/transaction_history")
def transaction_history():
    history = atm.show_transaction_history()
    return render_template("history.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)
