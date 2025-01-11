from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from rich.prompt import Prompt, Confirm
from rich import box
from rich.text import Text
from rich.align import Align
from time import sleep
import json
import uuid
import os
from pathlib import Path
from datetime import datetime

console = Console()

def display_startup_banner():
    # ASCII Art for CursorReset
    cursor_reset_art = """
[bold cyan]
   ______                         ____                __ 
  / ____/_  ___________  _____   / __ \___  ________/ /_
 / /   / / / / ___/ __ \/ ___/  / /_/ / _ \/ ___/ __/ /
/ /___/ /_/ / /  / /_/ / /     / _, _/  __(__  ) /_/_/ 
\____/\__,_/_/   \____/_/     /_/ |_|\___/____/\__(_)  
[/bold cyan]
    """
    
    # Developer Info Panel
    dev_info = """[bold blue]Developer Information[/bold blue]
[yellow]Name:[/yellow] Adel Elawady
[yellow]Email:[/yellow] adel50ali50@gmail.com
[yellow]Project:[/yellow] Cursor Reset Tool
[yellow]Version:[/yellow] 1.0.0"""

    # Display the banner
    console.print(Align.center(cursor_reset_art))
    console.print(Align.center(Panel.fit(
        dev_info,
        border_style="cyan",
        padding=(1, 2),
        title="[bold cyan]About Developer[/bold cyan]"
    )))
    
    # Add a small delay for better visual effect
    sleep(1)

def generate_machine_id():
    """Generate a new machine ID using UUID4 and convert to hex format."""
    return uuid.uuid4().hex + uuid.uuid4().hex[:32]

def generate_uuid():
    """Generate a simple UUID4."""
    return str(uuid.uuid4())

class AppManager:
    def __init__(self):
        self.storage_path = Path(os.getenv('APPDATA') + "\\Cursor\\User\\globalStorage\\storage.json").resolve()

    def reset_app_ids(self):
        try:
            console.print(Panel.fit("[bold blue]Resetting App IDs[/bold blue]", border_style="yellow"))
            
            # Read the existing JSON file
            with open(self.storage_path, 'r') as file:
                data = json.load(file)
            
            # Backup the original file
            backup_path = self.storage_path.with_suffix('.json.backup')
            with open(backup_path, 'w') as backup_file:
                json.dump(data, backup_file, indent=4)
            
            # Update all telemetry and machine IDs
            data['telemetry.machineId'] = generate_machine_id()
            data['telemetry.macMachineId'] = generate_machine_id()
            data['telemetry.sqmId'] = generate_uuid()
            data['telemetry.devDeviceId'] = generate_uuid()
            
            # Show progress bar while processing
            for step in track(range(50), description="Resetting app IDs..."):
                sleep(0.02)
            
            # Write the modified data back to the file
            with open(self.storage_path, 'w') as file:
                json.dump(data, file, indent=4)
                
            console.print(Panel.fit(
                "[bold green]Successfully reset app IDs![/bold green]\n" +
                f"[yellow]A backup of the original file has been created at: {backup_path}[/yellow]",
                border_style="green"
            ))
            
        except FileNotFoundError:
            console.print(Panel.fit(
                f"[bold red]Error: Could not find the file at {self.storage_path}[/bold red]",
                border_style="red"
            ))
        except json.JSONDecodeError:
            console.print(Panel.fit(
                "[bold red]Error: The file contains invalid JSON data[/bold red]",
                border_style="red"
            ))
        except Exception as e:
            console.print(Panel.fit(
                f"[bold red]An unexpected error occurred: {str(e)}[/bold red]",
                border_style="red"
            ))

    def view_current_ids(self):
        try:
            with open(self.storage_path, 'r') as file:
                data = json.load(file)
            
            table = Table(show_header=True, header_style="bold magenta", box=box.DOUBLE_EDGE)
            table.add_column("ID Type", style="cyan")
            table.add_column("Value", style="yellow", overflow="fold")
            
            id_fields = [
                ('Machine ID', 'telemetry.machineId'),
                ('Mac Machine ID', 'telemetry.macMachineId'),
                ('SQM ID', 'telemetry.sqmId'),
                ('Device ID', 'telemetry.devDeviceId')
            ]
            
            for label, field in id_fields:
                if field in data:
                    table.add_row(label, data[field])
            
            console.print(Panel.fit(
                "[bold blue]Current App IDs[/bold blue]",
                border_style="blue"
            ))
            console.print(table)
            
        except Exception as e:
            console.print(Panel.fit(
                f"[bold red]Error viewing IDs: {str(e)}[/bold red]",
                border_style="red"
            ))

def main():
    app_manager = AppManager()
    
    while True:
        console.clear()
        display_startup_banner()  # Add the startup banner
        
        # Create options table
        table = Table(show_header=True, header_style="bold magenta", box=box.DOUBLE_EDGE)
        table.add_column("Option", style="cyan")
        table.add_column("Description", style="yellow")
        
        table.add_row("1", "Reset App IDs")
        table.add_row("2", "View Current IDs")
        table.add_row("3", "Exit")
        
        console.print(table)
        
        choice = Prompt.ask("\n[bold cyan]Enter your choice[/bold cyan]", choices=["1", "2", "3"])
        
        if choice == "1":
            if app_manager.storage_path.exists():
                if Confirm.ask("[bold yellow]Are you sure you want to reset all app IDs?[/bold yellow]"):
                     app_manager.reset_app_ids()
            else:
                console.print(Panel.fit(
                    "[bold red]Could not find storage.json in the expected location.[/bold red]\n" +
                    "[yellow]Please make sure Cursor is installed correctly.[/yellow]",
                    border_style="red"
                ))
        elif choice == "2":
            app_manager.view_current_ids()
        else:
            console.print(Panel.fit(
                "[bold blue]Thank you for using App ID Management System![/bold blue]",
                border_style="green"
            ))
            break
            
        if choice in ["1", "2"]:
            Prompt.ask("\n[bold cyan]Press Enter to continue[/bold cyan]")

if __name__ == "__main__":
    main() 