import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры орбит планет (приблизительные, для визуализации)
planets = {
    'Mercury': {'radius': 0.39, 'period': 0.24, 'color': 'gray'},
    'Venus': {'radius': 0.72, 'period': 0.62, 'color': 'orange'},
    'Earth': {'radius': 1.0, 'period': 1.0, 'color': 'blue'},
    'Mars': {'radius': 1.52, 'period': 1.88, 'color': 'red'},
    'Jupiter': {'radius': 5.2, 'period': 11.86, 'color': 'brown'},
    'Saturn': {'radius': 9.58, 'period': 29.45, 'color': 'yellow'},
    'Uranus': {'radius': 19.22, 'period': 84.0, 'color': 'lightblue'},
    'Neptune': {'radius': 30.05, 'period': 164.8, 'color': 'darkblue'}
}

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal', 'box')
ax.set_facecolor('black')

# Настраиваем оси
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.axis('off')

# Рисуем Солнце
sun = plt.Circle((0, 0), 0.5, color='yellow')
ax.add_artist(sun)

# Инициализируем планеты на орбитах
planet_artists = {}
for name, props in planets.items():
    planet = plt.Circle((props['radius'], 0), 0.2, color=props['color'])
    ax.add_artist(planet)
    planet_artists[name] = planet

# Обновление позиций планет в каждом кадре
def update(frame):
    for name, props in planets.items():
        angle = 2 * np.pi * frame / (props['period'] * 100)
        x = props['radius'] * np.cos(angle)
        y = props['radius'] * np.sin(angle)
        planet_artists[name].set_center((x, y))

# Анимация
ani = FuncAnimation(fig, update, frames=range(2000), interval=20)
plt.show()

