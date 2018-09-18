import unittest
import json
from app import create_app

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_post_order(self):
        data = {
            "name": "Chicken",
            "price": 1000,
            "description": "One plate"
        }

        result = self.client.post(
            "/api/v1/orders",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(result.status_code, 201)
        self.assertEqual(json.loads(res.data)['Message'], "Your order was successfully submitted! Kindly wait!")

    def test_retrieve_orders(self):

        result = self.client.get(
            "/api/v1/orders",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(result.status_code, 200)


    def test_order_by_id(self):
        result = self.client.get(
            "/api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(result.status_code, 200)

    
    def test_update_order_status(self):
        result = self.client.put(
            "api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        print(result.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.data)[
                         'Message'], "status approved")

    def test_invalid_order(self):
        result = self.client.get(
            "/api/v1/orders/1000",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(result.status_code, 404)
        self.assertEqual(json.loads(result.data)[
                         'Message'], "Your Order was not found")

    def test_del_invalid_order(self):
        res = self.client.delete(
            "api/v1/orders/100",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.data)[
                         'Message'], "Your Order was not found")