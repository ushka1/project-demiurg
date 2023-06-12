# Project Demiurg

Project Demiurg is an interactive game creation platform that allows users to design and play their own text-based adventure games. With Demiurg, you can unleash your creativity and build captivating game worlds filled with quests, dialogues, and immersive environments.

This repository contains code for the Demiurg app that is used to play games. If you're searching for app that is used to create games then check out [Demiurg_Creator](https://github.com/Lightios/Demiurg_Creator).

## Setup

### Requirements

- Python 3.10+
- Kivy 2.2.0+
- KivyMD 1.1.1+
- Plyer 2.1.0+
- Pyobjus 1.2.2+

### Guide

1. Install python.
1. Install all required packages using `pip install -r requirements.txt`.
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
  },
  "quests": {
    "<quest id>": {
      "name": "<quest name>",
      "description": "<quest description>",
      "start_stage_id": "<stage id>",
      "stages": {
        "<stage id>": {
          "location_id": "<location id>",
          "text": "<stage text>",
          "options": {
            "<option id>": {
              "text": "<option text>",
              "next_stage_id": "<stage id>",
              "response_message?": "<response message>"
            }
          }
        }
      }
    }
  }
}
```

### game-progress.json

Game progress file contains information about the current state of the game such as current location, inventory, etc.

```json
{
  "player_name": "<player name>",
  "location_id": "<location id>",
  "quests": {
    "<quest id>": {
      "stage_id": "<stage id>"
    }
  },
  "message?": "<message>"
}
```
