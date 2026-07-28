from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTreeView)

from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QFont
)


def main():
    app = QApplication([])
    font = QFont()

    window = QMainWindow()
    tree = QTreeView()
    model = QStandardItemModel()
    root = model.invisibleRootItem()

    model.setHorizontalHeaderLabels(["Project"])
    tree.setModel(model)
    window.setCentralWidget(tree)

    project = QStandardItem("Project")
    sub1 = QStandardItem("Sub1")
    sub2 = QStandardItem("Sub2")

    class1 = QStandardItem("Class1")
    class2 = QStandardItem("Class2")
    class3 = QStandardItem("Class3")

    root.appendRow(project)
    project.appendRow(sub1)
    project.appendRow(sub2)
    sub1.appendRow(class1)
    sub1.appendRow(class2)
    sub2.appendRow(class3)

    font.setPointSize(14)
    app.setFont(font)

    window.resize(1200, 800)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
