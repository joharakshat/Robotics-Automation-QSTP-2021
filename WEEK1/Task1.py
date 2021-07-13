import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        t = self.dt

        for i in range(n):
            vel_x = v * np.cos(self.theta )
            vel_y = v * np.sin(self.theta )
            x = self.x_points[-1] + (vel_x * self.dt)
            y = self.y_points[-1] + (vel_y * self.dt)
            self.x_points.append(x)
            self.y_points.append(y)
            self.dt += t
            self.theta += w * t

        return x, y, self.theta

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        # plt.savefig(f"Unicycle_{v}_{w}.png")


if __name__ == "__main__":
    print("Unicycle Model Assignment")
    i=Unicycle(0,0,0,0.1)
    i.step(1,0.5,25)
    i.plot(1,0.5)
