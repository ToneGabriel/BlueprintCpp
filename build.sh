#!/bin/bash

DEST_PATH="$(pwd)/.pyinstaller.out"
TMP_PATH="$(pwd)/app/templates:templates"

pyinstaller --onefile \
            --name=blueprintcpp \
            --add-data "$TMP_PATH" \
            --distpath "$DEST_PATH/dist" \
            --workpath "$DEST_PATH/build" \
            --specpath "$DEST_PATH" \
            "$(pwd)/app/__main__.py"
