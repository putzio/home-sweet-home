from table import Table
from dataclasses import dataclass


@dataclass
class AlarmTable(Table):
    def __init__(self):
        self.name = "alarms"
        self.columns = {"id": "INT AUTO_INCREMENT PRIMARY KEY", "time": "VARCHAR(255)", "description": "VARCHAR(255)"}

        # initialise the base class (self.values dictionary) based on self.columns
        super().__init__()

    def add_alarm(self, time: str, description: str):
        self._add_record(time=time, description=description)


if __name__ == "__main__":
    from database import Database

    alarm_table = AlarmTable()
    alarm_table.add_alarm("2021-01-01 12:00:00", "Wake up")
    alarm_table.add_alarm("2021-01-01 12:00:00", "Wake up")
    print(alarm_table.get_all_columns())
    print(alarm_table.get_values_to_insert())

    db = Database()
    db.init()
    db.create_table(alarm_table)
    db.print_table(alarm_table.name)
    db.insert(alarm_table)
    recieved = db.get_table_in_rows(alarm_table)
    print(f"Recieved: {recieved}")
    db.delete(alarm_table.name, "id>1")
    db.print_table(alarm_table.name)
    del db
