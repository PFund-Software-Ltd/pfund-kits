import click
from rich.console import Console
from rich.table import Table


def display_help(command_groups: dict[str, click.Group]):
    """Display help with all available commands organized by group.

    Args:
        command_groups: Dictionary mapping group names to Click Group objects
    """
    console = Console()
    console.print("[bold]Available commands:[/bold]\n")

    # Iterate over command groups and display each in a table
    for group_name, group in command_groups.items():
        table = Table(
            title=f"[bold]{group_name} commands[/bold]",
            show_lines=True,
        )

        table.add_column("Command", justify="left", style="cyan", no_wrap=True)
        table.add_column("Description", justify="left", style="green")

        # Iterate over commands in the group
        for command_name, command_obj in group.commands.items():
            table.add_row(command_name, command_obj.help or "No description available")

        console.print(table)
        console.print()  # Add spacing between tables
