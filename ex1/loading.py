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
            if dep.name == "requests":
                continue
            print("\nSome dependencies are missing.\nInstall them with:")
            print("- Pip: activate venv then pip install -r requirements.txt or\n"
                  "- Poetry: poetry install")
            return None
    return all_deps


def generate_matrix_data(n: int, numpy_module: object) -> object:
    print(f"\nProcessing {n} data points")
    generator = numpy_module.random.default_rng()  # type: ignore[attr-defined]
    data = generator.normal(size=n)
    return data


def build_dataframe(data: object, pandas_module: object) -> object:
    data_frame = pandas_module.DataFrame({"signal": data})  # type: ignore[attr-defined]
    data_frame["rolling_mean"] = data_frame["signal"].rolling(window=10).mean()
    return data_frame


def generate_visualization(data_frame: object, matplotlib_module: object) -> str:
    plt = importlib.import_module("matplotlib.pyplot")  # type: ignore[attr-defined]
    fig, ax = plt.subplots()
    ax.plot(data_frame["signal"])
    ax.set_title("Matrix Data Analysis")
    output_path = "matrix_analysis.png"
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    dependencies: list[tuple[str, str]] = [
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computation"),
        ("matplotlib", "Visualization"),
    ]
    
    all_deps = check_dependencies(dependencies)
    if not all_deps:
        return 
    
    # Analyzing Matrix data...
    n = 1000
    data = generate_matrix_data(n, all_deps["numpy"].module)
    data_frame = build_dataframe(data, all_deps["pandas"].module)
    print(data_frame)
    visualization = generate_visualization(data_frame, all_deps["matplotlib"].module)
    print(visualization)

if __name__ == "__main__":
    main()
