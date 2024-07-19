"""Functions for configuring paths."""

from pathlib import Path


def get_project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).parent.parent.parent


def image_path(file_name: str) -> Path:
    """Create a Path object for the image file to the docs/images folder with the
    same name as the file name.
    """
    project_root = get_project_root()
    docs_images_dir = project_root / "docs" / "images"
    file_name = file_name.replace(".py", "")

    outfile = docs_images_dir / f"{file_name}.png"

    return outfile
