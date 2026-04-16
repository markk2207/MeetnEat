from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

# Sample menu
menu = [
    {"id": 1, "name": "Pizza", "price": 200},
    {"id": 2, "name": "Burger", "price": 120},
    {"id": 3, "name": "Pasta", "price": 150},
]

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/add/<int:item_id>')
def add_to_cart(item_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(item_id)
    session.modified = True
    return redirect('/')

@app.route('/cart')
def cart():
    cart_items = []
    total = 0

    for item_id in session.get("cart", []):
        for item in menu:
            if item["id"] == item_id:
                cart_items.append(item)
                total += item["price"]

    return render_template("cart.html", items=cart_items, total=total)

@app.route('/order', methods=["POST"])
def order():
    session.pop("cart", None)
    return render_template("order.html")

if __name__ == '__main__':
    app.run(debug=True)
