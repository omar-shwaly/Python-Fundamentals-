product_1= {

      "name" : "Laptop" ,
      "price" : 25000 ,
      "quantity" : 3 ,
      "category" : "Electronics"
}
print("#"*50)
print(product_1)

print("-"*50)
print(f" The price of one laptop = {product_1["price"]}")
print(f" The quanttity you took  ={product_1["quantity"]}")

First_Product_Total_Price= product_1["price"] * product_1["quantity"]

print(f" The_Total_Price ={First_Product_Total_Price} \n name is : {product_1["name"]} \n Category is : {product_1["category"]}")

product_1["price"]=22000
print("-"*50)
print(product_1)
print("#"*50)