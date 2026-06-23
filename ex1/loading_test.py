import importlib
import importlib.metadata


class DependencyInfo:
    def __init__(
            self, name: str,
            available: bool,
            description: str,
            version: str | None = None):

        self.name = name
        self.available = available
        self.version = version
        self.description = description

    def show_info(self):
        if self.available:
            print(f"[OK] {self.name} ({self.version}) - {self.description} ready")
        else:
            print(f"[MISSING] {self.name} - package not installed")


def check_dependencies(
        dependencies: list[tuple[str, str]]) -> dict[str, DependencyInfo]:
    print("Checking dependencies:")
    all_deps: dict[str, DependencyInfo] = {}

    for key, value in dependencies:
        try:
            importlib.import_module(key)
        except ImportError:
            all_deps[key] = DependencyInfo(
                key, available=False, description=value, version=None)
            continue
        
        try:
            version = importlib.metadata.version(key)
        except importlib.metadata.PackageNotFoundError:
            version = None

        all_deps[key] = DependencyInfo(
            key, available=True, description=value, version=version)

    for dep in all_deps.values():
        dep.show_info()

    for dep in all_deps.values():
        if not dep.available:
            print("\nSome dependencies are missing.")
            print("Install with: pip install -r requirements.txt")
            print("Or with Poetry: poetry install")
            break

    return all_deps 


def main() -> None:
    print(f"\nLOADING STATUS: Loading programs...\n")
    dependencies: list[tuple[str, str]] = [
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computation"),
        ("matplotlib", "Visualization")
    ]
    check_dependencies(dependencies)
    # Analyzing Matrix data...

    
    

if __name__ == "__main__":
    main()
