import app.impl as impl
import app.config as config
import app.ui as ui


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
    # Parse executable arguments
    args = parse_arguments()

    input_path: Path    = Path(args.input).resolve()
    output_path: Path   = Path(args.output).resolve()
    create_backup: bool = args.backup

    # Create generator
    GENERATOR = impl.CppGenerator(
        config.GENERATOR_NAME_AND_VERSION,
        config.JINJA_ENV_PACKAGE,
        config.CLASS_HEADER_TEMPLATE_FILENAME,
        config.CLASS_SOURCE_TEMPLATE_FILENAME,
        config.INTERFACE_HEADER_TEMPLATE_FILENAME,
        config.ENUM_HEADER_TEMPLATE_FILENAME,
        config.TAB_INDENT
    )

    # Create Parser
    PARSER = impl.Parser(
        config.STANDARD_INCLUDE_MAP
    )

    # Instrument files
    file_models_info: dict[str, impl.ModelInfo] = {}
    for yaml_path in input_path.rglob("*.yaml"):
        relative_dir = yaml_path.parent.relative_to(input_path)
        base_name, model_type = yaml_path.stem.rsplit(".", 1)

        namespaces = list(relative_dir.parts)
        h_path = relative_dir / f"{base_name}.h"

        typename_parts = namespaces + [base_name]
        typename = "::".join(typename_parts)

        include_guard_parts = typename_parts + ["H"]
        include_guard = "_".join(s.upper() for s in include_guard_parts)

        PARSER.add_project_include(typename, str(h_path))
        file_models_info[yaml_path] = impl.ModelInfo(base_name, model_type, namespaces, include_guard)

    # Parse yamls and generate files
    for yaml_path in input_path.rglob("*.yaml"):
        model_info: impl.ModelInfo = file_models_info[yaml_path]

        # Create general model
        model: impl.Model = impl.Model(model_info.name, model_info.namespaces, model_info.include_guard)

        # Preserve directory structure
        relative_dir: Path = yaml_path.parent.relative_to(input_path)
        destination_dir: Path = output_path / relative_dir
        destination_dir.mkdir(parents=True, exist_ok=True)

        # Output filenames
        header_file: Path = destination_dir / f"{model_info.name}.h"
        source_file: Path = destination_dir / f"{model_info.name}.cpp"

        # Parse yaml and append info to model
        PARSER.parse_yaml(model, yaml_path.read_text())

        match model_info.classification:
            case impl.ModelClassification.CLASS:
                # Generate text for header and cpp
                header_content: str = GENERATOR.generate_class_header_content(model, yaml_path, header_file.relative_to(output_path))
                source_content: str = GENERATOR.generate_class_source_content(model, yaml_path, source_file.relative_to(output_path))
            case impl.ModelClassification.INTERFACE:
                header_content: str = GENERATOR.generate_interface_header_content(model, yaml_path, header_file.relative_to(output_path))
                source_content: str = None
            case impl.ModelClassification.ENUM:
                header_content: str = GENERATOR.generate_enum_header_content(model, yaml_path, header_file.relative_to(output_path))
                source_content: str = None

        # Backup if requested
        if create_backup:
            for file in (header_file, source_file):
                if file.exists():
                    file.rename(file.with_name(file.name + ".bak"))

        if header_content:
            header_file.write_text(header_content)

        if source_content:
            source_file.write_text(source_content)


def main_ui() -> None:
    manager = ui.AppManager()

    env = ui.UiEnvironment()

    logger  = ui.LoggerWrapper(env.get_logger_widget())
    menu    = ui.MenuWrapper(env.get_menubar_widget(), env.get_menubar_action_widgets())
    tree    = ui.TreeWrapper(env.get_tree_widget())
    table   = ui.TableWrapper(env.get_table_widget())

    manager.set_logger_reference(logger)
    manager.set_menu_reference(menu)
    manager.set_table_reference(table)
    manager.set_tree_reference(tree)

    logger.set_manager_reference(manager)
    menu.set_manager_reference(manager)
    tree.set_manager_reference(manager)
    table.set_manager_reference(manager)

    env.run()


if __name__ == "__main__":
    # main()
    main_ui()
