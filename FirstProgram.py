voltages = [395.2, 393.8, 391.5, 388.0, 385.3, 390.1]
voltage_highest = max(voltages)
print("The highest voltage is:", voltage_highest)
voltage_lowest = min(voltages)
print("The lowest voltage is:", voltage_lowest)
voltage_average = sum(voltages) / len(voltages)
print("The average voltage is:", voltage_average)
if voltage_lowest < 388.0:
    print("Warning: Low cell voltage detected")
else:
    print("all cells normal")
