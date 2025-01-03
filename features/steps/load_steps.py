@given('there are some products')
def step_impl(context):
    context.products = [
        {"name": "Product A", "category": "Category 1", "availability": True},
        {"name": "Product B", "category": "Category 2", "availability": False},
    ]
