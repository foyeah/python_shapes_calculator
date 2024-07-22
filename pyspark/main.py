from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.master("local").appName("Products and Categories").getOrCreate()

products_data = [("p1", "Product A"), ("p2", "Product B"), ("p3", "Product C")]
categories_data = [("c1", "Category 1"), ("c2", "Category 2")]
product_category_data = [("p1", "c1"), ("p1", "c2"), ("p2", "c1")]

products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])

categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])

product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

def get_product_category_pairs_and_unassigned_products(products_df, categories_df, product_category_df):
    product_with_category_df = products_df.join(product_category_df, "product_id", "left")
    product_with_category_names_df = product_with_category_df.join(categories_df, "category_id", "left")
    product_category_pairs_df = product_with_category_names_df.select("product_name", "category_name")
    unassigned_products_df = product_category_pairs_df.filter(col("category_name").isNull()).select("product_name")
    return product_category_pairs_df, unassigned_products_df

product_category_pairs_df, unassigned_products_df = get_product_category_pairs_and_unassigned_products(products_df, categories_df, product_category_df)

product_category_pairs_df.show()
unassigned_products_df.show()

spark.stop()


# Пример

# +------------+-------------+
# |product_name|category_name|
# +------------+-------------+
# |   Product A|   Category 1|
# |   Product A|   Category 2|
# |   Product B|   Category 1|
# |   Product C|         null|
# +------------+-------------+

# +------------+
# |product_name|
# +------------+
# |   Product C|
# +------------+

# В этом примере:
#     Продукт "Product A" принадлежит к категориям "Category 1" и "Category 2".
#     Продукт "Product B" принадлежит к категории "Category 1".
#     Продукт "Product C" не принадлежит ни к одной категории.