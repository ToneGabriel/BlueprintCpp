import os
import impl
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

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    input_path = Path(args.input)
    output_path = Path(args.output)

    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                # Path to file
                src_file = os.path.join(root, file)

                # Preserve relative directory structure
                rel_path = os.path.relpath(root, input_path)
                dest_dir = os.path.join(output_path, rel_path)

                os.makedirs(dest_dir, exist_ok=True)

                module = impl.load_module_yaml(src_file)

                header_content = impl.generate_header_content(module)
                source_content = impl.generate_source_content(module)

                dest_file = os.path.join(dest_dir, file)

                # shutil.copy2(src_file, dest_file)


    # with open(h_path, 'w') as f:
    #     f.write(header_content)

    # with open(cpp_path, 'w') as f:
    #     f.write(source_content)


if __name__ == "__main__":
    main()
