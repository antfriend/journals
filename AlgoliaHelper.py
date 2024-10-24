# ============================================
#
# This module is not yet modified for use in Journals
#
# 
# Solution helper code, loose, prototype form
#
# ============================================
import pandas as pd
from datetime import datetime, date
import json
from algoliasearch.search_client import SearchClient

def initialize_Algolia():
    import os

    # set environment variables before trying this step 
    app_id = os.getenv('APP_ID')
    api_key = os.getenv('API_KEY')
    set_Algolia_params(app_id,api_key,'EmployeesAndClaims')

def set_Algolia_params(app_id, api_key, index_name):
    global _app_id
    global _api_key
    global _index_name
    _app_id = app_id
    _api_key = api_key
    _index_name = index_name
    init_Algolia()

def save_df_to_algolia(df):
    init_Algolia()
    json_str = "[\n "
    for record in df.to_json(orient='records', lines=True).splitlines():
        json_str += record + ',\n'
    
    # Find the index of the last comma
    last_comma_index = json_str.rfind(',')

    # Remove the last comma using slicing
    if last_comma_index != -1:
        json_str = json_str[:last_comma_index] + json_str[last_comma_index+1:]

    json_str += ']'
    # print(jsonl_str)
    new_data = json.loads(json_str)
    index.save_objects(new_data)

def init_Algolia():
    global client
    global index 
    client = SearchClient.create(_app_id, _api_key)
    index = client.init_index(_index_name)
    
def load_Algolia_employees(num_records):

    results = index.search('', {'getRankingInfo': False,
                                'attributesToHighlight': [],
                                 'facetFilters': [
                                    [
                                        'type:dependents',
                                        'type:employees',
                                        'type:retirees'
                                    ]
    ],'hitsPerPage': num_records})['hits']
    # Convert the results to a DataFrame
    df = pd.DataFrame(results)
    return df

def load_Algolia_claims(num_records):
    results = index.search('', {'getRankingInfo': False,
                                'attributesToHighlight': [],
                                 'facetFilters': [['type:claims']],'hitsPerPage': num_records})['hits']
    # Convert the results to a DataFrame
    df = pd.DataFrame(results)
    return df

def query_Algolia(query, filters, num_records):
    
    # Define your query and filters
    # query = 'your search query'
    # filters = 'attribute:value AND another_attribute:value2'

    # Perform the search with the filter
    results = index.search(query, {
        'getRankingInfo': False,
        'filters': filters,
        'attributesToHighlight': [],
        'hitsPerPage': num_records})['hits']
    
    # Convert the results to a DataFrame
    df = pd.DataFrame(results)
    # df.to_json('employees.jsonl', orient='records', lines=True)
    return df