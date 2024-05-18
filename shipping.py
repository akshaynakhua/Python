# Sal's Shipping

weight = 5
cost_ground_premium = 125

#Ground shipping

if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

# Ground Shipping Premimum

print("Ground Shipping: $" + str(cost_ground))
print("Cost Ground Premium: $" + str(cost_ground_premium))

#Drone shipping

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $" + str(cost_drone))
