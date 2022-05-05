import matplotlib.pyplot as plt
import numpy as np

volts_list = []
dt = 0.0
dv = 0.0

with  open("data.txt", 'r')  as  data:
    for line in data:
        volts_list.append(int(line))
with  open("settings.txt", 'r')  as  settings:
    print(settings.readline())
    dt = float((settings.readline().split()[3]))
    print(settings.readline())
    dv = float(settings.readline())
print(dv, ' ', dt)
volts_list_np = np.array(volts_list)
volts_list_update_np = volts_list_np * 3.3 / 256
time_array = np.linspace(0, dt * len(volts_list_update_np) - 1, len(volts_list_update_np))

fig, ax = plt.subplots(figsize=(10,7), constrained_layout=True)

plt.plot(time_array, volts_list_update_np, label='V(t) capasitor')
ax.set_ylabel("Voltage of capasitor")
ax.set_xlabel("Time")
ax.set_title("V(t) in process of RC")
ax.minorticks_on()
ax.grid(which='major', color = 'green',    #  цвет линий
        linewidth = 2,    #  толщина
        linestyle = ':')
ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':')
ax.set_ylim(bottom=0, top=3.3)
ax.set_xlim(left=0, right=90)
plt.legend(fontsize=14)
plt.savefig('saved_figure.svg')
plt.show()
