# 🛍️ ForceFashion

**ForceFashion** ist eine moderne E-Commerce-Webanwendung für Modeartikel, entwickelt mit Django. Die Plattform ermöglicht es Nutzern, Produkte zu durchsuchen, in den Warenkorb zu legen und sicher zu bezahlen.

## 🚀 Features

- Benutzerregistrierung & Anmeldung
- Produktkatalog mit Bildern und Preisen
- Warenkorb-Funktionalität
- Sichere Checkout-Prozesse
- Admin-Panel zur Verwaltung von Produkten & Bestellungen

## 🛠️ Installation

1. **Repository klonen:**
   ```sh
   git clone https://github.com/Seymakarakurt/ForceFashion.git
   cd ForceFashion
   ```

2. **Virtuelle Umgebung erstellen & aktivieren:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Abhängigkeiten installieren:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Datenbankmigrationen durchführen:**
   ```sh
   python manage.py migrate
   ```

5. **Superuser erstellen (für Admin-Panel):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Entwicklungsserver starten:**
   ```sh
   python manage.py runserver
   ```

Nun ist die Anwendung unter `http://127.0.0.1:8000/` erreichbar.

## 📁 Projektstruktur

```
ForceFashion/
│── bag/          # Warenkorb-App
│── checkout/     # Checkout & Zahlung
│── core/         # Zentrale Konfiguration
│── products/     # Produktverwaltung
│── profiles/     # Benutzerprofile
│── static/       # Statische Dateien (CSS, JS, Bilder)
│── templates/    # HTML-Templates
│── db.sqlite3    # SQLite-Datenbank (lokal)
│── manage.py     # Django-Management-Skript
│── requirements.txt  # Abhängigkeiten
```

## 🔧 Konfiguration

Falls Umgebungsvariablen benötigt werden (z.B. für Zahlungsanbieter oder E-Mail-Versand), können sie in einer `.env`-Datei gespeichert werden:

```
SECRET_KEY=dein_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## 📜 Lizenz

Dieses Projekt ist unter der **MIT-Lizenz** veröffentlicht.

---

💡 Entwickelt mit ❤️ von [Seymakarakurt](https://github.com/Seymakarakurt)
