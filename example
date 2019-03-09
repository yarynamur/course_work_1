from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjE3ZWZmZjFhMGJkMmI2ZjQ0ZjcwMDdjMGVjNjA4ZDQw'
fundamentals_api = intrinio_sdk.FundamentalsApi()
identifier = 'DIS'
statement_code = 'income_statement'  # str | The statement code
fiscal_year = 2017  # int | The fiscal year
fiscal_period = 'FY'  # str | The fiscal period
try:
    api_response = fundamentals_api.lookup_fundamental(identifier, statement_code, fiscal_year, fiscal_period)
    with open('outputfile.json', 'w') as outf:
        outf.write(str(api_response).replace("\'", "\"").replace('None', '"None"').replace(
            'False', '"False"').replace("datetime.date", "\"datetime.date").replace(")", ")\""))
except ApiException as e:
    print("Exception when calling IndexApi->get_economic_index_by_id: %s\n" % e)
