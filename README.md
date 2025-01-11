# cursor-snap

 Cursor Trail Reset Tool

## Installation

You can install the package directly from PyPI:

```bash
pip install cursor-snap
```

Or install from source:

```bash
git clone https://github.com/adelelawady/cursor-snap.git
cd cursor-snap
pip install .
```

## Features

The tool provides the following features:
- Cursor Position Management: Save and restore cursor positions
- Reset App IDs: Clear stored cursor positions
- View Current IDs: Display active cursor position identifiers
- Cross-platform Support: Works on Windows, macOS, and Linux

## Usage

### Command Line Interface

```bash
# Save current cursor position
cursor-snap save position_name

# Restore cursor to saved position
cursor-snap restore position_name

# List all saved positions
cursor-snap list

# Reset all saved positions
cursor-snap reset
```

### Python API

```python
from cursor_snap import CursorSnap

# Initialize cursor snap
cursor = CursorSnap()

# Save current cursor position
cursor.save_position("main_window")

# Move cursor to saved position
cursor.restore_position("main_window")

# View all saved positions
positions = cursor.get_saved_positions()

# Reset all saved positions
cursor.reset_positions()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Adel Elawady (adel50ali50@gmail.com)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Support

If you encounter any issues or have questions, please file an issue on the [GitHub repository](https://github.com/adelelawady/cursor-snap/issues).
