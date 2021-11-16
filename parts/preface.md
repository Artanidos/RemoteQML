#Einleitung
##Copyright
**Erstelle native WebApplikationen mit QML und Python**  
von Adam Art Ananda  
(C) Copyright 2021 Adam Art Ananda. All rights reserved.
##Motivation

Nach dem ich bereits seit über 30 Jahren Software entwickle, kam ich von C, Assembler, Clipper, Powerbuilder, Java, C#, Objetive-C, C++ zu Python. Und rate mal...   
**I liebe Python**   
Es wäre einfach für mich native Applikationen in Java, C++ oder Objective-C zu schreiben und ausserdem wäre ich ich in der Lage, Kotlin, Dart oder Swift zu lernen, aber die Dinge sind einfacher, wenn man sie mit Python programmiert.  
Ich habe mal ein Django Tutorial gemacht, Django ist ein Web-Framework für Python, und dabei hat mich fasziniert, wie einfach es ist, Daten-Modelle zu entwickeln. Einfach eine simple Datenklasse schreiben, ein Scaffolding job starten und schwups werden alle nötigen Tabellen auf dem SQL-Server für dich angelegt. Dann nur noch eben den Python-Interpreter starten, das Modell importieren, eine Instanz erstellen, sie mit Daten füllen und die Save-Methode aufrufen und schon wird das Ganze auf den SQL-Server geschrieben.  
Ich musste nicht eine Zeile SQL-Code schreiben. Python hatte mich eingefangen :-)  
Dann habe ich noch etwas über Generators, Comprehensions und Meta-Programmierung erfahren und Python hatte mich komplett überzeugt.  

Wo wir grad dabei sind...um dieses Buch schreiben zu können, habe ich eine Applikation geschrieben, die ich EbookCreator genannt habe. Diese Anwendung nutz auch PyQt5, QtWidgets und QML nutze ich, um Daten zu serialisieren. Diese App ist Open Source und du kannst sie benutzen, um dich inspirieren zu lassen. Du findest den <a href="https://github.com/Artanidos/EbookCreator/">Source Code</a> auf github.com.

Bevor ich mein erstes Buch über Python GUI geschrieben habe, habe ich ein Video mit "Uncle" Bob Martin über das Programmieren in der Zukunft gesehen. Er sagt, das sich alle 5 Jahre die Zahl der Softwareentwickler verdoppelt. Das bedeutet, das um die 50% aller Entwickler unerfahren sind.
Er sagte auch, das die erfahrenen Entwickler dafür verantwortlich sind, wenn z.B. ein selbst fahrendes Auto einen Menschen umfährt und tötet, nur weil ein Softwarefehler vorlag. Als ich das Heute gehörte habe, habe ich mich entschlossen andere Entwickler auszubilden und habe mit diesem Buch begonnen. 

##Warum RemoteQML
Du bist sicherlich auch schon öfters auf Webseiten gestoßen, die versuchen eine App darzustellen oder du hast dir eine App für dein Smartphone runtergeladen und mußtest feststellen, das dies gar keine native App ist, sondern einfach nur eine Webseite rendert.  
Die Art von WebApps sind zwar immer auf dem neusten Stand und alle Nutzer arbeiten mit der selben Version, aber zum einen sind diese Apps einfach langsam, da bei jedem Klick auf einen Button ein RoundTrip zum Server gemacht wird um den aktuellen Status der App runterzuladen und zum anderen sind diese Apps einfach nicht wirklich benutzerfreundlich.  

##Für Wen Ist Dieses Buch
Wenn du in der Lage bist, einfache Programme in Python zu schreiben und interessiert bist Anwendungen mit einem grafischem Benutzer-Interface für Android zu schreiben, dann ist dieses Buch genau das richtige für dich.  
Du musst dich nicht unbedingt mit Qt auskennen.  
Wenn du willst, probiere alle Beispiele aus diesem Buch selber aus. Von Vorteil wäre es, wenn du auch, wie ich, auf Linux arbeitest. Die Beispiele sollten aber auch mühelos auf MacOS und Windows laufen. Lediglich für die Installation der benötigten Software solltest du dich selber im Internet einlesen, da ich nur die nötigen Schritte für Linux erkläre.  

##Für Wen Ist Dieses Buch Nicht

Solltest du noch ein Anfänger in Python sein, dann schlage ich dir vor, erst einmal einen geeigneten Grundkurs für Python zu machen, bevor du in diesem Buch weiterliest. Es gibt hierfür tolle Bücher und eine Menge Videos auf Youtube.  
In diesem Buch gehe ich nicht in Python spezifische Details ein.

##Wie Dieses Buch Organisiert Ist

Hier findest du die Übersicht über die Teile dieses Buches.  
Zuerst werden wir in ***Teil I*** alle nötigen Werkzeuge zum Erstellen der Software mit PyQt5 und Python installieren.  
In ***Teil II*** lernst du etwas über die verschiedenen Ansätze um Anwendungen zu bauen.  
In ***Teil III*** lernst du Anwendungen mit Python und QML zu schreiben.  
TODO  


##Konventionen In Diesem Buch

In diesem Buch nutze ich folgende typografischen Konventionen. 

*Kursiv*
<blockquote>
<p>Wird benutzt, um Dateinamen und Pfade zu markieren</p>  
</blockquote>

```
Feste Schriftbreite
```

<blockquote>
<p>Wird für Programm-Beispiele benutzt</p>  
</blockquote>

##Beipiel Source Code Benutzen

Die gesamten [Beispiele](https://github.com/Artanidos/RemoteQMLBook/) sind auf github.com verfügbar.

##Wie Du Mich Kontaktieren Kannst

Solltest du eine Frage oder ein Kommentar zu diesem Buch haben, scheue dich nicht, mir eine Email zu schreiben. Sende deine Fragen und Kommentare einfach an: japp.olaf@gmail.com

##Danksagungen
Zu allererst bin ich meinem Körper dankbar, weil er mich zur richtigen Zeit auf die richtigen Wege geführt hat. Ich weiß, das klingt bestimmt ein bisschen verrückt, aber da ich Maschinenschlosser gelernt habe und bereits nach wenigen Jahren, Rückenschwerzen bekam und über ein halbes Jahr krank war, habe ich angefangen Maschinenbau zu studieren und während des Studiums habe ich dann mit dem Programmieren angefangen. Zu der Zeit habe ich mich entschieden, mein Studium abzubrechen und als Softwareentwickler zu arbeiten.  
Dann hat mir mein Körper vor 5 Jahren mit gleich zwei Burnouts zu verstehen gegeben, mich aus dem Arbeitsleben zurückzuziehen.  
Nun habe ich viel Zeit, um Open Source Software zu schreiben und neue Dinge auszuprobieren, wie zum Beispiel Bücher wie dieses hier zu schreiben.
 
Ich bin Guido Rossum dankbar, weil es 1991 Python erfunden und veröffentlicht hat.

Und ausserdem bin ich allen Pythonistas da draussen dankbar, weil sie so tolle Tutorials und Videos gemacht haben, damit ich Python lernen konnte.