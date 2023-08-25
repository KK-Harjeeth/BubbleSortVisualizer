import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

def update_fig(frame):
    ax.clear()
    ax.bar(range(len(frame)), frame, color='blue')
    ax.set_title("Bubble Sort")

# Generate a random list of integers to sort
array_length = 10
data = [random.randint(1, 100) for _ in range(array_length)]

# Create a figure and axis for the animation
fig, ax = plt.subplots()
animation_generator = bubble_sort(data.copy())

# Create the animation
bubble_animation = animation.FuncAnimation(
    fig, update_fig, frames=animation_generator, repeat=False, interval=300, save_count=100
)

plt.show()
