# Teil II - QML

## QML Syntax
Die QML Syntax wurde entwickelt, um Benutzerinterfaces mit einer leicht les- und leicht schreibbaren Syntax, basierend auf Ideen von XAML, Json und Javascript zu nutzen.
QML kombiniert alle drei Sprachen in einer.

Das Benutzerinterface wird in QML als Hierarchie deklariert. Jedes Element wird innerhalb eines anderen positioniert. Ereignisse, die von einem Control getriggert werden, wenn der Benutzer zum Beispiel einen Button klickt, können in Javascript kodiert werden.

Um einen Element zu deklarieren, schreiben wir den Namen des Elementes gefolgt von geschweiften Klammern, ähnlich wie in Javascript.

```qml
Rectangle 
{ 
}
```

Um den Wert einer Eigenschaft zu deklarieren, schreiben wir den Namen der Eigenschaft gefolgt von einem Doppelpunkt und dem Wert.  
```qml
name: value
```
Um einen numerischen Wert zu deklarieren, schreiben wir den numerischen Wert einfach hinter den Doppelpunkt.  
```qml
width: 200
```
Einen Text schreiben wir in Anführungszeichen **"** oder **'**.  
```qml
text: "The quick brown fox"
message: 'Hello "Brother"'
```
Farben werden genau so zwischen Anführungszeichen gesetzt und mit dem Hash "#" Zeichen gestartet.  
```qml
color: "#FF00FF"
```
Hier im Beispiel wurde der Rot-Anteil auf hexadezimal FF (255) gesetzt, der Grün-Anteil ist auf 0 und der Blau-Anteil auch auf FE (254). Man spricht hier auch von RGB. (Rot Grün Blau)

Du kannst die Opacity auch mit einem hexadezimalen Wert setzen. Einfach an das Ende des Farbstrings anhängen.  
```qml
color: "#FF00FEEE"
```
Hier im Beispiel wurde die Opacity auf den Wert EE (238) gesetzt.
0 bedeutet transparent und FF (255) voll sichtbar. 

### Die Id
Ein spezieller Wert in QML ist die **id**.   
```qml
ApplicationWindow 
{
    id: root
    Text 
    {
        text: "The parent is " + root.width + " pixels wide"
    }
}
```
Die **id** is schreibgeschütz und wird einmalig in der Deklaration gesetzt. Sie wird benutzt, um items zu referenzieren. Eine gute Praxis is es, das oberste Element in der Hierarchie mit **root** zu benennen, so das es in allen QML-Objekten gleich heisst.  

Kind-Elemente erben das Koordinatensystem vom Vater-Element (parent), dem übergeordnetem Element. Somit sind die x und y Koordinaten immer relativ zum Vater (parent).

Jedes QML-Objekt benötigt genau ein Wurzel-Element (root). Somit kann es zum Beispiel nur ein einziges ApplicationWindow geben.    

### Kind Elemente
Jedes Element kann Kind-Elemente innerhalb der geschweiften Klammern deklarieren. Auf diese Weise kann ein ganzer Baum an hierarchisch angeordneten Elementen entstehen.  

```qml
Rectangle 
{
    color: "red"

    MouseArea
    {
        anchors.fill: parent
    }
}
```
Kind-Elemente können dann wiederum weitere Kind-Elemente enthalten.  

### Kommentare
Kommentare können mit **//** für eine Zeile oder mit **/* */** für mehrere Zeilen deklariert werden. Genau wie in C, C++ und Javascript.    

```qml
ApplicationWindow
{
    /* This
    ** is a
    ** comment.
    */
    visible: true

    // This is also a comment
}
```  

### Imports 
    import Namespace Major.Minor
    import Namespace Major.Minor as SingletonIdentifier
    import "directory"
    import "file.js" as ScriptIdentifier

Mit einer Import Deklaration werden QML-Objekte mit einer spezifischen Version dazugeladen.  

