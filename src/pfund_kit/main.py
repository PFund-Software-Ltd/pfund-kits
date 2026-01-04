import atexit

from pfund_kit.cli import pfund_cli_group


def exit_cli():
    """Application Exitpoint."""
    print("Cleanup actions here...")


def run_cli() -> None:
    """Application Entrypoint."""
    # atexit.register(exit_cli)
    pfund_cli_group(obj={})


if __name__ == '__main__':
    run_cli()