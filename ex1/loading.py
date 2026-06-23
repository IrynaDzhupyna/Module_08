import importlib
import importlib.metadata


class DependencyInfo:
    def __init__(
            self, name: str,
            available: bool,
            version: str | None = None):

        self.name = name
        self.available = available
        self.version = version

    def show_info(self):
        if self.available:
            print(f"[OK] {self.name} ({self.version})")
        else:
            print(f"[MISSING] {self.name} - package not installed")


def check_dependency(dependency: str) -> DependencyInfo:
    try:
        importlib.import_module(dependency)
    except ImportError:
        return DependencyInfo(dependency, available=False)

    try:
        version = importlib.metadata.version(dependency)
    except importlib.metadata.PackageNotFoundError:
        version = None
    return DependencyInfo(dependency, available=True, version=version)


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies")
    dependencies = ["pandas", "numpy", "matplotlib"]
    dep_obj = []
    all_available = False

    for dep in dependencies:
        dep_obj.append(check_dependency(dep))

    for element in dep_obj:
        element.show_info()

if __name__ == "__main__":
    main()
