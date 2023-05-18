# Project Demiurg

## Setup

### Requirements

- Python 3.10+

### Guide

1. Run `src/main.py`.

## JSON Game Schema

Game has to be in the following format:

```json
{
  "metadata": {
    "title": "<game title>",
    "author": "<author name>",
    "description": "<game description>"
  },
  "map": {
    "start_location_id": "<location id>",
    "end_location_id": "<location id>",
    "locations": {
      "<location id>": {
        "name": "<location name>",
        "text": "<location text>",
        "exits": {
          "N": {
            "location_id": "<location id>",
            "text": "<exit text>"
          },
          "E": {
            "location_id": "<location id>",
            "text": "<exit text>"
          },
          "S": {
            "location_id": "<location id>",
            "text": "<exit text>"
          },
          "W": {
            "location_id": "<location id>",
            "text": "<exit text>"
          }
        }
      }
    }
  }
}
```

## To Do

- Interactions, conditionals
- Items, inventroy
- Multiple endings (good, bad, etc.)
- Profile selection
