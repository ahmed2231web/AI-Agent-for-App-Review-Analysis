import os
import pandas as pd
from sqlalchemy import create_engine


# Define file paths
csv_file = "/home/ahmed/Desktop/Desktop/Projects/Pydantic AI/Projects/Agent 2/all_combined.csv"

db_file_path = "/home/ahmed/Desktop/Desktop/Projects/Pydantic AI/Projects/Agent 2/database.db"

# Ensure the directory exists
db_directory = os.path.dirname(db_file_path)
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Load CSV into DataFrame
df = pd.read_csv(csv_file)

# Create SQLAlchemy engine
engine = create_engine(f"sqlite:///{db_file_path}")

# Infer table name from file name
table_name = "dataset"

# Insert data into table
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Data from '{csv_file}' has been imported into the SQLite database successfully.")

