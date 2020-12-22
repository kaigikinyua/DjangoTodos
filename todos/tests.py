from django.test import TestCase,Client

# Create your tests here.
class ViewsTest(TestCase):
    def setUp(self):
        self.client=Client()

    def test_indexpage(self):
        response=self.client.get("/")
        response_check(response)
        self.assertEqual(response.status_code,200)

    def test_loginpage(self):
        response=self.client.get("/login")
        self.assertEqual(response.status_code,200)
    
    def test_signup(self):
        response=self.client.get("/signup")
        self.assertEqual(response.status_code,200)

#class TodosDBTest(TestCase)