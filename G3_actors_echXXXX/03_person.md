# Person

## Meeting 22.05.2025

* Möglichst übernahme von eCH44 bezüglich Identifikation.

* Amtlicher Name genügend? -> oft ist der Rufname, wie damit umgehen?
* Undefined Name Type als Option?
* Aliase ? -> mit Geburtsdatum
* offizieler Name (eindeutig in der Zeit, für apel)

### Namenstypen basierend nach eCH11


Person1 {
usedFirstName: "Michael",
usedLastName: "Luggen",
otherNames: 
[
  { nameType: nameOnForeignPassport , 
  firstname: "Michéle",
  lastname: "Luca",
  fullName "Michael Luggen"},
  { nameType: Rufname, 
  fullName "luggi",
  },
]
}

Amtlich * Label typ
  vorname
  nachname
  fullName

Amtlicher Name (präferenziert, optional) – officialName, siehe Kapitel 3.3.2.1   (TODO: Bestimmen ab wann wird ein Namenswechsel ausgewiesen?)
Amtliche Vornamen (präferenziert, optional) – firstName, siehe Kapitel 3.3.2.2

Ledigname (optional) – originalName, siehe Kapitel 3.3.2.3 (Use-Case: Kann helfen über Zeit Rückverfolgung zu erlauben.)
Allianzname (optional) – allianceName, siehe Kapitel 3.3.2.4 (Use-Case: Kann helfen über Zeit Rückverfolgung zu erlauben.)

Aliasname (optional) – aliasName, siehe Kapitel 3.3.2.5  (Brauch im ech11 eine Definition.)
Andere amtliche Name (optional) – otherName, siehe Kapitel 3.3.2.6 (Brauch im ech11 eine Definition.)

Rufname (optional) – callName, siehe Kapitel 3.3.2.7
  Name im ausländischen Pass (optional) - nameOnForeignPassport, siehe Kapitel 3.3.2.8
oder
  Name gemäss Deklaration (optional) – declaredForeignName, siehe Kapitel 3.3.2.9



  # Use Case

  -> UseCase 1: 
