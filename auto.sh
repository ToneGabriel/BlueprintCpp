#!/bin/bash

PROJECT_ROOT_DIR="$(pwd)"
TEST_DIR="$PROJECT_ROOT_DIR/tests/blueprint"

BUILD_DIR="$PROJECT_ROOT_DIR/.pyinstaller.out"
DIST_DIR="$BUILD_DIR/dist"
WORK_DIR="$BUILD_DIR/build"
RELEASE_DIR="$BUILD_DIR/dist/blueprintcpp/"
RELEASE_NAME="blueprintcpp"
MAIN_FILE="$PROJECT_ROOT_DIR/src/app/__main__.py"

TEMPLATES_DIR="$PROJECT_ROOT_DIR/src/app/jinja/templates"
TEMPLATES_PACKAGE_DIR="app/jinja/templates"

ARTIFACTS_UI_DIR="$PROJECT_ROOT_DIR/ui_artifacts"
GENERATED_UI_DIR="$PROJECT_ROOT_DIR/src/app/ui/generated"

RELEASE_ZIP_NAME="blueprintcpp-linux-x86_64.zip"
EXECUTABLE="$RELEASE_DIR/$RELEASE_NAME"

generate() {
    echo "Generating UI tools..."

    pyside6-uic ui_artifacts/mainwindow.ui -o src/app/ui/generated/ui_mainwindow.py
}

build() {
    echo "Building $RELEASE_NAME..."

    pyinstaller --onedir --noconfirm                                \
                --name     "$RELEASE_NAME"                          \
                --add-data "$TEMPLATES_DIR:$TEMPLATES_PACKAGE_DIR"  \
                --distpath "$DIST_DIR"                              \
                --workpath "$WORK_DIR"                              \
                --specpath "$BUILD_DIR"                             \
                "$MAIN_FILE"
}

archive() {
    if [ ! -d "$RELEASE_DIR" ]; then
        echo "Release directory not found. Build first."
        exit 1
    fi

    echo "Creating release archive..."

    (
        cd "$DIST_DIR" || exit 1
        zip -r -X "$RELEASE_ZIP_NAME" "$RELEASE_NAME"
    )
}

run() {
    if [ ! -f "$EXECUTABLE" ]; then
        echo "Executable not found. Build first."
        exit 1
    fi

    "$EXECUTABLE" "$TEST_DIR"
}

DO_GENERATE=false
DO_BUILD=false
DO_ARCHIVE=false
DO_RUN=false

while getopts "gbar" opt; do
    case "$opt" in
        g) DO_GENERATE=true ;;
        b) DO_BUILD=true ;;
        a) DO_ARCHIVE=true ;;
        r) DO_RUN=true ;;
        ?)
            echo "Usage: $0 [-g] [-b] [-a] [-r]"
            echo "  -g    Generate UI tools for python"
            echo "  -b    Build the application"
            echo "  -a    Create the release archive"
            echo "  -r    Run the built application"
            exit 1
            ;;
    esac
done

# Execute in a fixed order
$DO_GENERATE && generate
$DO_BUILD && build
$DO_ARCHIVE && archive
$DO_RUN && run