```qml
import QtQuick 2.5
```
Die Hauptversion deutet auf die QtQuick-Version hin.
Die Unterversion deutet auf die Qt-Version hin.  
Somit wird im obigen Beispiel QtQuick 2 und Qt mit der Version 5.* importiert.  
Die Version 2.12 importiert in diesem Fall QtQuick 2 und Qt 5.12.  

## Eigenschaften
Du kannst Eigenschaften mit dem Schlüsselwort **property**, gefolgt von dem Typ, dem Namen und optional mit einem Initialwert deklarieren.  
Die Syntax lautet ```property <type> <name> : <value>```  
```qml
property int clickCount: 0
```
Eine weitere Möglichkeit ist es das Schlüsselwort **alias** zu nutzen, um die Eigenschaft eines untergeordneten Objektes weiterzureichen.  
Die Syntax lautet ```property alias <name>: <reference>```
```qml
property alias text: lable.text
``` 
Eine alias Eigenschaft benötigt keinen Typ, da der Typ des referenzierten Objektes benutzt wird.  

## Basic Types
| Typ | Beschreibung |
|  :---     |   :---:     |
| bool | Binär Wahr/Falsch-Wert |
| double | Nummer mit Dezimalpunkt, gespeichert mit doppelter Genauigkeit |
| enumeration | Benannte Aufzahlung |
| int | Ganzzahl, e.g. 0, 11, or -22 |
| list | Liste von QML Objekten |
| real | Nummer mit Dezimalpunkt |
| string | Zeichenkette |
| url | Uniform Resource Locator |
| var | Generischer Typ |  

## Property Binding
Eines der wichtigsten Merkmale von QML ist die Eigenschaftsbindung. Ein Wert einer Eigenschaft kann über eine Konstante, einen Ausdruck oder über die Bindung an eine andere Eigenschaft festgelegt werden.

```qml
Rectangle 
{
    width: 200; height: 200

    Rectangle 
    {
        width: 100
        height: parent.height
        color: "red"
    }
}
```
Im obigen Fall wurde die Höhe an die Höhe des übergeordneten Objekts gebunden. Wenn wir die Höhe des Elternteils ändern, wird die Höhe des inneren Rechtecks automatisch angepasst.  

## Signals
### Empfangen von Signalen und Signalhandlern
Um eine Benachrichtigung zu erhalten, wenn ein Signal für ein Objekt ausgegeben wird, sollte die Objektdefinition einen Signalhandler mit dem Namen ```on<Signal>``` deklarieren, wobei Signal der Name des Signals ist und der erste Buchstabe groß geschrieben wird. Der Signalhandler sollte den JavaScript-Code enthalten, der ausgeführt werden soll, wenn der Signalhandler aufgerufen wird.  
```qml
    Button 
    {
        id: button
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Change color!"
        
        onClicked: 
        {
            root.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
        }
    }
```
Im obigen Fall hat der Button ein Signal mit dem Namen **clicked** und wir erstellen einen Signalhandler mit dem entsprechenden Namen **onClicked**.

### Signalhandler für Eigenschaftsänderungen
Ein Signal wird ausgegeben, wenn sich der Wert einer QML-Eigenschaft ändert. Diese Art von Signal ist ein Eigenschaftsänderungssignal, und Signalhandler für diese Signale werden in der Form ```on<PropertyName>Changed
``` geschrieben, wobei PropertyName der Name der Eigenschaft ist und der erste Buchstabe groß geschrieben wird.  
```qml
    Rectangle 
    {
        id: rect
        width: 100; height: 100
        color: "#C0C0C0"

        TapHandler 
        {
            onPressedChanged: console.log("pressed changed to ", pressed)
        }
    }
```
Zum Beispiel hat der TapHandler eines Rechtecks eine **pressed** Eigenschaft. Um eine Benachrichtigung zu erhalten, wenn sich diese Eigenschaft ändert, schreiben Sie einen Signalhandler mit dem Namen ```onPressedChanged
``` wie im obigen Beispiel.  

### Connections
In einigen Fällen möchten wir auf ein Signal außerhalb eines Objekts zugreifen. Daher verwenden wir den Connections-typ.  
```qml
    Button
    {
        id: button
    }

    Connections 
    {
        target: button
        onClicked: 
        {
            rect.color = Qt.rgba(Math.random(), Math.random(), Math.random(), 1);
        }
    }
```

