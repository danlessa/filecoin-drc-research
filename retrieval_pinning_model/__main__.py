from cadCAD_tools.execution import easy_run
from datetime import datetime
import click

from retrieval_pinning_model.model import timestep_block


default_run_args = (initial_state,
                    params,
                    timestep_block,
                    TIMESTEPS,
                    SAMPLES)


@click.command()
def main() -> None:
    df = easy_run(*default_run_args)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"data/simulation_output/{timestamp}.csv"
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    main()
