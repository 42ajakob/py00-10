from abc import ABC, abstractmethod
from typing import Any, TypeGuard, Protocol


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
            self.values.append((self.processed, str(data)))
            self.processed += 1
        elif isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            for x in data:
                self.values.append((self.processed, str(x)))
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
            self.values.append((self.processed, data))
            self.processed += 1
        elif isinstance(data, list) and all(
            isinstance(x, str) for x in data
        ):
            for x in data:
                self.values.append((self.processed, x))
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
                (self.processed, ": ".join(v.strip() for v in data.values()))
            )
            self.processed += 1
        elif isinstance(data, list) and all(_is_dict_str(x) for x in data):
            for item in data:
                joined = ": ".join(v.strip() for v in item.values())
                self.values.append((self.processed, joined))
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.proc_list:
            data: list[tuple[int, str]] = []
            for _ in range(min(nb, len(proc.values))):
                data.append(proc.output())
            plugin.process_output(data)

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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = ", ".join(
            f'"item_{idx}": "{value}"'
            for idx, value in data
        )
        print("{" + pairs + "}")


def data_processor() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()

    print("Initialize Data Stream...")
    stream = DataStream()
    # Why is there now a new line???
    print()
    stream.print_processors_stats()

    print("Registering Processors")
    numProc = NumericProcessor()
    txtProc = TextProcessor()
    logProc = LogProcessor()
    stream.register_processor(numProc)
    stream.register_processor(txtProc)
    stream.register_processor(logProc)
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
    # Another...
    print()
    stream.print_processors_stats()

    # New prints
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()

    stream.print_processors_stats()

    new_data = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"Send another batch of data: {new_data}")
    stream.process_stream(new_data)
    print()

    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()

    stream.print_processors_stats()


if __name__ == "__main__":
    data_processor()
