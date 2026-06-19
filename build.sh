#!/bin/bash

BUILD_DIR="$(pwd)/.pyinstaller.out"
DIST_DIR="$BUILD_DIR/dist"
WORK_DIR="$BUILD_DIR/build"
MAIN_FILE="$(pwd)/src/app/__main__.py"

TEMPLATES_DIR="$(pwd)/src/app/jinja/templates"
TEMPLATES_PACKAGE_DIR="app/jinja/templates"

RELEASE_ZIP_NAME="blueprintcpp-linux-x86_64.zip"
RELEASE_PATH="$BUILD_DIR/dist/blueprintcpp/"
RELEASE_NAME="blueprintcpp"

pyinstaller --onedir                                            \
            --noconfirm                                         \
            --name="$RELEASE_NAME"                              \
            --add-data "$TEMPLATES_DIR:$TEMPLATES_PACKAGE_DIR"  \
            --distpath "$DIST_DIR"                              \
            --workpath "$WORK_DIR"                              \
            --specpath "$BUILD_DIR"                             \
            "$MAIN_FILE"

cd "$DIST_DIR"
zip -r -X "$RELEASE_ZIP_NAME" "$RELEASE_NAME"
