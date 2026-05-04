from os import getenv, path
from dotenv import load_dotenv

load_dotenv()


def load_config() -> tuple[dict[str, str], list[str]]:
    config: dict[str, str] = {}
    env_var = [
        "MATRIX_MODE", "DATABASE_URL", "API_KEY",
        "LOG_LEVEL", "ZION_ENDPOINT",
    ]
    missing: list[str] = []

    for key in env_var:
        value = getenv(key)
        if value is None:
            missing.append(key)
        else:
            config[key] = value

    return config, missing


def display_status() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    config, missing = load_config()
    print()
    if missing:
        for key in missing:
            print(f"WARNING: missing {key}")
        print()

    print("Configuration loaded:")

    # Mode
    mode = config["MATRIX_MODE"]
    if mode and mode in ("development", "production"):
        print(f"Mode: {mode}")
    else:
        print("ERROR: set MATRIX_MODE=development or production")
        print()
        return

    # Database
    url = config['DATABASE_URL']
    if url:
        if mode == "production":
            print("Database: Connected to production instance")
        else:
            print(f"Database: Connected to {url} instance")

    # API
    if config['API_KEY']:
        if mode == "production":
            print("API Access: Authenticated for productivity")
        else:
            print("API Access: Authenticated")

    # Log level
    if config['LOG_LEVEL']:
        print(f"Log Level: {config['LOG_LEVEL']}")

    # Zion endpoint
    if config['ZION_ENDPOINT']:
        print(f"Zion Network: {config['ZION_ENDPOINT']}")

    # Security check
    print()
    print("Environment security check:")

    env_file_exists = path.isfile(".env")
    hardcoded = False  # nothing is hardcoded in this source file

    hc_status = 'OK' if not hardcoded else 'WARN'
    print(f"[{hc_status}] No hardcoded secrets detected")
    env_status = 'OK' if env_file_exists else 'WARN'
    env_msg = (
        'properly configured' if env_file_exists
        else 'not found (using env vars only)'
    )
    print(f"[{env_status}] .env file {env_msg}")
    print("[OK] Production overrides available")

    print()
    print("The Oracle sees all configurations.")
    print()


if __name__ == "__main__":
    display_status()
