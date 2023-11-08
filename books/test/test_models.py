from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from books.models import Product


class ProductAdminTest(TestCase):
    def setUp(self):
        """
        Creats adminuser for testing
        """
        self.user = User.objects.create_superuser(
            username='adminuser',
            password='adminpassword',
            email='admin@example.com'
        )
        self.client = Client()

    def test_add_product_in_admin(self):
        """
        Function creates new product entry. After it checks if the product
        was sucesfully added (HTTP status code 302 indicates success).
        Finaly it checks if product variables have the correct values.
        """
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.post('/admin/books/product/add/', {
            'title': 'Eat That Frog!',
            'details': 'Product details',
            'stars': 4,
            'numberreviews': 10,
            'price': 50,
            'productpic': 'https://example.com/exa.jpg',
            'amazon': 'https://example.com/Test'
        })
        self.assertEqual(response.status_code, 302)
        new_product = Product.objects.get(title='Eat That Frog!')
        self.assertEqual(new_product.details, 'Product details')
        self.assertEqual(new_product.stars, 4)
        self.assertEqual(new_product.numberreviews, 10)
        self.assertEqual(new_product.price, 50)
        self.assertEqual(new_product.productpic, 'https://example.com/exa.jpg')
        self.assertEqual(new_product.amazon, 'https://example.com/Test')

    def tearDown(self):
        # Clean up by deleting the user and product
        self.user.delete()
        Product.objects.filter(title='New Product').delete()
