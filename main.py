import re
import typer
import time
from datetime import datetime
from playwright.sync_api import sync_playwright
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text

app = typer.Typer()
console = Console()

def get_timestamp():
    return f"[bold cyan][{datetime.now().strftime('%H:%M:%S')}][/bold cyan]"

def log_message(message: str, style: str = "green"):
    console.print(f"{get_timestamp()} {message}", style=style)

@app.command()
def start_monitor(
    browser_type: str = typer.Option("chromium", help="Browser: chromium, firefox oder webkit")
):
    
    console.print(Panel.fit("🚀 Button Monitor gestartet", style="bold magenta"))

    with sync_playwright() as p:
    
        if browser_type == "firefox":
            browser_engine = p.firefox
        elif browser_type == "webkit":
            browser_engine = p.webkit
        else:
            browser_engine = p.chromium

        log_message(f"Starte {browser_type}...", "yellow")
        
        browser = browser_engine.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        
        page.goto("https://campus.ta.de/login")

        log_message("Warten auf manuellen Login durch den Benutzer...", "bold yellow")
        
        
        try:
            login_check = page.get_by_role("button", name=re.compile(r"Ansicht", re.IGNORECASE))
            login_check.wait_for(state="visible", timeout=0)
            log_message("Login erfolgreich erkannt!", "bold green")
            log_message("BITTE JETZT ZUM KURS NAVIGIEREN", "blink bold red")
        except Exception as e:
            log_message(f"Fehler beim Warten auf Login: {e}", "red")
            return
        
        log_message("Prüfe, ob du dich auf der Kurs-Seite befindest...", "yellow")
        
        while True:
            jitsi_locator = page.locator("#jitsiConferenceFrame0")
            if jitsi_locator.count() > 0:
                log_message("Du befindest dich nun auf der richtigen Seite.", "bold green")
                break
            time.sleep(2)

        
        log_message("Skript überwacht jetzt den Browser.", "bold blue")
        
        start_time = time.time()
        last_heartbeat = time.time()

        try:
            while True:
            
                btn_anwesend = page.get_by_role("button", name="Ich bin anwesend")

                if btn_anwesend.is_visible():
                    log_message("Bestätigungs-Button erkannt!", "bold green")
                    btn_anwesend.click()
                    break
                
            
                if time.time() - last_heartbeat > 10:
                    current_duration = int(time.time() - start_time)
                    log_message(f"Status: Überwachung läuft... (seit {current_duration}s aktiv)", "dim white")
                    last_heartbeat = time.time()
                
                time.sleep(0.5)

        except KeyboardInterrupt:
            log_message("Überwachung durch Benutzer abgebrochen.", "yellow")
        finally:
            log_message("Beende Browser...", "yellow")
            browser.close()

if __name__ == "__main__":
    app()