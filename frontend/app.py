# import streamlit as st
# import requests
# import pandas as pd

# API_URL = "http://127.0.0.1:8000"

# st.title("💰 Expense Tracker")

# # Add Expense Form
# st.subheader("Add Expense")
# amount = st.number_input("Amount", min_value=0.0, format="%.2f")
# category = st.text_input("Category")
# date = st.date_input("Date")
# notes = st.text_area("Notes")

# if st.button("Add Expense"):
#     res = requests.post(f"{API_URL}/add_expense", params={
#         "amount": amount,
#         "category": category,
#         "date": str(date),
#         "notes": notes
#     })
#     st.success(res.json()["message"])

# # View Expenses
# st.subheader("All Expenses")
# res = requests.get(f"{API_URL}/get_expenses")
# data = res.json()

# if data:
#     df = pd.DataFrame(data)
#     st.dataframe(df)

#     # Summary Chart
#     summary = df.groupby("category")["amount"].sum().reset_index()
#     st.bar_chart(summary.set_index("category"))

import streamlit as st
import requests
from datetime import date

BACKEND_URL = "http://127.0.0.1:8000"

st.title("💰 Expense Tracker")

# Add new expense
st.header("➕ Add Expense")
item = st.text_input("Item")
amount = st.number_input("Amount", min_value=0.0, step=0.5)
expense_date = st.date_input("Date", value=date.today())

if st.button("Save Expense"):
    payload = {"item": item, "amount": amount, "date": str(expense_date)}
    res = requests.post(f"{BACKEND_URL}/add_expense/", json=payload)
    if res.status_code == 200:
        st.success("Expense added successfully ✅")
    else:
        st.error(f"Error: {res.text}")

# Show all expenses
st.header("📊 All Expenses")
res = requests.get(f"{BACKEND_URL}/expenses/")
if res.status_code == 200:
    expenses = res.json()
    if expenses:
        st.table(expenses)
    else:
        st.info("No expenses yet.")
else:
    st.error("Failed to fetch expenses")

# Daily total
st.header("📅 Daily Total")
day = st.date_input("Select Date", value=date.today(), key="daily")
res = requests.get(f"{BACKEND_URL}/daily_total/{day}")
if res.status_code == 200:
    st.write(f"Total for {day}: ₹ {res.json()['total']}")
else:
    st.error("Failed to fetch daily total")

# Monthly total
st.header("🗓️ Monthly Total")
year = st.number_input("Year", min_value=2000, max_value=2100, value=date.today().year)
month = st.number_input("Month", min_value=1, max_value=12, value=date.today().month)
res = requests.get(f"{BACKEND_URL}/monthly_total/{year}/{month}")
if res.status_code == 200:
    st.write(f"Total for {month}/{year}: ₹ {res.json()['total']}")
else:
    st.error("Failed to fetch monthly total")
