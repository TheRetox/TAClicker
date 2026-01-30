# 🚀 Playwright Button Monitor

Ein automatisiertes Tool zur Überwachung von Webseiten-Buttons (z. B. Anwesenheits-Checks) innerhalb von Iframes. Das Skript nutzt **Playwright** für die Automatisierung, **Typer** für die CLI-Steuerung und **Rich** für ein schönes Terminal-Interface.

## 📋 Features

- **Manueller Login-Support:** Das Skript wartet geduldig, bis du dich eingeloggt hast.
- **Iframe-Erkennung:** Findet Buttons auch in tief verschachtelten Strukturen (wie Jitsi).
- **Echtzeit-Monitoring:** Zyklische Statusmeldungen mit Zeitstempel im Terminal.
- **Multi-Browser:** Unterstützung für Chromium, Firefox und Webkit.

## 📋 Voraussetzungen

Bevor du startest, müssen **Python**, **pip** und **git** auf deinem System installiert sein.

### 1. Installation der Tools

- **Git:**
  - **Windows:** Lade [git-scm.com](https://git-scm.com/download/win) herunter und installiere es.
  - **macOS:** `brew install git` oder installiere die Xcode Command Line Tools.
  - **Linux:** `sudo apt install git`
- **Python & pip:**
  - **Windows:** Lade den Installer von [python.org](https://www.python.org/downloads/) herunter.
    **WICHTIG:** Aktiviere im Installer unbedingt den Haken bei **"Add Python to PATH"**. (Pip wird automatisch mitinstalliert).
  - **macOS:** `brew install python`
  - **Linux:** `sudo apt install python3 python3-pip`

### 2. Installation prüfen

Öffne ein Terminal (CMD, PowerShell oder Bash) und teste die Befehle:

```bash
git --version
python --version
pip --version
```

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

## 🔁 Wiederholte Nutzung (nach Neustart)

Wenn du den PC neu gestartet hast oder ein neues Terminal öffnest, musst du die Umgebung nicht neu installieren, sondern nur kurz **reaktivieren**:

1. **Navigiere in den Ordner:**

```bash
cd DEIN_REPO_NAME
```

2. **Aktiviere die Umgebung:**

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Starte das Skript:

```bash
python main.py
```

[TIPP] Du erkennst die aktive virtuelle Umgebung daran, dass am Anfang deiner Eingabezeile im Terminal (.venv) steht.

```

```
