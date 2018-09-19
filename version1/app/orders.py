from flask import Flask, request, jsonify
from flask_restful import    Resource
from .models import CustomerOrder, food_orders


class PostOrder(Resource):

    def post(self):
        data = request.get_json()
        order = CustomerOrder(data['name'], data["price"],data['description'])
        food_orders.append(order)

        return jsonify({'Message' : 'Congratulations. Your new order has been posted. Kindly wait!'}), 201

class GetOrders(Resource):
    def get(self):
        return jsonify({"orders" : [order.virtualize() for order in food_orders]})


class SingleOrder(Resource):
    def get(self, id):
        spec_order = CustomerOrder().retrieve_order_by_id(id)
        
        if spec_order:
            return jsonify({'Order': spec_order.virtualize()}), 200

        return jsonify({'Message' : "Oops! Specified Order not found in our records"}), 404

    def put(self, id):
        order = CustomerOrder().retrieve_order_by_id(id)

        if order:
            order.status="Confirmed"
            return jsonify({'Message' : 'Order approved!'}), 200
        return jsonify({'Message' : 'Oops! Specified Order not found in our records!'}), 404

    def delete(self, id):
        spec_order = CustomerOrder().retrieve_order_by_id(id)

        if spec_order:
            food_orders.remove(spec_order)
            return jsonify({'Message' : 'Requested Order deleted successfully!'}),200
        return jsonify({'Message' : 'Oops! Requested Order not found in our records! Try a different ID!'}, 404



