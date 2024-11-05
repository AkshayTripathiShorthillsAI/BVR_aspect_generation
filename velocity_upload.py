import pandas as pd
import requests
import json
import numpy as np

# Read the Excel file
excel_file = "/home/shtlp_0170/Desktop/BVR/Aspect_generation/llama_Aspects_29_July_2024.csv"
df = pd.read_csv(excel_file)

# Replace infinite values with NaN and fill NaN with empty string
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna("", inplace=True)

# Remove '{X%}' from tag_line column and strip leading/trailing whitespaces from all columns
df['tag_line'] = df['tag_line'].str.replace(r'\{X%\}', '').str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Replace '{X%}' and '{Y%}' with '{X}' and '{Y}' respectively in the 'mixed_title' column
df['mixed_title'] = df['mixed_title'].str.replace(r'\{X%\}', '{X}').str.replace(r'\{Y%\}', '{Y}')

payload_list = df.to_dict(orient='records')
print(payload_list)
api_url = "https://dpl.bestviewsreviews.com/api/create_and_update_aspect_and_tagline"

auth_token = "5854f65c66d0a011629c0a7c0fa0466d2a8ff204"

headers = {
    "Authorization": f"Token {auth_token}",
    "Content-Type": "application/json"
}

try:
    response = requests.post(api_url, json=payload_list, headers=headers)
    if response.status_code == 201:
        print("Data successfully sent to the API.")
    else:
        print("Error:", response.json())
except Exception as e:
    print("Error occurred while making the API call:", str(e))


    # category_slug	old_aspect	new_aspect	tag_line	definition	mixed_title