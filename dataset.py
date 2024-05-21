import pandas as pd
from datetime import datetime

# Les donnees brutes sous forme de liste de dictionnaires
data = [
    {"id": 1, "name": "John Doe", "birthdate": "1987-05-24", "purchase_date": "2021/12/01", "amount_paid": "$1,234.56", "email": "john.doe@example.com"},
    {"id": 2, "name": "Jane Smith", "birthdate": "1992-08-17", "purchase_date": "12-15-2021", "amount_paid": "USD 999.99", "email": "jane.smith#example.com"},
    {"id": 3, "name": "Alice Johnson", "birthdate": "April 4, 1985", "purchase_date": "2020-05-21", "amount_paid": "Â£750", "email": "alice@example.co.uk"},
    {"id": 4, "name": "Bob Brown", "birthdate": "03/12/1990", "purchase_date": "21 May 2020", "amount_paid": "1300â‚¬", "email": "bob.brown at example.com"},
    {"id": 5, "name": "Eve White", "birthdate": "1995-07-30", "purchase_date": "2022-01-03", "amount_paid": "â‚¹80,000", "email": "eve.white@example.com"},
    {"id": 6, "name": "Frank Black", "birthdate": None, "purchase_date": "2020-07-15", "amount_paid": "1500", "email": "frank@example.com"},
    {"id": 7, "name": "Charlie Green", "birthdate": "1991-09-05", "purchase_date": "Not Available", "amount_paid": "45.67 USD", "email": "charlie.green@example.com"},
    {"id": 8, "name": "Daisy Blue", "birthdate": "August 14 1990", "purchase_date": "14-08-2021", "amount_paid": "$2,000.50", "email": "daisy.blue[at]example.com"},
    {"id": 9, "name": "George Red", "birthdate": "01-12-1983", "purchase_date": "01/12/21", "amount_paid": "1750 CAD", "email": "george.red@example.com"},
    {"id": 10, "name": "Hannah White", "birthdate": "1984/05/06", "purchase_date": "15/Dec/2021", "amount_paid": "Â¥200000", "email": "hannah.white@example.com"}
]

# Conveti done yo en un DataFrame Pandas
df = pd.DataFrame(data)

# Conveti kolon "birthdate" en format de date
df['birthdate'] = pd.to_datetime(df['birthdate'], errors='coerce')

# pour extraire les montants numériques
df['amount_paid'] = df['amount_paid'].replace('[^\\d.]', '', regex=True).astype(float)

# afiche du DataFrame 
print(df)
