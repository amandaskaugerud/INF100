import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")
plt.minorticks_on()

# Adding an arrow to graph starting
# from the base (2, 4) and with the
# length of 2 units from both x and y
# And setting the width of arrow for
# better visualization
plt.arrow(5.21, 2.14, -2, -2, width = 0.05)
plt.text(3, 2.26, "Første interseksjonen")

# savefig lagrer filene
plt.savefig("test.png")
plt.savefig("test.pdf")

# interaktivt vindu
plt.show() # Hva skjer om vi ikke har med den raden: plt.show()?
