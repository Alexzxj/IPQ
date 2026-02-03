#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Castlery has N warehouses and needs to make inventory adjustments based on customer orders. Given:
--Warehouse network diagram (directed graph)
--The inventory quantity of each warehouse
--List of customer demand orders
--Transportation Cost Matrix
'''

class Warehouse:
    def __init__(self, id, name, inventory):
        self.id = id  # warehouse ID
        self.name = name  # warehouse name
        self.inventory = inventory  # warehouse dict {product_id: quantity}


class Order:
    def __init__(self, id, customer_id, items, priority=1):
        self.id = id  # Order ID
        self.customer_id = customer_id  # Customer ID
        self.items = items  # product info {product_id: quantity}
        self.priority = priority  # priority (1-5)


class TransportationCost:
    def __init__(self, from_warehouse, to_warehouse, cost_per_unit, transit_days):
        self.from_warehouse = from_warehouse
        self.to_warehouse = to_warehouse
        self.cost_per_unit = cost_per_unit  # transport cost per unit
        self.transit_days = transit_days  # transport days


# 示例数据
warehouses = [
    Warehouse(1, "ShangHai", {"A": 100, "B": 50, "C": 200}),
    Warehouse(2, "BeiJing", {"A": 80, "B": 100, "C": 50}),
    Warehouse(3, "GuangZhou", {"A": 150, "B": 30, "C": 100}),
    Warehouse(4, "ChengDu", {"A": 60, "B": 80, "C": 150}),
]

orders = [
    Order(1, "CUST001", {"A": 20, "B": 10}, priority=3),
    Order(2, "CUST002", {"B": 30, "C": 25}, priority=1),
    Order(3, "CUST003", {"A": 50, "C": 40}, priority=2),
]

# transport cost dict
transport_costs = {
    (1, 2): TransportationCost(1, 2, 5.0, 2),
    (1, 3): TransportationCost(1, 3, 3.0, 1),
    (1, 4): TransportationCost(1, 4, 8.0, 3),
    (2, 3): TransportationCost(2, 3, 6.0, 2),
    (2, 4): TransportationCost(2, 4, 7.0, 3),
    (3, 4): TransportationCost(3, 4, 4.0, 2),
    # Directly To The Customer's Warehouse
    (1, "CUST001"): TransportationCost(1, "CUST001", 10.0, 1),
    (2, "CUST001"): TransportationCost(2, "CUST001", 15.0, 2),
}

def allocate_inventory(warehouses, order):
    """
    Allocate inventory for a single order
    Rules:
    1. Prioritize shipping from the warehouse closest to the customer.
    2. If the inventory in a single warehouse is insufficient, replenish from multiple warehouses.
    3. Minimize the number of shipping warehouses as much as possible.
    - warehouses: List of warehouses sorted by distance
    - order: Order object
    Output: - allocations: [(warehouse_id, product_id, quantity), ...]
    - total_cost: Total Cost
    """
    pass


