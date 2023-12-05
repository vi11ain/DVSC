#!/bin/bash
venv/Scripts/activate
(flask --app dvsc run --port 80) &
(python token_gen.py) &