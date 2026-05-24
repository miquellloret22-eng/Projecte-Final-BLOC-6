# Projecte-Final-BLOC-6 - Django

## Introducció
Aquest projecte consisteix en el desenvolupament d’un blog web amb Django, aplicant conceptes de programació orientada a objectes, bases de dades i desenvolupament web dinàmic. L’aplicació permet gestionar posts, autors i etiquetes mitjançant diferents rutes, vistes i plantilles HTML.

El blog inclou funcionalitats com la pàgina principal amb els darrers posts, el llistat complet de publicacions, el detall de cada post, pàgines d’autors i tags, així com una plantilla d’error 404. També s’han implementat relacions entre models (One-to-Many i Many-to-Many), ús de dades dinàmiques des de la base de dades, càrrega de fixtures i estilització amb CSS o Bootstrap.

L’objectiu principal és crear una aplicació funcional i estructurada seguint les bones pràctiques de desenvolupament amb Python i Django.

## Instal·lació

### Clonar el repositori
```bash
git clone https://github.com/miquellloret22-eng/Projecte-Final-BLOC-6.git
cd Projecte-Final-BLOC-6
```

### Crear entorn virtual
```bash
python -m venv venv
```
Activar-lo:
Linux/Mac:
```bash
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```

### Instal·lar dependències
```bash
pip install -r requirements.txt
```

### Executar migracions
```bash
python manage.py migrate
```

## Execució del projecte

### Executar el servidor
```bash
python manage.py runserver
```

### Accedir al projecte
Obrir el navegador a:
```bash
http://127.0.0.1:8000
```

## Documentació
Obrir el navegador a:
```bash
https://miquellloret22-eng.github.io/Projecte-Final-BLOC-6/
```