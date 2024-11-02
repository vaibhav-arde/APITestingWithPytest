from pprint import pprint

from woocommerce import API

wcapi = API(
    # url="http://localhost:10003/wp-json/wc/v3/products", #Here we dont need complete path as we are using woocommerce package.
    url="http://localhost:10003",
    consumer_key="ck_bcee3bd76c4a11a63a471e476afb179650c12f24",
    consumer_secret="cs_cc59b9dbb914559285c306d94b40587f40fe3a33",
    version="wc/v3"
)

r = wcapi.get("products")
pprint(r.json())

