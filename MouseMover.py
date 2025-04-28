import pyautogui
import math
import time
import argparse

"""
Mouse Activity Script

Description:
This script moves the mouse cursor around the screen in a specified pattern (circle or box) to prevent the computer from going into sleep mode and to simulate user activity.

Requirements:
Requires the `pyautogui` package.
To install it, run:
  pip install pyautogui

Usage:
Run the script from a terminal with optional arguments:

  python mouse_activity_script.py [options]

Arguments:
  --shape {circle,box}        Movement shape (default: circle).
  --size SIZE                 Diameter for circle, side length for box (in pixels, default: 200).
  --click                     Enable mouse clicking (default: False).
  --interval INTERVAL         Interval between mouse moves in seconds (default: 0.1).
  --click-points {all,vertices,quadrants}
                              Locations to perform clicks (default: quadrants).
  --move-duration DURATION    Duration to move the mouse continuously in seconds (default: 5).
  --wait-duration DURATION    Duration to wait between movement cycles in seconds (default: 30).
  --monitor-offset OFFSET     Horizontal offset to position mouse cursor on another monitor (default: 1920).

Examples:
  Move in circle on second monitor, click at quadrants, move 10 seconds, wait 60 seconds:
    python mouse_activity_script.py --shape circle --size 300 --click --click-points quadrants --monitor-offset 1920 --move-duration 10 --wait-duration 60

  Move in box, click at vertices, move 15 seconds, wait 45 seconds:
    python mouse_activity_script.py --shape box --size 400 --click --click-points vertices --move-duration 15 --wait-duration 45

Press Ctrl+C to stop the script. You can also move your mouse to the top-left corner of the screen to trigger pyautogui's built-in fail-safe and stop execution immediately.
"""


# Configuration parser
parser = argparse.ArgumentParser(description='Mouse mover and clicker.')
parser.add_argument('--shape', choices=['circle', 'box'], default='circle', help='Movement shape.')
parser.add_argument('--size', type=int, default=200, help='Diameter for circle, side for box (in pixels).')
parser.add_argument('--click', action='store_true', help='Enable clicking.')
parser.add_argument('--interval', type=float, default=0.1, help='Interval between mouse moves (seconds).')
parser.add_argument('--click-points', choices=['all', 'vertices', 'quadrants'], default='quadrants', help='Click locations.')
parser.add_argument('--move-duration', type=int, default=5, help='Duration to move mouse (seconds).')
parser.add_argument('--wait-duration', type=int, default=30, help='Duration to wait between movements (seconds).')
parser.add_argument('--monitor-offset', type=int, default=1920, help='Horizontal offset to move mouse to another monitor.')
args = parser.parse_args()

# Center position with offset for multiple monitors
screenWidth, screenHeight = pyautogui.size()
centerX, centerY = (screenWidth // 2) + args.monitor_offset, screenHeight // 2

# Move in circle
def move_circle(diameter, click, click_points, move_time):
    print("Moving mouse in a circle")
    radius = diameter / 2
    points = 360
    click_angles = {'quadrants': [0, 90, 180, 270], 'all': range(0, 360, 30)}
    start_time = time.time()

    while time.time() - start_time < move_time:
        for angle in range(points):
            rad = math.radians(angle)
            x = centerX + radius * math.cos(rad)
            y = centerY + radius * math.sin(rad)
            pyautogui.moveTo(x, y, duration=args.interval)

            if click and ((click_points == 'all' and angle % 30 == 0) or
                          (click_points == 'quadrants' and angle in click_angles['quadrants'])):
                pyautogui.click()
                print(f"Clicked at angle {angle}")

# Move in box
def move_box(size, click, click_points, move_time):
    print("Moving mouse in a box")
    half = size / 2
    corners = [
        (centerX - half, centerY - half),  # top-left
        (centerX + half, centerY - half),  # top-right
        (centerX + half, centerY + half),  # bottom-right
        (centerX - half, centerY + half)   # bottom-left
    ]

    start_time = time.time()

    while time.time() - start_time < move_time:
        for i, (x, y) in enumerate(corners):
            pyautogui.moveTo(x, y, duration=args.interval)
            if click and click_points == 'vertices':
                pyautogui.click()
                print(f"Clicked at vertex {i+1}")

# Main loop
try:
    while True:
        if args.shape == 'circle':
            move_circle(args.size, args.click, args.click_points, args.move_duration)
        elif args.shape == 'box':
            move_box(args.size, args.click, args.click_points, args.move_duration)

        print(f"Waiting for {args.wait_duration} seconds...")
        time.sleep(args.wait_duration)

except KeyboardInterrupt:
    print('Script stopped.')
