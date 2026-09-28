\newpage

# Richtext Definition

In einigen Anwendungsfällen im Rahmen der politschen Geschäfte werden Texte strukturiert übermittelt. In diesem Falle enthalten die Texte verschiedene Formatierungselemente welche repräsentiert werden sollen. Im Grundsatz werden Formatierungen mit HTML Elemente ausgedrückt. Es sollen aber nicht alle Möglichkeiten von HTML erlaubt werden, sondern nur solche welche grundsätzliche Formatierungen erlauben. Schriftart, -grösse und farbe sind Grundsätzlich nicht erlaubt um Inkompatibilitäten zu vermeiden.

Dieses Kapitel zeigt auf welche Elemente von HTML in diesen sogenannten "Richtext" Feldern erlaubt sind.

## Erlaubte Codepages
Im Grundsatz wird in allen Standards dieser eCH Gruppe nur Unicode erlaubt.

## Auflistung der erlaubten und nicht erlau


| Zweck        | Element                                         | HTML                                                              | Bemerkung                                                                                                                            |
| ------------ | ----------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Gliederung   | Paragraph                                       | `<p>`                                                            | CSS-Styles, Klassen und in-line Definitionen sind nicht erlaubt.                                                                     |
| Gliederung   | Titel                                           | `<h2>`–`<h4>`                                                   | Nur `<h2>`, `<h3>` und `<h4>` sind erlaubt. H1 wird meist als eigenes Titeldatenfeld mitgeliefert.                                |
| Elemente     | Tabelle Kopf Inhalt                             | `<table>` `<thead>` `<tbody>` `<tr>` `<td>`                  | Styles sind auch in Tabellen nicht erlaubt. Ein angehängtes `<figure>` ist erlaubt.                                                 |
| Elemente     | Bild                                            | `<img>`                                                          | Bilder in einem Text müssen inline mit BASE64 geliefert werden. Externe Links sind nicht erlaubt.                                    |
| Elemente     | Links                                           | `<a href>`                                                       | Keine Einschränkungen; es muss darauf geachtet werden, dass es sich um öffentlich zugängliche und langfristig stabile Links handelt. |
| Elemente     | Geordnete Liste / Ungeordnete Liste             | `<ol>` `<ul>` `<li>`                                           | Die Attribute `list-style-types` und `start` sind erlaubt.                                                                           |
| Formatierung | Kursiv / Fett / Unterstrichen / Durchgestrichen | `<i>` `<em>` `<b>` `<strong>` `<u>` `<s>` `<sub>` `<sup>` | Alle Elemente sind erlaubt. `<em>` und `<strong>` werden `<i>` und `<b>` vorgezogen, da sie semantisch statt typografisch sind.  |
| Formatierung | Allgemein                                       | —                                                                 | CSS-Styles, Klassen und Inline-Definitionen sind nicht erlaubt.                                                                      |
| Formatierung | Schriftgrösse                                   | `<span style="font-size: 18px;">`                                | Nicht erlaubt.                                                                                                                       |
| Formatierung | Schriftfarbe                                    | `<mark class=*>` `<span style="color: rgb(184, 49, 47);">`      | Nicht erlaubt.                                                                                                                       |
| Formatierung | Schriftart                                      | `<span style="font-family: Impact, Charcoal, sans-serif;">`      | Nicht erlaubt.                                                                                                                       |
| Formatierung | Einrücken                                       | `<p style="margin-left: 20px">`                                  | Nicht erlaubt.                                                                                                                       |
| Formatierung | Ausrichtung                                     | `<p style="text-align: center;">`                                | Nicht erlaubt.                                                                                                                       |
