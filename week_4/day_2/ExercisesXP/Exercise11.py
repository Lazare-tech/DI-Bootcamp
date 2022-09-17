#Sandwich Orders#2
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.append("Pastrami sandwich")
sandwich_orders.insert(0,"Pastrami sandwich")
print(sandwich_orders)
print("le taiteur n'a plus de pastrami")
for i in range(0,6):
    if (sandwich_orders[i]=="Pastrami sandwich"):
        del sandwich_orders[i]
print(sandwich_orders)