import csv

    
def main():
    for num in range(3):
        with open(f"data/daily_sales_data_{num}.csv") as f:
            reader = csv.DictReader(f)
            with open("pink_morsels_sales_data.csv", "a", newline='') as df:
                headers = ["sales", "date", "region"]
                writer = csv.DictWriter(df, fieldnames=headers)
                if num == 0:
                    writer.writeheader() 
                for row in reader:
                    if row['product'] == "pink morsel":
                        data = get_data(row)
                        writer.writerow(data)

                    
def get_data(row):
    data = {}
    price, qty = convert_to_float(row["price"]), convert_to_float(row["quantity"])
    data["sales"] = f"${price * qty:.02f}"
    data["date"] = row["date"]
    data["region"] = row["region"]
    
    return data

    
def convert_to_float(price):
    return float(price.strip("$"))

if __name__ == "__main__":
    main()