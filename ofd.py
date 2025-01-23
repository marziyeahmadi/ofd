from pulp import LpMaximize, LpProblem, LpVariable, lpSum
import pandas as pd

products = [1, 2, 3, 4]
stations = [1, 2]
price_levels = [1]  #without RM
total_capacity = [800, 760, 720, 680, 640, 600, 560, 520, 480, 440, 400, 360, 320, 280, 240, 200]
prices = [10, 11, 12, 13]
dine_in_demand = [100, 80, 100, 80]
ofd_demand = [100, 80, 100, 80]

model = LpProblem("No_RM_Revenue_Maximization", LpMaximize)

x_dine_in = LpVariable.dicts("x_dine_in", products, lowBound=0, cat="Integer")
x_ofd = LpVariable.dicts("x_ofd", products, lowBound=0, cat="Integer")

# objective function: Max Revenue
model += lpSum(prices[i - 1] * (x_dine_in[i] + x_ofd[i]) for i in products)

no_rm_results = []

for capacity in total_capacity:
    # cap constraint
    model.constraints.clear()
    model += lpSum(x_dine_in[i] + x_ofd[i] for i in products) <= capacity  # ظرفیت کل

    # demand constraint
    for i in products:
        model += x_dine_in[i] <= dine_in_demand[i - 1]
        model += x_ofd[i] <= ofd_demand[i - 1]

    model.solve()

    # results
    dine_in_quantity = sum(x_dine_in[i].value() for i in products)
    dine_in_revenue = sum(x_dine_in[i].value() * prices[i - 1] for i in products)

    ofd_quantity = sum(x_ofd[i].value() for i in products)
    ofd_revenue = sum(x_ofd[i].value() * prices[i - 1] for i in products)

    total_quantity = dine_in_quantity + ofd_quantity
    total_revenue = dine_in_revenue + ofd_revenue
    net_revenue = dine_in_revenue + (ofd_revenue * 0.7)  # commission 30%

    no_rm_results.append([
        capacity,
        dine_in_quantity, dine_in_revenue,
        ofd_quantity, ofd_revenue,
        total_quantity, total_revenue,
        net_revenue
    ])

# table
table_3 = pd.DataFrame(no_rm_results, columns=[
    "Total Capacity",
    "Dine-in Avg. Quantity", "Dine-in Avg. Revenue",
    "OFD Avg. Quantity", "OFD Avg. Revenue",
    "Total Avg. Quantity", "Total Avg. Revenue",
    "Avg. Net Revenue"
])

# excel
output_file = "Table_3_No_RM_Pricing.xlsx"
table_3.to_excel(output_file, index=False)

print(f"The results of Table 3 were successfully saved in the file '{output_file}'.")
print(table_3)