from databricks.sdk.runtime import spark
from my_project import taxis
from pyspark.sql import DataFrame


def test_find_all_taxis():
    results = taxis.find_all_taxis()
    assert results.count() > 5
