# Selenium Python Automation Framework 🚀
This repository contains a basic Selenium automation framework built using **Python**.  
It is designed as a beginner-friendly yet professional setup for learning, practice, and interview preparation.

---

## 📌 Project Overview
- Language: **Python 3.12.6**
- Automation Tool: **Selenium WebDriver**
- Browser: **Google Chrome (v143)**
- Framework Type: Basic Selenium structure (can be extended to PyTest)

---

## 📂 Folder Structure

```text
selenium_python_automation/
│
├── automation/
│   ├── tests/
│   │   └── test_cart.py
│   └── venv/   (ignored using .gitignore)
│
├── project-2-shopping-cart/
├── .gitignore
└── README.md


⚙️Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/meenakshiadiandra199905-ui/selenium_python_automation.git
cd selenium_python_automation

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install selenium webdriver-manager

▶️ How to Run the Test
cd automation/tests
python test_cart.py

✔ Chrome browser will open
✔ Test executes successfully

🧪 Sample Test Included
test_cart.py
Launches Chrome browser
Uses webdriver-manager
Basic Selenium automation flow

📝 Git Configuration Notes
venv/ is excluded using .gitignore
Clean commits following industry standards

🌱 Future Enhancements
Convert framework to PyTest
Add explicit waits
Add assertions & reporting
Page Object Model (POM)
CI integration

👩‍💻Author

Meenakshi Adiandra
MCA | Software Testing | Selenium Automation


---

## ✅ STEP 3: Save the file

Press **Ctrl + S**  
Close the editor

---

## ✅ STEP 4: Check Git Status

In your terminal (already in repo root):

```bash
git status

You should see:

Untracked files:
  README.md


Updated README with setup instructions and author details

----

## 🧪 Automation Day B – Add Product to Cart (Real Website)
**Website Used:** https://www.saucedemo.com

### Scenario Automated
- Launch Chrome browser
- Login using valid credentials
- Add a product to cart
- Navigate to cart page
- Verify product is added successfully

### Test File
### Key Concepts Used
- Selenium WebDriver with Python
- WebDriver Manager for browser setup
- Locators (ID, Class Name)
- Basic assertions for validation

### Result
✅ Product successfully added to cart and verified

