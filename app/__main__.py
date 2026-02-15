import impl
import config

import argparse
from enum import Enum
from pathlib import Path


class ModelClassification(Enum):
    CLASS       = "class"
    INTERFACE   = "interface"
    ENUM        = "enum"


class ModelInfo:
    def __init__(self,
                 model_name: str,
                 model_type: str,
                 model_namespaces: list[str],
                 model_include_guard: str
                 ):
        self._name: str                             = model_name
        self._classification: ModelClassification   = ModelClassification(model_type)
        self._namespaces: list[str]                 = model_namespaces
        self._include_guard: str                    = model_include_guard

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def classification(self) -> ModelClassification:
        return self._classification
    
    @property
    def namespaces(self) -> list[str]:
        return self._namespaces
    
    @property
    def include_guard(self) -> str:
        return self._include_guard


# Create generator
GENERATOR = impl.CppGenerator(
    config.JINJA_ENV_PACKAGE,
    config.CLASS_HEADER_TEMPLATE_FILENAME,
    config.CLASS_SOURCE_TEMPLATE_FILENAME,
    config.INTERFACE_HEADER_TEMPLATE_FILENAME,
    config.ENUM_HEADER_TEMPLATE_FILENAME
)


# Create Parser
PARSER = impl.Parser(
    config.STANDARD_INCLUDE_MAP
)


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

    input_path: Path    = Path(args.input).resolve()
    output_path: Path   = Path(args.output).resolve()
    create_backup: bool = args.backup

    # Instrument files
    file_models_info: dict[str, ModelInfo] = {}
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
        file_models_info[yaml_path] = ModelInfo(base_name, model_type, namespaces, include_guard)

    # Parse yamls and generate files
    for yaml_path in input_path.rglob("*.yaml"):
        model_info: ModelInfo = file_models_info[yaml_path]

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
        PARSER.set_model(model)
        PARSER.parse_yaml(yaml_path.read_text())

        match model_info.classification:
            case ModelClassification.CLASS:
                # Generate text for header and cpp
                header_content: str = GENERATOR.generate_class_header_content(model)
                source_content: str = GENERATOR.generate_class_source_content(model)
            case ModelClassification.INTERFACE:
                header_content: str = GENERATOR.generate_interface_header_content(model)
                source_content: str = None
            case ModelClassification.ENUM:
                header_content: str = GENERATOR.generate_enum_header_content(model)
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


if __name__ == "__main__":
    main()
