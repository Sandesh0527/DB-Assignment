1) Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.

Product Category and Product have a relation of one to many i.e one Product Category can have many products linked to it.

2) How could you ensure that each product in the "Product" table has a valid category assigned to it?

To make sure each Product have valid Product Category to it we need to enforce foriegn key constraint on Product table with catergory id,
it will prevent insertion or updation of Product with invalid Product Category.
