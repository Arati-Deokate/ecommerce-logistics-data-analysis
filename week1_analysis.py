import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
orders = pd.read_csv("olist_orders_dataset.csv")

# Convert date columns
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col])

# Select delivered orders
delivered = orders[
    orders["order_status"] == "delivered"
].copy()

# Calculate delivery time
delivered["delivery_time_days"] = (
    delivered["order_delivered_customer_date"]
    - delivered["order_purchase_timestamp"]
).dt.total_seconds() / (24 * 60 * 60)

# Calculate delivery delay
delivered["delivery_delay_days"] = (
    delivered["order_delivered_customer_date"]
    - delivered["order_estimated_delivery_date"]
).dt.total_seconds() / (24 * 60 * 60)

# Calculate KPIs
average_delivery_time = delivered["delivery_time_days"].mean()
average_delivery_delay = delivered["delivery_delay_days"].mean()

on_time_orders = (
    delivered["delivery_delay_days"] <= 0
).sum()

total_delivered_orders = len(delivered)

on_time_rate = (
    on_time_orders / total_delivered_orders
) * 100

late_orders = (
    delivered["delivery_delay_days"] > 0
).sum()

late_rate = (
    late_orders / total_delivered_orders
) * 100

# Display results
print("Average Delivery Time:", round(average_delivery_time, 2), "days")
print("Average Delivery Delay:", round(average_delivery_delay, 2), "days")
print("On-Time Orders:", on_time_orders)
print("Total Delivered Orders:", total_delivered_orders)
print("On-Time Delivery Rate:", round(on_time_rate, 2), "%")
print("Late Orders:", late_orders)
print("Late Delivery Rate:", round(late_rate, 2), "%")

# Visualization
plt.figure(figsize=(8, 5))
sns.histplot(
    delivered["delivery_time_days"].dropna(),
    bins=30
)

plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time (Days)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()
