

A full-stack web application that allows users to browse food items, add them to a cart, and place orders seamlessly. This project demonstrates backend development, session management, and dynamic rendering using Flask.

---

## 🚀 Features

* 🧾 Dynamic food menu display
* 🛒 Add items to cart (session-based)
* 💰 Real-time cart total calculation
* 📦 Order placement system
* 🔄 Cart state persistence during session
* 🎯 Lightweight and scalable architecture

---

## 🏗️ System Architecture

This application follows a **Model-View-Controller (MVC)** inspired structure:

* **Frontend (View)**: HTML templates rendered using Jinja2
* **Backend (Controller)**: Flask handles routing and business logic
* **Data Layer (Model)**: In-memory data (can be extended to databases)

---

## 🛠️ Tech Stack

| Layer        | Technology              |
| ------------ | ----------------------- |
| Frontend     | HTML, Jinja2            |
| Backend      | Python, Flask           |
| Session Mgmt | Flask Sessions          |
| Deployment   | Localhost / Cloud-ready |

---

## 📂 Project Structure

```
food_app/
│── app.py
│── templates/
│     ├── index.html
│     ├── cart.html
│     └── order.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/food-ordering-system.git
cd food-ordering-system
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔄 Application Flow

1. User visits the homepage
2. Menu items are dynamically displayed
3. User adds items to cart
4. Cart stores item IDs in session
5. Total price is calculated in backend
6. User places order
7. Cart is cleared and confirmation is shown

---

## 📊 Data Handling

* Cart data is stored using Flask session
* Menu is stored as a Python list (temporary)
* No persistent storage (can be upgraded)

---

## 🔐 Future Enhancements

* 🔑 User Authentication (Login/Register)
* 🗄️ Database Integration (SQLite/MySQL)
* 💳 Payment Gateway Integration (Stripe/Razorpay)
* 📱 Responsive UI (Bootstrap/React)
* 📍 Real-time Order Tracking
* 📦 Admin Dashboard for Order Management

---

## 🧪 Testing

Basic testing can be performed by:

* Adding/removing items from cart
* Checking total calculation
* Verifying order placement flow

For advanced testing:

* Use pytest for backend
* Selenium for UI testing

---

## ⚡ Performance Considerations

* Session-based storage reduces DB overhead
* Lightweight routing ensures fast response
* Suitable for small to medium-scale applications

---

## 🌐 Deployment

You can deploy this project on:

* Heroku
* Render
* AWS EC2
* Docker containers

---

## 📸 Screenshots (Optional)

*Add screenshots of your UI here for better presentation.*

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **[Your Name]**

---

## ⭐ Acknowledgements

* Flask Documentation
* Open-source community
