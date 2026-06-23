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

    def dependency_discription(self, name: str) -> str:
        if name == "pandas":
            return "Data manipulation"
        elif name == "numpy":
            return "Numerical computation"
        elif name == "matplotlib":
            return "Network access"

    def show_info(self):
        if self.available:
            print(f"[OK] {self.name} ({self.version}) - {self.dependency_discription(self.name)} ready")
        print(f"[MISSING] {self.name} - package not installed")


def check_dependencies(dependencies: list) -> DependencyInfo:
    print("Checking dependencies")
    dependencies_info = []

    for dependency in dependencies:
        try:
            importlib.import_module(dependency)
        except ImportError:
            dependencies_info.append(
                DependencyInfo(dependency, available=False))

        try:
            version = importlib.metadata.version(dependency)
        except importlib.metadata.PackageNotFoundError:
            version = None
        dependencies_info.append(
            DependencyInfo(dependency, available=True, version=version))
    return dependencies_info



def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    dep_to_check = ["pandas", "numpy", "matplotlib"]
    dependencies = check_dependencies(dep_to_check)
    for dep in dependencies:
        dep.show_info()


'''
    dep_obj = []
    all_available = False

    for dep in dependencies:
        dep_obj.append(check_dependency(dep))
    for element in dep_obj:
        element.show_info()'''

if __name__ == "__main__":
    main()
