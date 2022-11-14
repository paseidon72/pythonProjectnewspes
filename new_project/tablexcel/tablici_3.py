import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

df = pd.read_excel("excel-comp-data.xlsx") #открываем таблицу во фрейме
df["total"] = df["Jan"] + df["Feb"] + df["Mar"] # добавить столбец с итогами, чтобы показать общие продажи
# за январь, февраль и март.
df["Jan"].sum(), df["Jan"].mean(), df["Jan"].min(), df["Jan"].max() #щоб отримати підсумки за місяць.
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum() #створіть суму для стовпців місяця та підсумку.
df_sum = pd.DataFrame(data=sum_row).T #якщо ви хочете додати підсумки у вигляді рядка.
# Ця T функція дозволяє нам переключати дані з рядків на стовпці.
df_sum = df_sum.reindex(columns=df.columns) #додати відсутні стовпці
df_final = df.append(df_sum, ignore_index=True)  #Тепер відформатований DataFrame,
df_final.tail(3)  # ми можемо додати його до існуючого за допомогою append .
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
#фрагмент кода, нам нужен, отображение имени штата в аббревиатуру.
#функция сопоставления нечеткого текста:
process.extractOne("Minnesotta", choices=state_to_code.keys())
process.extractOne("AlaBAMMazzz", choices=state_to_code.keys(), score_cutoff=80)
def convert_state(row):
    if pd.notnull(row['state']):
        abbrev = process.extractOne(row["state"], choices=state_to_code.keys(), score_cutoff=80)
        if abbrev:
            return state_to_code[abbrev[0]]
    return np.NaN
#В функции мы либо возвращаем допустимое сокращение, либо np.NaN, чтобы у нас были допустимые значения в поле.

df_final.insert(6, "abbrev", np.NaN) #Добавьте столбец в нужном месте и заполните его значениями NaN:
df_final.head()
df_final['abbrev'] = df_final.apply(convert_state, axis=1) #Теперь используем apply для добавления сокращений
# в столбец abbrev:
df_final.tail()
df_sub = df_final[["abbrev", "Jan", "Feb", "Mar", "total"]].groupby('abbrev').sum() #Создание промежуточного итога
# в pandas выполняется с помощью метода groupby:



def money(x): #Затем хотим отобразить данные с обозначением валюты, используя applymap для
    # всех значений в кадре данных:
    return "${:,.0f}".format(x)


formatted_df = df_sub.applymap(money)
sum_row = df_sub[["Jan", "Feb", "Mar", "total"]].sum() #теперь можем получить итоговые значения, как раньше:
df_sub_sum = pd.DataFrame(data=sum_row).T #Преобразуйте значения в столбцы и отформатируйте их:
df_sub_sum = df_sub_sum.applymap(money)
final_table = formatted_df.append(df_sub_sum) #добавьте итоговое значение в DataFrame:
final_table = final_table.rename(index={0: "Total"}) #Вы заметите, что для итоговой строки индекс равен 0.
#Можем изменить это с помощью метода rename:

# print(df.head())
# print('*' * 50)
print(final_table)
print('*' * 50)

