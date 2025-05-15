# mainWinClass
## 소스코드 설명 

1. mainWindow 만들기   
2. Class 단위로 만들기   
3. 몇개의 Class로 만들어진 APP   
   
pyQTapp01.py
```
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("dialog.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
```
