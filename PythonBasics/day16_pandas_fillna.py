import pandas as pd 

machines_df = pd.read_csv("machines.csv")
assignments_df = pd.read_csv("assignments.csv")

merged_df = pd.merge(machines_df , assignments_df , how="left",
                     left_on="name", right_on="machine_name")

merged_df["technician_name"] = merged_df["technician_name"].fillna("ยังไม่มีช่าง")

print("ช่างที่ได้รับงานแล้ว")
print(merged_df[["name","technician_name"]])

unassigned_count = len(merged_df[merged_df["technician_name"] == "ยังไม่มีช่าง"])

print("unassigned_count")
print(unassigned_count)
print(merged_df["technician_name"].isna().sum())