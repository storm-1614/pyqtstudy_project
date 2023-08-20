import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 最外层的垂直布局，包含两部分：爱好和性别
        container = QVBoxLayout()

        # ----创建第 1 个组，填加多个组件----
        # hobby 主要是保证它们是一个组
        hobby_box = QGroupBox("爱好")
        # v_layout 保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()
        btn1 = QRadioButton("抽烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("烫头")
        # 填加到 v_layout 中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 把 v_layout 填加到 hobby_box 中
        hobby_box.setLayout (v_layout)

        # ----创建第 2 个组，添加多个组件----
        # 性别组
        gender_box = QGroupBox("性别")
        # 性别容器
        h_layout = QHBoxLayout()
        # 性别选项
        bth4 = QRadioButton("男")
        bth5 = QRadioButton("女")
        # 追加到性别容器中
        h_layout.addWidget(bth4)
        h_layout.addWidget(bth5)
        # 填加到 box 中
        gender_box.setLayout(h_layout)

        # 把爱好的内容填加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        self.setLayout(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
