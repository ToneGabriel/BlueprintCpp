#!/bin/bash

PROJECT_ROOT_DIR="$(pwd)"
TEST_DIR="$PROJECT_ROOT_DIR/tests/blueprint/project"

BUILD_DIR="$PROJECT_ROOT_DIR/.pyinstaller.out"
DIST_DIR="$BUILD_DIR/dist"
WORK_DIR="$BUILD_DIR/build"
RELEASE_DIR="$BUILD_DIR/dist/blueprintcpp/"
RELEASE_NAME="blueprintcpp"
MAIN_FILE="$PROJECT_ROOT_DIR/src/app/__main__.py"

TEMPLATES_DIR="$PROJECT_ROOT_DIR/src/app/jinja/templates"
TEMPLATES_PACKAGE_DIR="app/jinja/templates"

RELEASE_ZIP_NAME="blueprintcpp-linux-x86_64.zip"

# Build project
pyinstaller --onedir --noconfirm                                \
            --name     "$RELEASE_NAME"                          \
            --add-data "$TEMPLATES_DIR:$TEMPLATES_PACKAGE_DIR"  \
            --distpath "$DIST_DIR"                              \
            --workpath "$WORK_DIR"                              \
            --specpath "$BUILD_DIR"                             \
            "$MAIN_FILE"

# ZIP release
cd "$DIST_DIR"
zip -r -X "$RELEASE_ZIP_NAME" "$RELEASE_NAME"

# Run program to generate from test files
cd "$PROJECT_ROOT_DIR"
"$RELEASE_DIR/$RELEASE_NAME" "$TEST_DIR"
