import pandas as pd

data = pd.read_csv("machine.data")

data.columns = ["vendorName", "model", "myct", "mmin", "mmax", "cach","chmin","chmax", "prp", "erp"]

data.to_csv("machine.csv", index = None, header=True)