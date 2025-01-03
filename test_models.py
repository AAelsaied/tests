def test_read_product(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    retrieved_product = Product.objects.get(name="Sample Product")
    self.assertEqual(retrieved_product.name, "Sample Product")

def test_update_product(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    product.price = 120
    product.save()
    updated_product = Product.objects.get(name="Sample Product")
    self.assertEqual(updated_product.price, 120)

def test_delete_product(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    product.delete()
    with self.assertRaises(Product.DoesNotExist):
        Product.objects.get(name="Sample Product")


def test_list_all_products(self):
    product1 = Product.objects.create(name="Product 1", category="Electronics", price=100, availability=True)
    product2 = Product.objects.create(name="Product 2", category="Home", price=50, availability=False)
    all_products = Product.objects.all()
    self.assertEqual(len(all_products), 2)


def test_find_by_name(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    found_product = Product.objects.get(name="Sample Product")
    self.assertEqual(found_product.name, "Sample Product")


def test_find_by_category(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    found_products = Product.objects.filter(category="Electronics")
    self.assertEqual(len(found_products), 1)

def test_find_by_availability(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    available_products = Product.objects.filter(availability=True)
    self.assertEqual(len(available_products), 1)

def test_find_by_availability(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    available_products = Product.objects.filter(availability=True)
    self.assertEqual(len(available_products), 1)


