from cadCAD_tools.preparation import prepare_params
from cadCAD_tools.types import ParamSweep, Param

from retrievability_consortium_model.types import ModelSweepParams


raw_params = ModelSweepParams(

)

params = prepare_params(raw_params, cartesian_sweep=True)
