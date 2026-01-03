import click
from trogon import tui


@tui(command='tui', help="Open terminal UI")
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.pass_context
@click.version_option()
def pfund_cli_group(ctx):
    ctx.ensure_object(dict)
    # ctx.obj['config'] = get_config()
