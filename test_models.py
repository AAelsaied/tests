def test_read_product(self):
    product = Product.objects.create(name="Sample Product", category="Electronics", price=100, availability=True)
    retrieved_product = Product.objects.get(name="Sample Product")
    self.assertEqual(retrieved_product.name, "Sample Product")
