# SPARQL Abfragen auf Fedlex
Adapted from [Fedlex Linked Data Tutorial](https://swissfederalarchives.github.io/LD-Tutorials/lab/). 

## Tutorial

Einfache SPARQL-Abfragen funktionieren  ganz ohne Installation (siehe Tutorial)[TUTORIAL.md]. Die Samples der Schweizerischen Bundeskanzlei sind für Testingzwecke als `.sparqlbook` im Ordner `/sparl-tutorial` gespeichert,

## Samples

Die Originaldatei der Schweizerischen Bundeskanzlei mit Beispielen ist unter `fedlex_WIP.ipynb` gespeichert und lässt sich in Jupyter Lab anzeigen. `version_link.ipynb` enthält ein Tutorial zu **version.link Schema** und dem Anwendungsfall des historisierten Gemeindeverzeichnisses. 

## Documentation

Die UTI Patterns und weitere Informationen zum Gesetzgebungsprozess sind im Ordner `doc`abgespeichert.

## Git setup

- Create new directory
- Clone repo to local directory `git clone https://github.com/mgajdo/spraql.git`
- cd into repo `cd ` to new directory

### Install

## Python setup (SPARQL Tutorial)

- Install Python and pip (install dependencies if the project is cloned) `python3 -m pip install --upgrade pip`. [Installation advice](https://packaging.python.org/en/latest/tutorials/managing-dependencies/) for Python projects.
- Initialize a Virtual Environment: `python -m venv myenv`. The dependencies will be installed in the /myenv directory
- Activate environment: `source myenv/bin/activate`
- Install the Requests and Pandas library `pip install requests pandas`. [Documentation](https://pandas.pydata.org/docs/index.html)

You should now be able to run SPARQL queries in the `fedlex/tutorial` directory without further dependencies.


## Usage (`fedlex` directory)

The [`fedlex` directory](fedlex/README.md) contains all sample queries to Fedlex and a tutorial. **Tutorial notebooks** for sample code and patterns are inside the `examples` directory


Run the `.ipynb` files in the browser: