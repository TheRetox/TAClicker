# 🚀 Playwright Button Monitor

Ein automatisiertes Tool zur Überwachung von Webseiten-Buttons (z. B. Anwesenheits-Checks) innerhalb von Iframes. Das Skript nutzt **Playwright** für die Automatisierung, **Typer** für die CLI-Steuerung und **Rich** für ein schönes Terminal-Interface.

## 📋 Features

- **Manueller Login-Support:** Das Skript wartet geduldig, bis du dich eingeloggt hast.
- **Iframe-Erkennung:** Findet Buttons auch in tief verschachtelten Strukturen (wie Jitsi).
- **Echtzeit-Monitoring:** Zyklische Statusmeldungen mit Zeitstempel im Terminal.
- **Multi-Browser:** Unterstützung für Chromium, Firefox und Webkit.

## 🛠 Installation

Folge diesen Schritten, um das Skript auf deinem lokalen Rechner einzurichten:

1. **Repository klonen**

   ```bash
   git clone git@github.com:TheRetox/TAClicker.git
   cd TAClicker
   ```

2. **Virtuelle Umgebung erstellen**

   ```bash
   python -m venv .venv
   ```

3. **Virtuelle Umgebung aktivieren**
   - Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. **Abhängigkeiten installieren**

   ```bash
   pip install -r requirements.txt
   ```

5. **Playwright Browser-Engines installieren**

   ```bash
   playwright install
   ```

## 🚀 Nutzung

Starte das Skript mit dem Standard-Chromium-Browser:

```bash
python main.py
```

Optionale Parameter

Option Beschreibung Standardwert

```
--browser-type Wahl des Browsers (chromium, firefox, webkit) chromium
```

Beispiel mit Parametern:

```bash
python main.py --browser-type firefox
```
