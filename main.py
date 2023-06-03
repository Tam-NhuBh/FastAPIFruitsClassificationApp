import os

import click
import uvicorn


@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prod"], case_sensitive=False),
    default="local",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=False,
)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)
    uvicorn.run(
        app="app.server:app",
        host="127.0.0.1",
        port=8000,
        # reload=True if config.ENV != "production" else False,
        reload=True,
        workers=1,
    )


if __name__ == "__main__":
    main()
