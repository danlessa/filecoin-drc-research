from retrievability_consortium_model.logic import *

timestep_block: list[dict] = [
    {
        'label': 'Time Tracking',
        'policies': {

        },
        'variables': {
            'days_passed': s_days_passed
        }
    }
]

timestep_block = [block
                  for block in timestep_block
                  if block.get('ignore', False) is not True]
