import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_facecolor('white')

# Your name
name = "NUSRAT JANNAT"

# Add text object at center
text = ax.text(0.5, 0.5, name,
               color='red',
               fontsize=40,
               ha='center',
               va='center')

# Hide axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.axis('off')

# Animation function
def animate(frame):
    fps = 30  # frames per second
    stable_duration = 3  # seconds to stay centered
    stable_frames = fps * stable_duration

    if frame < stable_frames:
        # Stay centered
        x = 0.5
    else:
        # Slide forever from left to right
        slide_frame = frame - stable_frames
        speed = 0.02  # adjust for speed
        x = (slide_frame * speed) % 1.2  # wraps around at 1.2
    text.set_position((x, 0.5))
    return text,

# Create animation: lots of frames for endless effect
ani = animation.FuncAnimation(
    fig, animate, frames=range(2000), interval=1000/30, blit=True)

plt.show()
