import click


@click.command()
@click.option("--github", is_flag=True, default=True, help="Show review requests for GitHub.")
@click.option("--gitlab", is_flag=True, default=True, help="Show review requests for GitLab.")
@click.option("--pagure", is_flag=True, default=True, help="Show review requests for Pagure.")
def day_starter(github: bool, gitlab: bool, pagure: bool):
    pass


if __name__ == "__main__":
    day_starter()
