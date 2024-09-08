from faker import Faker
import time
import polars as pl

start = time.perf_counter()
fake = Faker()
num_rows = 1000000

for i in range(250):
    df = pl.DataFrame(
        {
            "ix": range(num_rows),
        }
    )
    df = df.with_columns([
        pl.lit(fake.first_name()).alias("first_name"),
        pl.lit(fake.last_name()).alias("last_name"),
        pl.lit(fake.address().replace("\n", ", ")).alias("address"),
        pl.lit(fake.date_of_birth().strftime("%Y-%m-%d")).alias("date_of_birth"),
    ])
    df = df.drop('ix')
    # df.head(2)
    df.write_csv(f"./data/personal_data_{i}.csv", separator=",")

stop = time.perf_counter()
elapsed = stop - start
print(f"creating dataframe with {num_rows} rows took {elapsed}")

