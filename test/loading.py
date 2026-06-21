import importlib


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
    pass


main()