### Attached signal handlers
Ein angeschlossener Signalhandler empfängt ein Signal von einem angeschlossenen Typ.  
```qml
ApplicationWindow
{
    Component.onCompleted: 
    {
        console.log("The windows title is", title)
    }
}
```
Im obigen Fall wird das Ereignis onCompleted ausgelöst, wenn das ApplicationWindow vollständig geladen wurde.   
 
### Signale für einen benutzerdefinierten QML-Typ 
Die Syntax zum Definieren eines neuen Signals lautet:
```signal <name>[([<type> <parameter name>[, ...]])]```

Ein Signal wird durch Aufrufen des Signals als Methode ausgegeben.  
```qml
// SquareButton.qml
import QtQuick 2.12

Rectangle 
{
    id: root
    signal activated(real xPosition, real yPosition)
    property point mouseXY
    property int side: 100
    width: side; height: side

    TapHandler 
    {
        id: handler
        onTapped: root.activated(mouseXY.x, mouseXY.y)
        onPressedChanged: mouseXY = handler.point.position
    }
}
```
Das Rechteckobjekt verfügt über ein aktiviertes Signal, das bei jedem Antippen des TapHandlers ausgegeben wird.

Um dieses Signal zu verwenden, deklarieren Sie einen onActivated-Handler im Code, der den SqareButton verwendet.  
```qml
    SqareButton
    {
        color: "#345462"
        x: 200
        y: 0
        onActivated: console.log("Activated at " + xPosition + "," + yPosition)
    }
```
##Funktionen
Um eine JavaScript-Funktion zu deklarieren, verwenden Sie die folgende Syntax.
```
function <name> ( <parameters> ) { ... }
```
Im nächsten Beispiel haben wir den Text mit der Id txt.
Im selben übergeordneten Element haben wir eine MouseArea, die nur zum Abrufen eines Klickereignisses verwendet wird, wenn der Benutzer mit der Maus darauf klickt oder wenn der Benutzer diesen Bereich auf einem Mobiltelefon berührt.  

```qml
property int clickCount: 0

Text 
{
    id: txt
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.verticalCenter: parent.verticalCenter
    text: "Right - Bottom "
}

MouseArea 
{
    anchors.fill: parent
    onClicked:  
    {
        increment()
        txt.text = "clicked " + clickCount + " times"
    }

    function increment()
    {
        clickCount++
    }
}
```
Die MouseArea hat ein clicked-Ereignis, das wir mit dem Präfix "on" codieren.
Wenn Sie mehr als eine Codezeile haben, müssen Sie Klammern verwenden.
In diesem Fall rufen wir die Funktion increment() auf.
Die Eigenschaft clickCount deklarieren wir auf oberster Ebene. Es ist eine gute Angewohnheit, alle Variablen oben im Stammelement zu deklarieren.  

##Interaktion zwischen QML und Python
Sie können fast alles in QML (Javascript) codieren, aber manchmal müssen Sie Geschäftslogik in Python ausführen. Deshalb werde ich Ihnen eine mögliche Brücke zeigen.
Wir erstellen eine von QObject abgeleitete Klasse und geben QML über die Kontexteigenschaft eine Instanz dieser Klasse.

```python
import sys
import os
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot


class Bridge(QObject):
    textChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._root = None
        self._cwd = os.getcwd()

    def setRoot(self, root):
        self._root = root

    @pyqtProperty(str, notify=textChanged)
    def cwd(self):
        return self._cwd

    @pyqtSlot("QString")
    def message(self, value):
        print(value + " from QML")
        self._root.updateMessage(value + " from Python")


if __name__ == "__main__":
    bridge = Bridge()
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("bridge", bridge)
    engine.load("view.qml")
    roots = engine.rootObjects()
    bridge.setRoot(roots[0])
    if not roots:
        sys.exit(-1)
    sys.exit(app.exec())
```

