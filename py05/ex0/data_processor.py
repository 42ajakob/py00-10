from abc import ABC, abstractmethod
from typing import Any, TypeGuard


def _is_dict_str(d: Any) -> TypeGuard[dict[str, str]]:
    return isinstance(d, dict) and all(
        isinstance(k, str) and isinstance(v, str) for k, v in d.items()
    )


class DataProcessor(ABC):
    def __init__(self):
        self.values: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.values.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, (int, float)) or (
            isinstance(data, list) and all(
                isinstance(x, (int, float)) for x in data
            )
        )

    def ingest(self, data: Any) -> None:
        if isinstance(data, (int, float)):
            self.values.append((len(self.values), str(data)))
        elif isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            for x in data:
                self.values.append((len(self.values), str(x)))
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) or (
            isinstance(data, list) and all(isinstance(x, str) for x in data)
        )

    def ingest(self, data: Any) -> None:
        if isinstance(data, str):
            self.values.append((len(self.values), data))
        elif isinstance(data, list) and all(
            isinstance(x, str) for x in data
        ):
            for x in data:
                self.values.append((len(self.values), x))
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return _is_dict_str(data) or (
            isinstance(data, list) and all(_is_dict_str(x) for x in data)
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if _is_dict_str(data):
            self.values.append(
                (len(self.values), ": ".join(v.strip() for v in data.values()))
            )
        elif isinstance(data, list) and all(_is_dict_str(x) for x in data):
            for item in data:
                joined = ": ".join(v.strip() for v in item.values())
                self.values.append((len(self.values), joined))
        else:
            raise ValueError("Improper log data")


def data_processor() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()

    print("Testing Numeric Processor...")
    numProc = NumericProcessor()

    print(" Trying to validate input '42': ", end="")
    print(f"{numProc.validate(42)}")

    print(" Trying to validate input 'Hello': ", end="")
    print(f"{numProc.validate("Hello")}")

    try:
        print(
            " Test invalid ingestion of string 'foo' without prior validation:"
        )
        numProc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    num_data = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_data}")
    numProc.ingest(num_data)

    print(" Extracting 3 values...")
    for _ in range(3):
        idx, val = numProc.output()
        print(f" Numeric value {idx}: {val}")
    print()

    print("Testing Text Processor...")
    txtProc = TextProcessor()

    print(" Trying to validate input '42': ", end="")
    print(f"{txtProc.validate(42)}")

    txt_data = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {txt_data}")
    txtProc.ingest(['Hello', 'Nexus', 'World'])

    print(" Extracting 1 value...")
    idx, val = txtProc.output()
    print(f" Text value {idx}: {val}")
    print()

    print("Testing Log Processor...")
    logProc = LogProcessor()

    print(" Trying to validate input 'Hello': ", end="")
    print(f"{logProc.validate('Hello')}")

    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {log_data}")
    logProc.ingest(log_data)
    print(" Extracting 2 values...")
    for _ in range(2):
        idx, val = logProc.output()
        print(f" Log entry {idx}: {val}")


if __name__ == "__main__":
    data_processor()
