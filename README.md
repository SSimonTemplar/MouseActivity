# Mouse Activity Script

A Python script to simulate user activity by moving the mouse in a circular or box pattern. Useful for preventing sleep mode or indicating idle activity. Supports clicking at specific locations and multi-monitor setups.

## Features

- Configurable mouse movement in `circle` or `box` patterns
- Optional mouse clicking at:
  - Quadrants of a circle
  - Vertices of a box
  - All specified angles
- Adjustable timing for movement and rest intervals
- Monitor offset to target specific screens in multi-monitor configurations
- Console output for visibility into what the script is doing
- Built-in fail-safe via `pyautogui`: move mouse to top-left to stop instantly

## Requirements

- Python 3.x
- `pyautogui` library

Install via pip:

```bash
pip install pyautogui
```

## Usage

```bash
python mouse_activity_script.py [options]
```

### Command-line Options

| Option                | Description |
|-----------------------|-------------|
| `--shape`             | `circle` or `box` (default: `circle`) |
| `--size`              | Diameter for circle / side for box (pixels) |
| `--click`             | Enable clicking during movement |
| `--interval`          | Time between movements in seconds |
| `--click-points`      | `all`, `vertices`, or `quadrants` |
| `--move-duration`     | How long to move mouse per cycle (seconds) |
| `--wait-duration`     | How long to pause between cycles (seconds) |
| `--monitor-offset`    | Horizontal offset for multi-monitor setups (pixels) |

## Examples

Move mouse in a circle on second monitor, click at quadrants:

```bash
python mouse_activity_script.py --shape circle --size 300 --click --click-points quadrants --monitor-offset 1920 --move-duration 10 --wait-duration 60
```

Move in a box and click at each corner:

```bash
python mouse_activity_script.py --shape box --size 400 --click --click-points vertices --move-duration 15 --wait-duration 45
```

## Stopping the Script

- Press `Ctrl+C` in the terminal
- Or move mouse to the top-left corner to trigger `pyautogui` fail-safe

## License

MIT License
