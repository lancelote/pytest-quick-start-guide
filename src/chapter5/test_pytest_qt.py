from PyQt5 import QtCore


class MainWindow:
    def __init__(self):
        self.about_button = None
        self.about_box = None


def test_main_window(qtbot):
    widget = MainWindow()
    qtbot.add_widget(widget)
    qtbot.mouseClick(widget.about_button, QtCore.Qt.LeftButton)
    qtbot.waitUntil(widget.about_box.isVisible)
    assert widget.about_button.text() == 'This is a GUI App'
