import importlib
import importlib.metadata


class DependencyInfo:
    def __init__(
            self, name: str,
            available: bool,
            version: str | None = None,
            description: str | None = None
    ) -> None:

        self.name = name
        self.available = available
        self.version = version
        self.description = description

    def show_info(self) -> None:
        if self.available:
            print(f"[OK] {self.name} ({self.version}) - {self.description} ready")
        else:
            print(f"[MISSING] {self.name} - package not installed")


def check_dependency(dependency: str, description: str | None = None) -> DependencyInfo:
    try:
        importlib.import_module(dependency)
    except ImportError:
        return DependencyInfo(dependency, available=False, description=description)

    try:
        version = importlib.metadata.version(dependency)
    except importlib.metadata.PackageNotFoundError:
        version = None
    return DependencyInfo(dependency, available=True, version=version, description=description)


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies")
    dependencies = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization"
        }
    dep_obj: list[DependencyInfo] = []

    for dep, description in dependencies.items():
        dep_obj.append(check_dependency(dep, description=description))

    for element in dep_obj:
        element.show_info()

    for element in dep_obj:
        if not element.available:
            print("\nSome dependencies are missing.")
            print("Install with: pip install -r requirements.txt")
            print("Or with Poetry: poetry install")
            break
    

if __name__ == "__main__":
    main()
