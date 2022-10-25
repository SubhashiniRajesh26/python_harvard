import pandas as pd

def as_dataframe(file_name):
    df = pd.read_csv(file_name)
    print(df.head(5))

as_dataframe('web_scrape.csv')