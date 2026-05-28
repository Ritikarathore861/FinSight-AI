import pandas as pd

data = {
    "Stock": ["TCS", "Infosys", "Reliance"],
    "Price": [3500, 1500, 2800]
}

df = pd.DataFrame(data)

print(df)
