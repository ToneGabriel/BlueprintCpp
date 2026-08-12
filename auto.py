#!/usr/bin/env python3
"""
Helper script that automates the development process for blueprintcpp.

Usage:
    python3 auto.py design
    python3 auto.py generate
    python3 auto.py build [--archive]
    python3 auto.py run
"""


from pathlib import Path
from enum import Enum
import subprocess
import argparse
import sys


RELEASE_NAME = "blueprintcpp"
RELEASE_ZIP_NAME = "blueprintcpp-linux-x86_64.zip"

PROJECT_ROOT_DIR = Path("/workspaces/blueprintcpp")
TEST_DIR = PROJECT_ROOT_DIR / "tests" / "blueprint"

BUILD_DIR = PROJECT_ROOT_DIR / ".pyinstaller.out"
DIST_DIR = BUILD_DIR / "dist"
WORK_DIR = BUILD_DIR / "build"
RELEASE_DIR = BUILD_DIR / "dist" / RELEASE_NAME
MAIN_FILE = PROJECT_ROOT_DIR / "src" / "app" / "__main__.py"
EXECUTABLE = RELEASE_DIR / RELEASE_NAME

TEMPLATES_DIR = PROJECT_ROOT_DIR / "src" / "app" / "jinja" / "templates"
TEMPLATES_PACKAGE_DIR = "app/jinja/templates"  # relative, not a filesystem path — kept as str

ARTIFACTS_UI_DIR = PROJECT_ROOT_DIR / "ui_artifacts"
GENERATED_UI_DIR = PROJECT_ROOT_DIR / "src" / "app" / "ui" / "generated"


class Command(Enum):
    DESIGN      = "design"
    GENERATE    = "generate"
    BUILD       = "build"
    RUN         = "run"
# Command


class Argument(Enum):
    COMMAND = "command"
    ARCHIVE = "archive"
# Argument


def parse_arguments(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="auto",
        description="Helper script that automates the development process",
        allow_abbrev=False
    )

    subparsers = parser.add_subparsers(
        dest=f"{Argument.COMMAND.value}",
        required=True,  # forces exactly one subcommand to be chosen
        help="Which command to run"
    )

    # -----------------------------------------------------------
    p1 = subparsers.add_parser(
        f"{Command.DESIGN.value}",
        help="Open Pyside6 Qt Widgets Designer",
        allow_abbrev=False
    )

    # -----------------------------------------------------------
    p2 = subparsers.add_parser(
        f"{Command.GENERATE.value}",
        help="Generate python files for all ui artifacts",
        allow_abbrev=False
    )

    # -----------------------------------------------------------
    p3 = subparsers.add_parser(
        f"{Command.RUN.value}",
        help="Run the program (Must be built first)",
        allow_abbrev=False
    )

    # -----------------------------------------------------------
    p4 = subparsers.add_parser(
        f"{Command.BUILD.value}",
        help="Build the program",
        allow_abbrev=False
    )

    p4.add_argument(
        f"--{Argument.ARCHIVE.value}",
        action="store_true",
        help="Archive the build output for release"
    )

    # -----------------------------------------------------------
    return parser.parse_args(argv)
# parse_arguments


def open_pyside6_designer() -> None:
    cmd = ["pyside6-designer"]
    print("Opening Pyside6 Qt Widgets Designer")
    subprocess.run(cmd, check=True)
# open_pyside6_designer


def generate_ui_helper_modules() -> None:
    if not ARTIFACTS_UI_DIR.is_dir():
        print(f"Error: UI artifacts directory not found: {ARTIFACTS_UI_DIR}", file=sys.stderr)
        return

    ui_files = sorted(ARTIFACTS_UI_DIR.glob("*.ui"))

    if not ui_files:
        print(f"No .ui files found in {ARTIFACTS_UI_DIR}")
        return

    GENERATED_UI_DIR.mkdir(parents=True, exist_ok=True)

    for ui_file in ui_files:
        output_file = GENERATED_UI_DIR / f"ui_{ui_file.stem}.py"

        cmd = [
            "pyside6-uic",
            str(ui_file),
            "-o",
            str(output_file)
        ]

        print(f"Generating {output_file.relative_to(PROJECT_ROOT_DIR)} from {ui_file.relative_to(PROJECT_ROOT_DIR)}")
        subprocess.run(cmd, check=True)
# generate_ui_helper_modules


def build_app(archive: bool) -> None:
    cmd = [
        "pyinstaller",
        "--onedir",
        "--noconfirm",
        "--name", RELEASE_NAME,
        "--add-data", f"{str(TEMPLATES_DIR)}:{TEMPLATES_PACKAGE_DIR}",
        "--distpath", str(DIST_DIR),
        "--workpath", str(WORK_DIR),
        "--specpath", str(BUILD_DIR),
        str(MAIN_FILE),
    ]

    subprocess.run(cmd, check=True)

    if archive is True:
        cmd = [
            "zip",
            "-r",
            "-X",
            RELEASE_ZIP_NAME,
            RELEASE_NAME
        ]

        subprocess.run(cmd, cwd=DIST_DIR, check=True)
# build_app


def run_app() -> None:
    cmd = [
        str(EXECUTABLE),
        str(TEST_DIR)
    ]

    print(f"Running executable {EXECUTABLE.relative_to(PROJECT_ROOT_DIR)}")
    subprocess.run(cmd, check=True)
# run_app


def main(argv=None) -> int:
    args = parse_arguments(argv)

    match getattr(args, Argument.COMMAND.value):
        case Command.DESIGN.value:
            open_pyside6_designer()
        case Command.GENERATE.value:
            generate_ui_helper_modules()
        case Command.BUILD.value:
            build_app(getattr(args, Argument.ARCHIVE.value))
        case Command.RUN.value:
            run_app()

    return 0
# main


if __name__ == "__main__":
    sys.exit(main())
