def transform_data(products, customers, sales):
    joined_data = sales.merge(products, left_on='product_id', right_on='id') \
                              .merge(customers, left_on='customer_id', right_on='id')
    relevant_data = joined_data[['product_id', 'customer_id', 'reason', 'sale_time', 'name', 'first_name', 'last_name', 'speciality', 'age', 'phone_number', 'address', 'city']]
    return relevant_data
