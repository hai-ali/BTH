import http.client as hc
import json

import requests
import json
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession

class APIExtract():

  def __init__(self):
    self.api_udf = udf(self.call_simple_rest_api)

  def call_simple_rest_api(self, url="https://cat-fact.herokuapp.com/facts/"):
    # public REST API from PostMan: https://documenter.getpostman.com/view/8854915/Szf7znEe
    response = requests.get(url)
    return json.loads(response.text)
# Create a list of dictionaries with the URL values
request_params = [
    {"url": "https://cat-fact.herokuapp.com/facts/"},
    {"url": "https://dog.ceo/api/breeds/list/all/"},
    {"url": "https://world.openpetfoodfacts.org/api/v0/product/20106836.json"},
    {"url": "https://world.openfoodfacts.org/api/v0/product/737628064502.json"},
    {"url": "https://openlibrary.org/api/books?bibkeys=ISBN:0201558025,LCCN:93005405&format=json"},
]

spark = SparkSession.builder.appName("RESTAPIExample").getOrCreate()

api_extract_client = APIExtract()
api_extract_client.call_simple_rest_api()

# Create DataFrame from the list of dictionaries
request_df = spark.createDataFrame(request_params)
request_df.show()


response_df = request_df.withColumn('response', api_extract_client.api_udf(col('url')))
response_df.show()


