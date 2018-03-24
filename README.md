# droneboard

## Inspiration
We want to find new and interesting ways to interact with sound. Therefor we experiment with an old-fashioned whiteboard and some magnets as a simple and cheap, yet intuitive and expressive interface to control sound.

## What it does
It detects the whiteboard with attached elements and uses their positions and rotations to control multiple sound layers with different parameters.

## How we built it
We use a webcam and OpenCV to recognize the magnets on the whiteboard and then send the data via Open Sound Control to a SuperCollider server, which is responsible for generating audio output.
