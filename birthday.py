import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# Try to import sound for beeps (optional)
try:
    import winsound
    has_sound = True
except:
    has_sound = False

# Setup
fig = plt.figure(figsize=(10, 8), facecolor='black')
ax = plt.gca()
ax.set_xlim(-5, 5)
ax.set_ylim(-4, 6)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Birthday text
birthday_text = ax.text(0, 4.5, "HAPPY BIRTHDAY!", 
                        fontsize=28, fontweight='bold', 
                        color='gold', ha='center', va='center',
                        fontfamily='serif')

friend_text = ax.text(0, 3.5, "MY DEAR PANDHI PILLA!", 
                      fontsize=24, fontweight='bold', 
                      color='coral', ha='center', va='center',
                      fontfamily='serif')

# Cake base
cake_base = FancyBboxPatch((-2.5, -1), 5, 1.2, 
                            boxstyle="round,pad=0.1", 
                            facecolor='#d4a373', edgecolor='#8b5a2b', linewidth=2)
ax.add_patch(cake_base)

cake_mid = FancyBboxPatch((-2, 0.2), 4, 1, 
                          boxstyle="round,pad=0.1", 
                          facecolor='#f4a261', edgecolor='#8b5a2b', linewidth=2)
ax.add_patch(cake_mid)

cake_top = FancyBboxPatch((-1.5, 1.2), 3, 0.8, 
                          boxstyle="round,pad=0.1", 
                          facecolor='#e76f51', edgecolor='#8b5a2b', linewidth=2)
ax.add_patch(cake_top)

# Candles
candles = []
flames = []
candle_positions = [-1, 0, 1]
for i, x in enumerate(candle_positions):
    candle = plt.Rectangle((x-0.15, 2), 0.3, 0.8, 
                            facecolor='white', edgecolor='gray', linewidth=1)
    ax.add_patch(candle)
    candles.append(candle)
    
    flame = Circle((x, 2.85), 0.12, facecolor='orange', alpha=0.9)
    ax.add_patch(flame)
    flames.append(flame)

# Create sparkling stars
num_stars = 50
star_x = np.random.uniform(-5, 5, num_stars)
star_y = np.random.uniform(3, 6, num_stars)
star_sizes = np.random.uniform(30, 150, num_stars)
star_colors = np.random.choice(['gold', 'yellow', 'white', 'coral'], num_stars)
stars = ax.scatter(star_x, star_y, s=star_sizes, c=star_colors, alpha=0.7, marker='*')

# Balloons
balloon_colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink']
balloons = []
for i in range(8):
    x = np.random.uniform(-4, 4)
    y = np.random.uniform(-3, 2)
    color = np.random.choice(balloon_colors)
    balloon = Circle((x, y), 0.4, facecolor=color, alpha=0.7, edgecolor='white', linewidth=1)
    ax.add_patch(balloon)
    balloons.append(balloon)
    
    # Balloon string
    line = plt.Line2D([x, x], [y-0.4, y-1.2], color='white', linewidth=1, alpha=0.5)
    ax.add_line(line)
    balloons.append(line)

# Confetti particles
num_confetti = 100
confetti_x = np.random.uniform(-5, 5, num_confetti)
confetti_y = np.random.uniform(-4, 6, num_confetti)
confetti_colors = np.random.choice(['red', 'blue', 'gold', 'green', 'pink', 'purple'], num_confetti)
confetti = ax.scatter(confetti_x, confetti_y, s=20, c=confetti_colors, alpha=0.8, marker='s')

# Animation update function
def update(frame):
    # Flames flicker
    for flame in flames:
        flame.set_radius(0.1 + np.random.uniform(0, 0.08))
        flame.set_facecolor(np.random.choice(['orange', 'yellow', 'red']))
    
    # Rotate star colors
    star_colors_anim = np.random.choice(['gold', 'yellow', 'white', 'coral', 'orange'], num_stars)
    stars.set_color(star_colors_anim)
    stars.set_alpha(0.5 + 0.4 * np.sin(frame * 0.3))
    
    # Balloons floating
    for i in range(0, len(balloons), 2):
        balloon = balloons[i]
        line = balloons[i+1]
        new_y = balloon.center[1] + 0.01 * np.sin(frame * 0.1 + i)
        if new_y < 3:
            balloon.center = (balloon.center[0], new_y)
            line.set_data([balloon.center[0], balloon.center[0]], 
                         [balloon.center[1]-0.4, balloon.center[1]-1.2])
    
    # Confetti falling and resetting
    global confetti_y, confetti_x
    confetti_y += 0.03
    reset_indices = confetti_y > 5
    confetti_y[reset_indices] = -4
    confetti_x[reset_indices] = np.random.uniform(-5, 5, np.sum(reset_indices))
    confetti.set_offsets(np.c_[confetti_x, confetti_y])
    
    # Pulsing text effect
    scale = 1 + 0.05 * np.sin(frame * 0.5)
    birthday_text.set_fontsize(28 * scale)
    friend_text.set_fontsize(24 * scale)
    
# Create animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=False, repeat=True)

# Add title instructions
plt.suptitle("🎂 Happy Birthday! 🎂", color='white', fontsize=16, y=0.95)

# Show animation
plt.tight_layout()
plt.show()

# Optional: Save as GIF
# ani.save('birthday_wish.gif', writer='pillow', fps=20)
print("🎉 Happy Birthday to your friend! 🎉")