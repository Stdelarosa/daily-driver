import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QIcon

def get_data_dir():
    """Get the appropriate directory for storing application data"""
    if os.name == 'nt':
        data_dir = os.path.join(os.environ['APPDATA'], 'DailyDriver')
    else:
        data_dir = os.path.join(os.path.expanduser('~'), '.dailydriver')
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    return data_dir

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daily Driver")
        self.setFixedSize(700, 800)
        self.setStyleSheet("background-color: #222;")
        self.setWindowIcon(QIcon(self.get_resource_path("resources/icon.ico")))
        self.data_dir = get_data_dir()
        self.tasks_file = os.path.join(self.data_dir, 'tasks.json')
        self.init_ui()

    def get_resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
            
        return os.path.join(base_path, relative_path)
    
    def init_ui(self):
        app_font = QFont("White Rabbit", 11)
        QApplication.setFont(app_font)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 40)
        main_layout.setSpacing(15)

        calendar_container = QWidget()
        calendar_container.setStyleSheet(
            "background-color: #333; border-radius: 10px; padding: 10px;"
        )
        calendar_container.setFixedHeight(50)
        calendar_layout = QHBoxLayout(calendar_container)
        calendar_layout.setSpacing(10)
        self.days_of_week_buttons = []
        days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

        for i, day in enumerate(days):
            button = QPushButton(day)
            button.setCheckable(True)
            button.setStyleSheet("color: #fff; background-color: #444;")
            self.days_of_week_buttons.append(button)
            calendar_layout.addWidget(button)

        current_day = (QDate.currentDate().dayOfWeek() % 7)
        self.days_of_week_buttons[current_day].setChecked(True)
        self.days_of_week_buttons[current_day].setStyleSheet("color: #fff; background-color: #99B7C1;")

        current_day_label = QLabel(QDate.currentDate().toString("MM/dd/yyyy"))
        current_day_label.setStyleSheet("color: #fff; margin-left: 10px;")
        calendar_layout.addWidget(current_day_label)

        main_layout.addWidget(calendar_container)

        mit_section = QVBoxLayout()
        mit_section.setSpacing(0) 

        mit_label = QLabel("MOST IMPORTANT TASK")
        mit_label.setFont(QFont("White Rabbit", 12, QFont.Bold))
        mit_label.setStyleSheet("color: #fff; margin-top: 20px; margin-bottom: 5px;")
        mit_section.addWidget(mit_label)

        mit_subtext = QLabel("The one sure thing you want to get done today.")
        mit_subtext.setFont(QFont("White Rabbit", 11))
        mit_subtext.setStyleSheet("color: #aaa; margin-bottom: 3px;")
        mit_section.addWidget(mit_subtext)

        mit_layout = QVBoxLayout()
        mit_layout.addLayout(mit_section)

        mit_task_layout = QHBoxLayout()
        mit_task_layout.setContentsMargins(0, 0, 0, 0)
        self.mit_checkbox = QCheckBox()
        self.mit_checkbox.setStyleSheet("color: #fff;")
        mit_task_layout.addWidget(self.mit_checkbox)

        self.mit_input = QLineEdit()
        self.mit_input.setPlaceholderText("Type something...")
        self.mit_input.setStyleSheet(
            "background-color: #333; color: #fff; padding: 10px; border: 2px solid #555;"
            "border-radius: 5px;"
        ) 
        mit_task_layout.addWidget(self.mit_input)

        mit_layout.addLayout(mit_task_layout)
        main_layout.addLayout(mit_layout)

        might_do_section = QVBoxLayout()
        might_do_section.setSpacing(10)

        might_do_label = QLabel("MIGHT-DO LIST")
        might_do_label.setFont(QFont("White Rabbit", 12, QFont.Bold))
        might_do_label.setStyleSheet("color: #fff; margin-top: 20px; margin-bottom: 0px;")
        might_do_section.addWidget(might_do_label)

        might_do_subtext = QLabel("What you may or may not do today.")
        might_do_subtext.setFont(QFont("White Rabbit", 11))
        might_do_subtext.setStyleSheet("color: #aaa;")
        might_do_section.addWidget(might_do_subtext)

        might_do_layout = QVBoxLayout()
        might_do_layout.addLayout(might_do_section)

        # Create 10 checkboxes
        self.might_do_tasks = []
        for _ in range(10):
            task_layout = QHBoxLayout()
            task_layout.setSpacing(10)
            checkbox = QCheckBox()
            checkbox.setStyleSheet("color: #fff;")
            input_field = QLineEdit()
            input_field.setPlaceholderText("Enter task...")
            input_field.setStyleSheet(
                "background-color: #333; color: #fff; padding: 5px; border: 2px solid #555;"
                "border-radius: 5px;"
            ) 
            task_layout.addWidget(checkbox)
            task_layout.addWidget(input_field)

            self.might_do_tasks.append((checkbox, input_field))
            might_do_layout.addLayout(task_layout)

        main_layout.addLayout(might_do_layout)

        bottom_layout = QHBoxLayout()
        
        sudosaint_label = QLabel('<a href="https://github.com/Stdelarosa" style="color: #b8eeff; text-decoration: none;">sudosaint</a>')
        sudosaint_label.setFont(QFont("White Rabbit", 11))
        sudosaint_label.setOpenExternalLinks(True)
        sudosaint_label.setStyleSheet("""
            QLabel a {
                color: #b8eeff; 
                text-decoration: none;
            }
            QLabel a:hover {
                color: #8ad5f0;
                text-decoration: none;
            }
        """)
        bottom_layout.addWidget(sudosaint_label)
        
        bottom_layout.addStretch()

        clear_button = QPushButton("↻") 
        clear_button.setFixedSize(30, 30)
        clear_button.setStyleSheet(
            "background-color: #444; color: #fff; border: none; border-radius: 10px;"
        )
        clear_button.clicked.connect(self.clear_tasks) 
        bottom_layout.addWidget(clear_button, alignment=Qt.AlignRight)

        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        self.load_tasks()

    def save_tasks(self):
        tasks = {
            "most_important_task": {
                "text": self.mit_input.text(),
                "checked": self.mit_checkbox.isChecked(),
            },
            "might_do_tasks": [
                {"text": input_field.text(), "checked": checkbox.isChecked()}
                for checkbox, input_field in self.might_do_tasks
            ],
        }
        try:
            with open(self.tasks_file, "w") as file:
                json.dump(tasks, file)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        try:
            if os.path.exists(self.tasks_file):
                with open(self.tasks_file, "r") as file:
                    tasks = json.load(file)
                    self.mit_input.setText(tasks["most_important_task"]["text"])
                    self.mit_checkbox.setChecked(tasks["most_important_task"]["checked"])

                    for (checkbox, input_field), task in zip(self.might_do_tasks, tasks["might_do_tasks"]):
                        input_field.setText(task["text"])
                        checkbox.setChecked(task["checked"])
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def clear_tasks(self):
        self.mit_checkbox.setChecked(False)
        self.mit_input.clear()

        for checkbox, input_field in self.might_do_tasks:
            checkbox.setChecked(False)
            input_field.clear()

        try:
            with open(self.tasks_file, "w") as file:
                file.write("{}")
        except Exception as e:
            print(f"Error clearing tasks: {e}")

    def closeEvent(self, event):
        self.save_tasks()
        super().closeEvent(event)

app = QApplication(sys.argv)
window = ToDoApp()
window.show()
sys.exit(app.exec_())