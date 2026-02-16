#!/bin/bash

DEST_PATH="$(pwd)/.pyinstaller.out"

pyinstaller --onedir \
            --name=blueprintcpp \
            --add-data "$(pwd)/src/app/jinja/templates:app/jinja/templates" \
            --distpath "$DEST_PATH/dist" \
            --workpath "$DEST_PATH/build" \
            --specpath "$DEST_PATH" \
            "$(pwd)/src/app/__main__.py"
