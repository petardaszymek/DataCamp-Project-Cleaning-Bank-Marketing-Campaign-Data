import pandas as pd
import numpy as np

# Start coding here...
#Load data
data = pd.read_csv('bank_marketing.csv')
client = data[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'housing', 'loan']]
campaign = data[['client_id', 'campaign', 'duration', 'pdays', 'previous', 'poutcome', 'y', 'loan', 'day', 'month']]
economics = data[['client_id', 'emp_var_rate', 'cons_price_idx', 'euribor3m', 'nr_employed']]
#Renaming colums
client.rename(columns={'client_id': 'id'}, inplace=True)
campaign.rename(columns={'duration': 'contact_duration', 'previous':'previous_campaign_contacts', 'y':'campaign_outcome', 'poutcome':'previous_outcome', 'campaign':'number_contacts'}, inplace = True)
economics.rename(columns={'euribor3m':'euribor_three_months', 'nr_employed':'number_employed'}, inplace = True)
#Replace
client['education'].replace({'.':'_', 'unknown': np.nan}, inplace=True)
client['job'] = client['job'].str.replace('.', '')
#setting values for campaign
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'success': 1, 'failure': 1, 'nonexistent': np.nan})
campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': 1, 'failure': 1, 'nonexistent': np.nan})
#adding new column
campaign['last_contact_date'] = pd.to_datetime('2022-' + campaign["month"].astype(str) + '-' + campaign["day"].astype(str))
#dropping columns
campaign.drop(columns=['day', 'month'], inplace=True)
#sending dataframes to csv
client.to_csv('client.csv', index=False)
campaign.to_csv('campaign.csv', index=False)
economics.to_csv('economics.csv', index=False)
#SQL queries \client_table
client_table ='''
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    age INT,
    job TEXT,
    marital TEXT,
    education TEXT,
    credit_default BOOLEAN,
    housing BOOLEAN,
    loan BOOLEAN
    );
    
\copy client FROM 'client.csv' DELIMITER ',' CSV HEADER;
'''
#SQL queries \campaign_table
campaign_table = '''
CREATE TABLE campaign (
    campaign_id SERIAL PRIMARY KEY,
    client_id SERIAL REFERENCES client (id),
    number_contacts INT,
    contact_duration INT,
    pdays INT,
    previous_campaign_contacts INT,
    previous_outcome BOOLEAN,
    campaign_outcome BOOLEAN,
    last_contact_date DATE
);

\copy campaign FROM 'campaign.csv' DELIMITER ',' CSV HEADER;
'''
#SQL queries \economics_table
economics_table = '''
CREATE TABLE economics (
    client_id serial REFERENCES client (id),
    emp_var_rate FLOAT,
    cons_price_idx FLOAT,
    euribor_three_months FLOAT,
    number_employed FLOAT
);

\copy economics FROM 'economics.csv' DELIMITER ',' CSV HEADER;
'''
