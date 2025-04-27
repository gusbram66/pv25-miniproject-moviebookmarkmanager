import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QLineEdit, QComboBox, QSpinBox, QCheckBox, QListWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox
)
from PyQt5.QtCore import Qt

class MovieBookmarkApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Bookmark Manager")
        self.setGeometry(100, 100, 600, 400)

        self.movies = []

        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Input fields
        self.title_input = QLineEdit()
        self.genre_input = QComboBox()
        self.genre_input.addItems(["Action", "Comedy", "Drama", "Horror", "Sci-Fi"])
        self.rating_input = QSpinBox()
        self.rating_input.setRange(1, 10)
        self.favorite_checkbox = QCheckBox("Favorite")

        # Buttons
        add_button = QPushButton("Add Movie")
        add_button.clicked.connect(self.add_movie)

        # Movie list
        self.movie_list = QListWidget()

        # Layouts
        form_layout = QGridLayout()
        form_layout.addWidget(QLabel("Title:"), 0, 0)
        form_layout.addWidget(self.title_input, 0, 1)
        form_layout.addWidget(QLabel("Genre:"), 1, 0)
        form_layout.addWidget(self.genre_input, 1, 1)
        form_layout.addWidget(QLabel("Rating:"), 2, 0)
        form_layout.addWidget(self.rating_input, 2, 1)
        form_layout.addWidget(self.favorite_checkbox, 3, 1)
        form_layout.addWidget(add_button, 4, 1)

        # NIM and Name display
        student_label = QLabel("NIM: F1D022052 - Name: Ida Bagus Brahmanta Jayana")
        student_label.setStyleSheet("font-weight: bold; color: white")
        student_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(QLabel("Movie List:"))
        layout.addWidget(self.movie_list)
        layout.addWidget(student_label)

        main_widget.setLayout(layout)

    def add_movie(self):
        title = self.title_input.text().strip()
        genre = self.genre_input.currentText()
        rating = self.rating_input.value()
        favorite = self.favorite_checkbox.isChecked()

        if not title:
            QMessageBox.warning(self, "Input Error", "Movie title cannot be empty.")
            return

        movie_str = f"{title} ({genre}) - Rating: {rating}{' ★' if favorite else ''}"
        self.movie_list.addItem(movie_str)
        self.title_input.clear()
        self.favorite_checkbox.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieBookmarkApp()
    window.show()
    sys.exit(app.exec_()) 