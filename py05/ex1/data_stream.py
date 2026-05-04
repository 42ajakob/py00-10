from abc import ABC, abstractmethod
from typing import Any, TypeGuard


def _is_dict_str(d: Any) -> TypeGuard[dict[str, str]]:
    return isinstance(d, dict) and all(
        isinstance(k, str) and isinstance(v, str) for k, v in d.items()
    )


class DataProcessor(ABC):
    def __init__(self):
        self.values: list[tuple[int, str]] = []
        self.processed = 0

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
            self.processed += 1
        elif isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            for x in data:
                self.values.append((len(self.values), str(x)))
                self.processed += 1
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
            self.processed += 1
        elif isinstance(data, list) and all(
            isinstance(x, str) for x in data
        ):
            for x in data:
                self.values.append((len(self.values), x))
                self.processed += 1
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
            self.processed += 1
        elif isinstance(data, list) and all(_is_dict_str(x) for x in data):
            for item in data:
                joined = ": ".join(v.strip() for v in item.values())
                self.values.append((len(self.values), joined))
                self.processed += 1
        else:
            raise ValueError("Improper log data")


class DataStream():
    def __init__(self):
        self.proc_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.proc_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            processed = False
            for proc in self.proc_list:
                if proc.validate(data):
                    proc.ingest(data)
                    processed = True
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {data}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.proc_list:
            print("No processor found, no data")
        else:
            for proc in self.proc_list:
                if proc.__class__ == NumericProcessor:
                    print("Numeric Processor: ", end="")
                elif proc.__class__ == TextProcessor:
                    print("Text Processor: ", end="")
                elif proc.__class__ == LogProcessor:
                    print("Log Processor: ", end="")
                print(
                    f"total {proc.processed} items processed, "
                    f"remaining {len(proc.values)} on processor"
                )
        print()


def data_processor() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Numeric Processor")
    numProc = NumericProcessor()
    stream.register_processor(numProc)
    print()

    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("Registering other data processors")
    txtProc = TextProcessor()
    logProc = LogProcessor()
    stream.register_processor(txtProc)
    stream.register_processor(logProc)
    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numProc.output()
    for _ in range(2):
        txtProc.output()
    logProc.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    data_processor()
