import matplotlib.pyplot as plt

# Product names and sales values
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

# Create a bar chart
plt.figure()
plt.bar(products, sales, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data for Different Products')
plt.grid(axis='y')

plt.show()