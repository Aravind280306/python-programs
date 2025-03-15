import matplotlib.pyplot as plt
sizes = [32,34,78,50,50,70]
labels = ["PHYSICS","CHEMISTRY", "English", "MathS", "C PROGRAMMING", "DIGITAL SYSTEMS"]
plt.pie (sizes, labels = labels, autopct = "%.2f ")
plt.show()
