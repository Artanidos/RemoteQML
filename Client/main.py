import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import qInstallMessageHandler, QtInfoMsg, QtWarningMsg, QtCriticalMsg, QtFatalMsg

def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))
    if mode == QtFatalMsg or mode == QtCriticalMsg:
        sys.exit("abort")


def object_created(object, url):
    if object:
        print("loaded")
        sys.exit(app.exec())
    else:
        print("App could not be loaded")
        sys.exit(-1)


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/Artanidos/RemoteQML/master/Basics/view.qml"
    qInstallMessageHandler(qt_message_handler)
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine(parent=app)
    engine.objectCreated.connect(object_created)
    engine.load(QUrl(url))