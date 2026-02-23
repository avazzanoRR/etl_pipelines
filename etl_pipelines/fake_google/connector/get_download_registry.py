from pathlib import Path

def get_download_registry_path(registry_name: str) -> str:
    """Get file path within the package that works in both dev and pip installation."""
    # Navigate to the package root and then to the target file
    package_root = Path(__file__).resolve().parent
    file_path = package_root / "download_registries" / f"{registry_name}.yaml"

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return str(file_path)