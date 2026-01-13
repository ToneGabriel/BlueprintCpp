import impl
import config

import os
import argparse


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

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    input_path: str = args.input
    output_path: str = args.output

    generator = impl.CppGenerator(config.JINJA_ENV_PACKAGE,
                                  config.HEADER_TEMPLATE_FILENAME,
                                  config.SOURCE_TEMPLATE_FILENAME
                                  )

    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                # Full path to file
                filepath = os.path.join(root, file)

                # Preserve relative directory structure
                relative_filepath = os.path.relpath(root, input_path)

                destination_directorypath = os.path.join(output_path, relative_filepath)
                destination_filepath = os.path.join(destination_directorypath, file)

                os.makedirs(destination_directorypath, exist_ok=True)

                generator.load_model(filepath)
                header_content = generator.generate_header_content()
                source_content = generator.generate_source_content()

                with open(destination_filepath, 'w') as f:
                    f.write(header_content)

                with open(destination_filepath, 'w') as f:
                    f.write(source_content)


if __name__ == "__main__":
    main()
