import matplotlib.pyplot as plt

# Dataset
data = {
        'SECP256R1': 40.70,
        'Ed25519': 59.30,
}

curves = list(data.keys())
values = list(data.values())

figure = plt.figure(figsize = (10, 5))

# Creation
bars = plt.bar(curves, values, color='maroon', width=0.4)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval - 0, f'{yval:.2f}%', ha='center', va='bottom')

plt.xlabel("Curves")
plt.ylabel("Percent of Execution Time")
plt.title("Performance Evaluation for Ed25519 and SECP256R1")
plt.show()
