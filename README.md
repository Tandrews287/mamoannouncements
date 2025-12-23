# Mamo Announcements

A simple and lightweight announcement management system built with Python.

## Features

- **Create** announcements with title, content, and priority levels
- **List** all announcements or filter by priority
- **View** detailed information about specific announcements
- **Update** existing announcements
- **Delete** announcements with confirmation
- **Persistent storage** using JSON file format

## Installation

This project uses only Python's standard library, so no external dependencies are required.

Requirements:
- Python 3.6 or higher

## Usage

### Command Line Interface

The system provides a CLI for managing announcements:

#### List all announcements
```bash
python cli.py list
```

#### List announcements by priority
```bash
python cli.py list --priority high
```

#### Create a new announcement
```bash
python cli.py create "System Maintenance" "The system will be down for maintenance on Sunday" --priority high
```

#### View a specific announcement
```bash
python cli.py view 1
```

#### Update an announcement
```bash
python cli.py update 1 --title "Updated Title" --priority normal
```

#### Delete an announcement
```bash
python cli.py delete 1
```

Add `--force` to skip the confirmation prompt:
```bash
python cli.py delete 1 --force
```

### Priority Levels

Announcements support three priority levels:
- `low` - Low priority announcements
- `normal` - Default priority (used if not specified)
- `high` - High priority announcements

## Data Storage

Announcements are stored in a `announcements.json` file in the current directory. The file is created automatically when you create your first announcement.

## Python API

You can also use the `AnnouncementManager` class directly in your Python code:

```python
from announcements import AnnouncementManager

# Initialize the manager
manager = AnnouncementManager()

# Create an announcement
announcement = manager.create_announcement(
    title="Welcome",
    content="Welcome to Mamo Announcements!",
    priority="normal"
)

# Get all announcements
all_announcements = manager.get_all_announcements()

# Get a specific announcement
announcement = manager.get_announcement(1)

# Update an announcement
manager.update_announcement(1, title="New Title")

# Delete an announcement
manager.delete_announcement(1)

# Get announcements by priority
high_priority = manager.get_announcements_by_priority("high")
```

## License

This project is open source and available under the MIT License.