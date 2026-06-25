import importlib
import importlib.metadata


class DependencyInfo:
    def __init__(
            self, name: str,
            available: bool,
            description: str,
            version: str | None = None,
            module: object | None = None) -> None:

        self.name = name
        self.available = available
        self.version = version
        self.description = description
        self.module = module

    def show_info(self) -> None:
        if self.available:
            print(f"[OK] {self.name} ({self.version}) - {self.description} ready")
        else:
            print(f"[MISSING] {self.name} - package not installed")


def check_dependencies(
        dependencies: list[tuple[str, str]]) -> dict[str, DependencyInfo] | None:
    print("Checking dependencies:")
    all_deps: dict[str, DependencyInfo] = {}

    for key, value in dependencies:
        try:
            module = importlib.import_module(key)
        except ImportError:
            all_deps[key] = DependencyInfo(
                key, available=False, description=value, version=None, module=None)
            continue
        
        try:
            version = importlib.metadata.version(key)
        except importlib.metadata.PackageNotFoundError:
            version = None

        all_deps[key] = DependencyInfo(
            key, available=True, description=value, version=version, module = module)

    for dep in all_deps.values():
        dep.show_info()

    for dep in all_deps.values():
        if not dep.available:
            print("\nSome dependencies are missing. Install them with:")
            print("pip: pip install -r requirements.txt\n"
                  "Or\nPoetry: poetry install")
            return None
    return all_deps


def generate_matrix_data(n: int, module) -> "numpy.ndarray":
    generator = module.random.default_rng()
    print(generator)


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    dependencies: list[tuple[str, str]] = [
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computation"),
        ("matplotlib", "Visualization")
    ]
    
    all_deps = check_dependencies(dependencies)
    if not all_deps:
        return 
    
    # Analyzing Matrix data...

    generate_matrix_data(1000, all_deps["numpy"].module)


if __name__ == "__main__":
    main()
