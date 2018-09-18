from flask import Flask, request, jsonify
from flask_restful import    Resource
from .models import CustomerOrder, food_orders


class PostOrder(Resource):

    def post(self):
        data = request.get_json()
        order = CustomerOrder(data['name'], data["price"],data['description'])
        food_orders.append(order)

        return ({'Message' : 'Congratulations. Your new order has been posted. Kindly wait!'}), 201

class GetOrders(Resource):
    def get(self):
        return {"orders":[order.virtualize() for order in food_orders]}


class SingleOrder(Resource):
    def get(self, id):
        spec_order = CustomerOrder().retrieve_order_by_id(id)
        
        if spec_order:
            return {"order": spec_order.virtualize()}, 200

        return {"message":"Order not found"}, 404