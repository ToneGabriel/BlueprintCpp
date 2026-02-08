import impl
import config

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


def main() -> None:
    args = parse_arguments()

    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()
    create_backup: bool = args.backup

    # Instrument files
    file_models: dict[str, impl.Model] = {}
    project_include_map: dict[str, str] = {}

    for yaml_path in input_path.rglob("*.yaml"):
        relative_dir = yaml_path.parent.relative_to(input_path)
        base_name = yaml_path.name.removesuffix("".join(yaml_path.suffixes))

        namespaces = list(relative_dir.parts)
        h_path = relative_dir / f"{base_name}.h"

        typename_parts = namespaces + [base_name]
        typename = "::".join(typename_parts)

        include_guard_parts = typename_parts + ["H"]
        include_guard = "_".join(s.upper() for s in include_guard_parts)

        model = impl.Model(base_name, namespaces, include_guard)

        file_models[yaml_path] = model
        project_include_map[typename] = str(h_path)

    # Create generator
    generator = impl.CppGenerator(
        config.JINJA_ENV_PACKAGE,
        config.HEADER_TEMPLATE_FILENAME,
        config.SOURCE_TEMPLATE_FILENAME
    )

    # Create Parser
    parser = impl.Parser(
        config.STANDARD_INCLUDE_MAP,
        project_include_map
    )

    # Parse yamls and generate files
    for yaml_path in input_path.rglob("*.yaml"):
        model = file_models[yaml_path]

        # Parse yaml and append info to model
        parser.set_model(model)
        parser.parse_yaml(yaml_path.read_text())

        # Load model
        generator.set_model(model)
        header_content = generator.generate_header_content()
        # source_content = generator.generate_source_content()

        # Preserve directory structure
        relative_dir = yaml_path.parent.relative_to(input_path)
        destination_dir = output_path / relative_dir
        destination_dir.mkdir(parents=True, exist_ok=True)

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
        # source_file.write_text(source_content)


if __name__ == "__main__":
    main()
