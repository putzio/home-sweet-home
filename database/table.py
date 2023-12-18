import mysql.connector
from dataclasses import dataclass, field
from typing import Dict, List
import abc


@dataclass
class Table:
    """
    A Base class for all tables in the database
    """

    name: str
    columns: dict
    values: Dict[str, List[str]] = field(default_factory=dict)

    def __init__(self):
        self.values = {key: [] for key in self.columns.keys() if key != "id"}

    def get_all_columns(self):
        result = ""
        for key, value in self.columns.items():
            result += f"{key} {value}, "
        return result[:-2]

    def get_column_names_to_insert(self):
        return ", ".join([key for key in self.columns.keys() if key != "id"])

    def get_values_to_insert(self) -> List[str]:
        result = []
        keys = list(self.values.keys())
        if keys is None or len(keys) == 0 or len(self.values[keys[0]]) == 0:
            return result

        number_of_rows = len(self.values[keys[0]])
        for i in range(number_of_rows):
            result.append(", ".join(str(self.values[key][i]) for key in keys))
        return result

    def _add_record(self, **kwargs):
        for key, value in kwargs.items():
            self.values[key].append(f"'{value}'")
