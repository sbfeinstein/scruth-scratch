# Overview
This is a scratch repo in which I followed and played with / altered the official Godot 4.6 Tutorial > [Getting Started](https://docs.godotengine.org/en/stable/getting_started/introduction/index.html) material.

It includes the step-by-step stuff (hence the name of this repo) but also "Your first 2D game".

# Your first 2D game
I deviated from the instructions in at least these ways:
- Used a subfolder for all aspects, called `first_2d_game`
- Created the Main scene early on, so I could add dynamically set the display window size (see
  below) rather than modifying the project settings as instructed.

## Dynamically setting the window size
Used a `_ready` script on the Main node to `DisplayServer.window_set_size(Vector2i(480, 720))`.
TBD how to set the Mode to `canvas_items` and Aspect to `keep` per instructions as well.

The instructions said to set these things in:
Project Settings > Display > Window > [Viewport size settings].
