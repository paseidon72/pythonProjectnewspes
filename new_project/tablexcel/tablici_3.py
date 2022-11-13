import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

df = pd.read_excel("excel-comp-data.xlsx")
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
df["Jan"].sum(), df["Jan"].mean(), df["Jan"].min(), df["Jan"].max()
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()
df_sum = pd.DataFrame(data=sum_row).T
df_sum = df_sum.reindex(columns=df.columns)
df_final = df.append(df_sum, ignore_index=True)
df_final.tail(3)
df.head()
state_to_code = {"VERMONT": "VT", "GEORGIA": "GA", "IOWA": "IA", "Armed Forces Pacific": "AP", "GUAM": "GU",
                 "KANSAS": "KS", "FLORIDA": "FL", "AMERICAN SAMOA": "AS", "NORTH CAROLINA": "NC", "HAWAII": "HI",
                 "NEW YORK": "NY", "CALIFORNIA": "CA", "ALABAMA": "AL", "IDAHO": "ID",
                 "FEDERATED STATES OF MICRONESIA": "FM", "Armed Forces Americas": "AA",
                 "DELAWARE": "DE", "ALASKA": "AK", "ILLINOIS": "IL", "Armed Forces Africa": "AE",
                 "SOUTH DAKOTA": "SD", "CONNECTICUT": "CT", "MONTANA": "MT", "MASSACHUSETTS": "MA", "PUERTO RICO": "PR",
                 "Armed Forces Canada": "AE", "NEW HAMPSHIRE": "NH", "MARYLAND": "MD", "NEW MEXICO": "NM",
                 "MISSISSIPPI": "MS", "TENNESSEE": "TN", "PALAU": "PW", "COLORADO": "CO",
                 "Armed Forces Middle East": "AE", "NEW JERSEY": "NJ", "UTAH": "UT", "MICHIGAN": "MI",
                 "WEST VIRGINIA": "WV", "WASHINGTON": "WA", "MINNESOTA": "MN", "OREGON": "OR", "VIRGINIA": "VA",
                 "VIRGIN ISLANDS": "VI", "MARSHALL ISLANDS": "MH", "WYOMING": "WY", "OHIO": "OH",
                 "SOUTH CAROLINA": "SC", "INDIANA": "IN", "NEVADA": "NV", "LOUISIANA": "LA",
                 "NORTHERN MARIANA ISLANDS": "MP", "NEBRASKA": "NE", "ARIZONA": "AZ", "WISCONSIN": "WI",
                 "NORTH DAKOTA": "ND", "Armed Forces Europe": "AE", "PENNSYLVANIA": "PA", "OKLAHOMA": "OK",
                 "KENTUCKY": "KY", "RHODE ISLAND": "RI", "DISTRICT OF COLUMBIA": "DC", "ARKANSAS": "AR",
                 "MISSOURI": "MO", "TEXAS": "TX", "MAINE": "ME"}


def convert_state(row):
    if pd.notnull(row['state']):
        abbrev = process.extractOne(row["state"], choices=state_to_code.keys(), score_cutoff=80)
        if abbrev:
            return state_to_code[abbrev[0]]
    return np.NaN


df_final.insert(6, "abbrev", np.NaN)
df_final.head()
df_final['abbrev'] = df_final.apply(convert_state, axis=1)
df_final.tail()
df_sub = df_final[["abbrev", "Jan", "Feb", "Mar", "total"]].groupby('abbrev').sum()



def money(x):
    return "${:,.0f}".format(x)


formatted_df = df_sub.applymap(money)
sum_row = df_sub[["Jan", "Feb", "Mar", "total"]].sum()
df_sub_sum = pd.DataFrame(data=sum_row).T
df_sub_sum = df_sub_sum.applymap(money)
final_table = formatted_df.append(df_sub_sum)
final_table = final_table.rename(index={0: "Total"})

# print(df.head())
# print('*' * 50)
print(final_table)
print('*' * 50)

