import pandas as pd
df = pd.read_csv("C:/Users/Nila/Desktop/pythonprojects/ancient_empires_viz/data/ancientempires.csv")

#renaming columns of the table to camel case
df = df.rename(columns = { "Empire Name": "empire_name", "Start Year (BCE)": "start_year_bce", "End Year (BCE)":"end_year_bce","Capital": "capital","Latitude":"latitude","Longitude": "longitude", "Region": "region", "Notes":"notes"})
#enforce data types
df["empire_name"]= df["empire_name"].astype(str)
df["start_year_bce"]  = df["start_year_bce"].astype(int)
df["end_year_bce"] = df["end_year_bce"].astype(int)
df["capital"] = df["capital"].astype(str)
df["latitude"] = df["latitude"].astype(float)
df["longitude"] = df["longitude"].astype(float)
df["region"] = df["region"].astype(str)
df["notes"] = df["notes"].astype(str)
print(df.info())
df.to_csv("data/clean_empire_data.csv",index = False)
print("dataset cleaned and stored in data folder")