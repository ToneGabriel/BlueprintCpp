from importlib.resources import files
from jinja2 import Environment, FileSystemLoader

def create_jinja_env():
    template_dir = files("templates")

    return Environment(loader=FileSystemLoader(str(template_dir)),
                       trim_blocks=True,
                       lstrip_blocks=True
                       )

if __name__ == "__main__":
    print(str(files("templates")))
