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
* Have you ever encountered the problem of slow data query? How did you solve it? When it comes to storing a large amount of data, how do you design the database in an efficient manner? (Database architecture level)
* Why is the concurrent performance of Python so low? How can we improve the concurrent performance? Please explain the GC mechanism.
* Are there any AI scenarios in Odoo where AI has helped solve those practical problems?
* < Algorithm> go to the stock.py and write your code.


