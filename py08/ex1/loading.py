import sys
from importlib import import_module


def detect_package_manager() -> str:
    if "pypoetry" in sys.prefix.lower():
        return "poetry"
    try:
        open("poetry.lock").close()
        return "poetry"
    except FileNotFoundError:
        pass
    return "pip"


def check_dependencies() -> list[str]:
    # Thanks subject for saying but not showing in example that we need it
    manager = detect_package_manager()
    print()
    print(f"LOADING STATUS: Loading programs... [package manager: {manager}]")
    dependencies = ["pandas", "numpy", "matplotlib"]
    missing = []
    print()

    print("Checking dependencies:")
    for pkg in dependencies:
        try:
            mod = import_module(pkg)
            ver = mod.__version__
            labels = {
                "pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "matplotlib": "Visualization ready",
            }
            print(f"[OK] {pkg} ({ver}) - {labels.get(pkg, 'ready')}")
        except ImportError:
            print(f"[MISSING] {pkg} - NOT INSTALLED")
            missing.append(pkg)
    print()
    return missing


def show_missing(missing: list[str]) -> None:
    print("Missing required dependencies:", ", ".join(missing))
    print()
    print("To install with pip:")
    print("  pip install -r requirements.txt")
    print()
    print("To install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def generate_matrix_data() -> object:  # wish we were allowed to use any
    import numpy
    data = numpy.random.randn(1000)
    return data


def analyze(data: object) -> object:
    import pandas  # type: ignore[import-untyped]
    print("Analyzing Matrix data...")
    print(f"Processing {len(data)} data points...")  # type: ignore[arg-type]

    data_frame = pandas.DataFrame({"value": data})
    return data_frame.describe()


def visualize(data_frame: object, output: str) -> None:
    import matplotlib
    import matplotlib.pyplot as plt

    print("Generating visualization...")
    matplotlib.use("Agg")  # non-interactive backend
    data_frame["value"].plot(title="Matrix Data")  # type: ignore[index]
    plt.savefig(output)
    plt.close()


if __name__ == "__main__":
    missing = check_dependencies()

    if missing:
        show_missing(missing)
        sys.exit(1)

    data = generate_matrix_data()
    data_frame = analyze(data)
    output = "matrix_analysis.png"
    visualize(data_frame, output)

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output}")
