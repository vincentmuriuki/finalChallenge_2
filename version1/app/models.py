food_orders = []
users = []

class CustomerOrder:

    order_id = 1
    def __init__(self,name=None,price=None,description=None, status="Pending"):
        self.name=name
        self.price=price
        self.description=description
        self.id=CustomerOrder.order_id
        self.status=status

        CustomerOrder.order_id += 1
    def virtualize(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status
        )

    def retrieve_order_by_id(self, order_id):
        for order in food_orders:
            if order.id == order_id:
                return order