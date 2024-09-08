import polars as pl
from faker import Faker
import os

fake = Faker()
df = pl.read_csv("./data/personal_data_*")
print(df.head(2))

num_rows = df['first_name'].count()
print(num_rows)


df = df.with_columns([
    pl.Series("first_name", [fake.first_name() for _ in range(num_rows)]),
    pl.Series("last_name", [fake.last_name() for _ in range(num_rows)]),
    pl.Series("address", [fake.address() for _ in range(num_rows)]),
])
# df.head(5)
df.write_csv(f"./data/personal_data_modified.csv", separator=",")
