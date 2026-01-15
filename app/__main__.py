import impl
import config

import os
import shutil
import argparse
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate C++ code from YAML")

    parser.add_argument("input",
                        help="Input path to root folder of YAML files"
                        )

    parser.add_argument("-o",
                        "--output",
                        default="generated",
                        help="Output path to root folder of generated header and source files"
                        )

    parser.add_argument("-b",
                        "--backup",
                        action="store_true",
                        help="Create a backup of existing files before overwriting"
                        )

    return parser.parse_args()


# def main() -> None:
#     args = parse_arguments()

#     input_path: str = args.input
#     output_path: str = args.output
#     create_backup: bool = args.backup

#     generator = impl.CppGenerator(config.JINJA_ENV_PACKAGE,
#                                   config.HEADER_TEMPLATE_FILENAME,
#                                   config.SOURCE_TEMPLATE_FILENAME
#                                   )

#     for root, dirs, files in os.walk(input_path):
#         for file in files:
#             if file.endswith((".yaml", ".yml")):
#                 # Full path to file
#                 filepath = os.path.join(root, file)

#                 # Preserve relative directory structure
#                 relative_filepath = os.path.relpath(root, input_path)

#                 destination_directorypath = os.path.join(output_path, relative_filepath)
#                 destination_filepath = os.path.join(destination_directorypath, file)

#                 os.makedirs(destination_directorypath, exist_ok=True)

#                 generator.load_model(filepath)
#                 header_content = generator.generate_header_content()
#                 source_content = generator.generate_source_content()

#                 with open(destination_filepath, 'w') as f:
#                     f.write(header_content)

#                 with open(destination_filepath, 'w') as f:
#                     f.write(source_content)




def main() -> None:
    args = parse_arguments()

    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    create_backup: bool = args.backup

    generator = impl.CppGenerator(
        config.JINJA_ENV_PACKAGE,
        config.HEADER_TEMPLATE_FILENAME,
        config.SOURCE_TEMPLATE_FILENAME,
    )

    for yaml_path in input_path.rglob("*"):
        if yaml_path.suffix.lower() not in (".yml", ".yaml"):
            continue

        # Preserve directory structure
        relative_dir = yaml_path.parent.relative_to(input_path)
        destination_dir = output_path / relative_dir
        destination_dir.mkdir(parents=True, exist_ok=True)

        # Load model
        generator.load_model(yaml_path)
        header_content = generator.generate_header_content()
        source_content = generator.generate_source_content()

        # Output filenames (example: Module1.yaml → Module1.h / Module1.cpp)
        header_file = destination_dir / f"{yaml_path.stem}.h"
        source_file = destination_dir / f"{yaml_path.stem}.cpp"

        # Backup if requested
        if create_backup:
            for file in (header_file, source_file):
                if file.exists():
                    file.rename(file.with_name(file.name + ".bak"))

        # Write files
        header_file.write_text(header_content)
        source_file.write_text(source_content)


if __name__ == "__main__":
    main()
