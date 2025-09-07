import tkinter as tk
from PIL import Image, ImageTk

# Flight data (mocked)
flight_info = {
    "Flight Number": "AAL111 / AA111",
    "Airline": "American Airlines",
    "Departure": "FCO (Rome)",
    "Arrival": "ORD (Chicago)",
    "Scheduled Departure": "11:05",
    "Actual Departure": "11:27",
    "Scheduled Arrival": "2:30",
    "Estimated Arrival": "1:33 PM",
    "Aircraft": "Boeing 787-8 Dreamliner",
    "Registration": "N888AM",
    "Country": "United States",
    "Aircraft Age": "8.6 years",
    "Altitude": "35,000 ft",
    "Speed": "478 knots",
    "Vertical Speed": "0 ft/min",
    "Track": "288°",
    "Latitude": "52.120",
    "Longitude": "-27.888"
}

# Create main window
root = tk.Tk()
root.title("Fake Flight Tracker")
root.geometry("1000x600")

# Load map background
map_img = Image.open("map.png")
map_img = map_img.resize((700, 600))
map_photo = ImageTk.PhotoImage(map_img)

# Load plane icon
plane_icon = Image.open("planeicon.png")
plane_icon = plane_icon.resize((40, 40))
plane_photo = ImageTk.PhotoImage(plane_icon)

# Canvas for map
canvas = tk.Canvas(root, width=700, height=600)
canvas.pack(side="left")
canvas.create_image(0, 0, anchor="nw", image=map_photo)

# Simulate plane position (mock coordinates)
plane_x = 400  # X position on map
plane_y = 200  # Y position on map
canvas.create_image(plane_x, plane_y, image=plane_photo)

# Sidebar for flight info
info_frame = tk.Frame(root, width=300, bg="white")
info_frame.pack(side="right", fill="y")

tk.Label(info_frame, text="Flight Details", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

for key, value in flight_info.items():
    tk.Label(info_frame, text=f"{key}: {value}", anchor="w", justify="left", bg="white", font=("Arial", 10)).pack(fill="x", padx=10)

root.mainloop()
