# Project Demiurg

## Setup

### Requirements

- Python 3.10+
- Kivy 2.2.0+
- KivyMD 1.1.1+

### Guide

1. Run `src/main.py`.

## JSON Schemas

Every game is stored in a directory with the same name as the game title in the `/games` directory. Directory of a game contains the game data file and the (optional) game progress file.

Both of these files must be in a specific format that is shown below.

Properties with `?` sign are optional.

### game-data.json

Game data file contains all the information about the game itself such as metadata, map, tasks, etc.

```json
{
  "metadata": {
    "title": "<game title>",
    "author": "<author name>",
    "description": "<game description>"
  },
  "map": {
    "start_location_id": "<location id>",
    "locations": {
      "<location id>": {
        "name": "<location name>",
        "text": "<location text>",
        "exits": {
          "N?": {
            "location_id": "<location id>",
            "text": "<exit text>"
          },
          "E?": {
            "location_id": "<location id>",
            "text": "<exit text>"
          },
          "S?": {
            "location_id": "<location id>",
            "text": "<exit text>"
          },
          "W?": {
            "location_id": "<location id>",
            "text": "<exit text>"
          }
        },
        "is_end_location?": true
      }
    }
  }
}
```

### game-progress.json

Game progress file contains information about the current state of the game such as current location, inventory, etc.

```json
{
  "location_id": "<location id>",
  "message?": "<message>"
}
```

## To Do

- UI
- Progress saving
- Interactions, tasks, conditions
- Items, inventroy
- Multiple endings (good, bad, ...)
- Profile selection
