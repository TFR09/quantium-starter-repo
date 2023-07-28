import csv, os


DATA_DIRECTORY = "./data"
OUTPUT_FILE = "pink_morsels_sales_data.csv"

   
def main():
    with open(OUTPUT_FILE, "w", newline='') as output_f:
        headers = ["sales", "date", "region"]
        writer = csv.DictWriter(output_f, fieldnames=headers)
        writer.writeheader() 
        for data_file in os.listdir(DATA_DIRECTORY):
            with open(f"{DATA_DIRECTORY}/{data_file}") as df:
                reader = csv.DictReader(df)
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