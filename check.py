import pandas as pd
import os
from groq import Groq
import re
from dotenv import load_dotenv
import csv
import json

class ReviewSnippets:
    def __init__(self):
        self.df_pid = None
        self.features_df = None
        load_dotenv()

    # Function to be used in old case when we are revieving full text
    def get_aspects(self, category_name):
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": '''You are a search-based assistant, which helps to find the revenue of company in USD. Please create a table for the given companies along with their revenues in dollars. Please do not hallucinate, write the value as per some source  only.
                    
                    Provide data in three columns: 1. Company, 2. Revenue (USD), 3. Source(URL).'''
                },
                {
                    "role": "user", 
                    "content": f'''Category Slug: {category_name}''' 
                },
            ],
            model="llama3-70b-8192",
        )

        outputs = chat_completion.choices[0].message.content
        final_response = outputs
        return final_response

if __name__ == "__main__":
    extractor = ReviewSnippets()
    companies = ['NASA Jet Propulsion Laboratory']
    failed_categories = []

    print(extractor.get_aspects('NASA Jet Propulsion Laboratory'))

    # for category in companies:
    #     attempts = 0
    #     while attempts < 5:
    #         try:
    #             extractor.get_aspects(category)
    #             break
    #         except Exception as e:
    #             print(f"Error processing category '{category}' on attempt {attempts + 1}: {e}")
    #             attempts += 1
    #             if attempts == 5:
    #                 failed_categories.append(category)
    #             continue

    # print("The following categories failed after 5 attempts:")
    # print(failed_categories)
