from cadCAD_tools.execution import easy_run
from datetime import datetime
import click

from retrievability_consortium_model.initial_state import initial_state
from retrievability_consortium_model.params import params
from retrievability_consortium_model.structure import timestep_block
from retrievability_consortium_model.sim_config import TIMESTEPS, SAMPLES


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
