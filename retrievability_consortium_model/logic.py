from retrievability_consortium_model.types import ModelParams, ModelState
from cadCAD_tools.types import VariableUpdate

def s_days_passed(params: ModelParams,
                  _2,
                  _3,
                  state: ModelState,
                  _5) -> VariableUpdate:
    value = state['days_passed'] + params['days_per_timestep']
    return ('days_passed', value)

