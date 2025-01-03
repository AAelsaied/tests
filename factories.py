from faker import Faker

fake = Faker()

def fake_product():
    return {
        'name': fake.product_name(),
        'category': fake.word(),
        'price': fake.random_number(),
        'availability': fake.boolean()
    }