In QML können Sie die das bridge Objekt verwenden, um mit Python zu kommunizieren.  
```qml
import QtQuick 2.0
import QtQuick.Controls 2.5

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "QML Demo"

    function updateMessage(text)
    {
        txt.text = text
    }

    Text {
        id: txt
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        text: "cwd: " + bridge.cwd
    }
    MouseArea {
        anchors.fill: parent
        onClicked: 
        {
            bridge.message("click")
        }
    }
}
```
```bridge.cwd()
``` verwendet die in Python deklarierte Eigenschaft, um das aktuelle Arbeitsverzeichnis abzurufen.   
Und mit ```bridge.message()
``` senden wir Daten an den Slot in Python.  
Auf der Python-Seite können wir eine Javascript-Funktion mit dem Root-Objekt aufrufen.  
```python
self._root.updateMessage(value + " from Python")
```

## Bildschirmgrößen 
Um Elemente auf der Oberfläche zu platzieren, müssen wir sie positionieren.
Wenn du aus einer Windows-Umgebung wie WinForms kommst, weißt du, wie du Elemente anhand ihrer x- und y-Koordinaten positionierst.
Dies war in Ordnung für Fenster, bei denen die Bildschirmgröße in den letzten Jahren bekannt war.
Wir hatten nur Bildschirmgrößen wie 640 x 480 oder 1024 x 768. Hier hast du versucht, beim Entwerfen eines Dialogfelds die kleinste Bildschirmauflösung zu unterstützen.
Auf einem Mobiltelefon haben wir hunderte verschiedener Bildschirmauflösungen und Formfaktoren, daher müssen wir unsere Überlegungen zum Entwerfen eines Dialogs ändern.
Außerdem erstellen wir keine Dialoge mehr.
Normalerweise erstellen wir Vollbildseiten.

Wenn du auf einem Desktop-Computer entwickelst, und dort auch testen möchtest, musst du den Formfaktor eines Mobiltelefons simulieren.
Aufgrund der Tatsache, dass mein Mobiltelefon eine Auflösung von 700 * 1200 und mein Desktop eine Auflösung von 1366 * 768 hat, muss ich eine Bildschirmgröße finden, um den Porträtmodus meines Telefons auf meinem Desktop zu simulieren. Daher stelle ich das ApplicationWindow auf die Größe 350 * 600 ein, damit das Fenster auf meinen Bildschirm passt und den Porträtmodus eines Mobiltelefons nachahmt.

```qml
ApplicationWindow #
{
    id: applicationWindow
    width: 350
    height: 600
    visible: true
    title: "Anchors Demo"
```
Du solltest eine andere, aber ähnliche Lösung für deine Umgebung finden.

Wenn wir also die direkte Positionierung wie in Windows verwenden würden, in der wir die x- und y-Koordinaten zum Positionieren eines Elements verwendet haben, sollten wir eine andere Lösung für das Telefon verwenden, da wir die Bildschirmauflösung der Zielplattform nicht kennen. 
  
## Elemente positionieren
Um ein Element in QML zu positionieren, verwenden wir Anker.
Du kannst weiterhin die x- und y-Koordinaten verwenden, dies ist jedoch nur dann sinnvoll, wenn das Element oben links verankert ist.
Du kannst ein Element oben, unten, links und rechts verankern. Darüber hinaus kannst du ein Element auch im horizontalen Zentrum und im vertikalen Zentrum verankern.  

```qml
    Rectangle 
    {
        id: rectangle
        width: 100
        height: 100
        color: "#75507b"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }
```
Im obigen Beispiel ist die Mitte des Rechtecks an die Mitte des übergeordneten Elements gebunden, das das Anwendungsfenster ist, oder es könnte ein anderes Element sein.

Wenn du ein Objekt unten rechts verankern möchtest, positionierst du es wie folgt.  
```qml
    Rectangle
    {
        width: 100
        height: 100
        color: "#73d216"
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        anchors.right: parent.right
        anchors.rightMargin: 20
    }
```
Die Margin ist der Abstand zwischen dem Element und der Seite des Eltern-Elementes.

