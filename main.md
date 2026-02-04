                Odoo Developer Interview Questions
* Please write out the output of the following code
````
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1))
print(append_to(2))
print(append_to(3), [])
print(append_to(4))

a, b = 257, 257
c, d = ["hello"], ["hello"]
print(a == b)
print(a is b)
print(c == d)
print(c is d)
````
* Explain what a Python metaclass is, and how __new__() and __init__() are loaded during the program execution process?
* Implement an Odoo model creation,please write code.
* Introduce Odoo and share your insights on Odoo.
  eg: From the framework, the version, the deployed, the advantages and disadvantages, and the usage experience.
* What is the integration mechanism of Odoo?
  eg: Currently, there are many identical methods in the modules of Odoo. How to determine the call chain of the methods?
* Introduce the ORM framework in Odoo, and explain why we use ORM instead of directly using SQL. What are the implications of using SQL directly? When can SQL be used?
* Have you ever encountered the problem of slow data query? How did you solve it?
* Please design a reasonable database structure based on the following information? (Database architecture level)
```
  Currently, Castlery has multiple platforms for selling products. We need to store all these order information into our own Odoo system. The business characteristics are as follows:
    - User volume: tens of millions
    - Daily order volume: tens of millions
    - Read-write ratio: approximately 1:20
    - Data volume: the order table has an annual growth of over 10 billion rows 
  Please design a database and data tables, such as the odoo-db database, the order table, the user table, etc.
  Order field: id, name, createDate, user_id
  User table fields: id, name, email, phone, createDate
```
* Why is the concurrent performance of Python so low? How can we improve the concurrent performance? Please explain the GC mechanism.
* What is your code development process like? How do you ensure the quality of your code? Will you be more proactive in conducting unit tests and inheritance tests? If so, what is your test coverage rate?
* Are there any AI scenarios in Odoo where AI has helped solve those practical problems?
* Please identify the flaws in the following code and optimize it.
```
# Example 1:
  class StockQuant(models.Model):
    _inherit = 'stock.quant'
    
    @api.depends('product_id', 'location_id')
    def _compute_extended_info(self):
        for quant in self:
            quant.product_category = quant.product_id.categ_id.name
            
            move_lines = self.env['stock.move.line'].search([
                ('product_id', '=', quant.product_id.id),
                ('state', '=', 'done'),
                ('date', '>=', fields.Date.today().replace(day=1))
            ])
            quant.monthly_movement = len(move_lines)
            
            if quant.location_id and quant.location_id.warehouse_id:
                warehouse = quant.location_id.warehouse_id
                company = warehouse.company_id
                
                # ...
                company_currency = company.currency_id
                product_price = quant.product_id.standard_price
                
                if company_currency.name == 'USD':
                    conversion_rate = 6.5
                elif company_currency.name == 'EUR':
                    conversion_rate = 7.8
                else:
                    conversion_rate = 1.0
                
                quant.value_local = product_price * quant.quantity * conversion_rate
    
  # Example 2:
    @api.depends('product_id', 'location_id', 'quantity', 
                 'product_id.categ_id', 'product_id.standard_price',
                 'location_id.warehouse_id', 'location_id.warehouse_id.company_id')
    def _compute_value(self):
        for quant in self:
            pass
    
    product_category = fields.Char(compute='_compute_extended_info', store=True)
    monthly_movement = fields.Integer(compute='_compute_extended_info')
    value_local = fields.Float(compute='_compute_extended_info')

```
* < Algorithm> go to the stock.py and write your code.


