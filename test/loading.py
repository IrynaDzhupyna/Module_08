import importlib
import importlib.metadata


class DependencyStatus:
    def __init__(self, available: bool, version: str | None) -> None:
        self.available = available
        self.version = version


def check_dependency(dependency: str) -> DependencyStatus:
    try:
        importlib.import_module(dependency)
    except ImportError:
        return DependencyStatus(available=False, version=None)
    else:
        try:
            return DependencyStatus(
                available=True,
                version=importlib.metadata.version(dependency))
        except importlib.metadata.PackageNotFoundError:
            return DependencyStatus(available=True, version=None)


def main() -> None:
    # check dependenies: pandas, numpy, matplotlib
    dependencies = ["pandas", "numpy", "matplotlib"]
    dep_dict = {}
    for dependency in dependencies:
        status = check_dependency(dependency)
        dep_dict[dependency] = status.available, status.version
    
    print("LOADING STATUS: Loading programs...i\n")
    print("Checking dependencies:")

    for dep in dep_dict:
        pass

    print(dep_dict)

    
if __name__ == "__main__":
    main()
