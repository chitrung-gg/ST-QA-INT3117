def calculate_shipping_fee(x: float, y: float, z: int) -> float:
    if not (0 < x <= 1000) or not (0 < y <= 100) or not (0 < z <= 24): 
        return "Invalid Input"

    x, y = round(x, 2), round(y, 2)
    if x < 10:
        distance_fee = x * 5000
    elif x < 50:
        distance_fee = x * 4500
    else:
        distance_fee = x * 4000
    
    weight_fee = 50000 if y >= 10 else 0
    time_fee = 50000 if z < 12 else 0
    
    return distance_fee + weight_fee + time_fee