Im Quellcode dieses Buches findest du ein Beispiel mit allen Ankern unter *QtQuick/Anchors*.

## Controls
Das am häufigsten verwendete Steuerelement auf einem Mobiltelefon ist möglicherweise die Listbox.
Hier ist ein Beispiel, das zeigt, wie es mit einem statischen Modell verwendet wird.     
```qml
import QtQuick 2.0
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.1

ApplicationWindow 
{
    width: 640
    height: 480
    visible: true
    title: "QML Listview Demo"

    ListView 
    {
        clip: true
        anchors.fill: parent
        anchors.margins: 5
        spacing: 5
	    	
        delegate: listDelegate
        Component 
        {
            id: listDelegate
	    		
            RowLayout 
            {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.margins: 10
                spacing: 10

                CheckBox {}
                Label { text: itemType; color: "#888"; font.italic: true }
                Label { text: itemName; Layout.fillWidth: true }
                Label { text: itemPath }
                ComboBox { model: itemVersions; Layout.preferredWidth: 90 }
            }
        } 
	    	
        model: ListModel 
        {
            ListElement 
            {
                itemType: "asset"
                itemName: "First entry"
                itemPath: "/documents/fe.md"
                itemVersions: []
            }
            ListElement 
            {
                itemType: "asset"
                itemName: "Second entry"
                itemPath: "/documents/se.md"
                itemVersions: []
            }
            ListElement 
            {
                itemType: "asset"
                itemName: "Third entry"
                itemPath: "/documents/te.md"
                itemVersions: []
            }
        }
    }
}
```
Um die Liste zu rendern, entwerfen wir eine Komponente, die als Delegat verwendet wird.
Das Modell, das die Daten liefert, verwenden wir hier deklarativ.

Als nächstes werden wir ein in Python erstelltes Modell verwenden.  
```python
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import Qt, QObject, pyqtProperty, pyqtSignal, pyqtSlot, QAbstractListModel, QModelIndex


class Model(QAbstractListModel):
    def __init__(self, items, parent=None):
        super(Model, self).__init__(parent)
        self._items = items

    def rowCount(self, parent=None):
        return len(self._items)

    def data(self, index, role=None):
        role = role or QModelIndex()

        if role == Qt.UserRole + 0:
            return self._items[index.row()]["type"]

        if role == Qt.UserRole + 1:
            return self._items[index.row()]["name"]

        if role == Qt.UserRole + 2:
            return self._items[index.row()]["path"]

        if role == Qt.UserRole + 3:
            return self._items[index.row()]["versions"]

    def roleNames(self):
        return {
            Qt.UserRole + 0: b"itemType",
            Qt.UserRole + 1: b"itemName",
            Qt.UserRole + 2: b"itemPath",
            Qt.UserRole + 3: b"itemVersions",
        }


if __name__ == "__main__":
    items = [
        {
            "type": "asset",
            "name": "shapes",
            "path": "c:/users/Roy/Desktop/shapes.ma",
            "versions": ["v001", "v002", "v003"]
        },
        {
            "type": "asset",
            "name": "shapes1",
            "path": "c:/users/Roy/Desktop/shapes.ma",
            "versions": ["v001", "v002", "v003", "v004"]
        },
        {
            "type": "asset",
            "name": "shapes2",
            "path": "c:/users/Roy/Desktop/shapes.ma",
            "versions": ["v001", "v002", "v003"]
        },
    ]
    model = Model(items)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("mymodel", model)
    engine.load("view.qml")
    roots = engine.rootObjects()
    if not roots:
        sys.exit(-1)
    sys.exit(app.exec())
```
In der Ansicht müssen wir nur das Modell ändern. 
```qml
model: mymodel
```
Das Modellobjekt wurde jetzt als Kontexteigenschaft **mymodel** festgelegt.

Weitere Informationen finden Sie in den Qt-Dokumentationen und Beispielen. 
[All QML Types](https://doc.qt.io/qt-5/qmltypes.html)


## Zusammenfassung
Wir haben die Grundlagen von QML gesehen. Wir können jetzt einfache Apps mit QML und Python erstellen.