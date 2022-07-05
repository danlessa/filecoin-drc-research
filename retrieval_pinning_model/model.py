from cadCAD_tools.types import VariableUpdate
from math import exp
from cadCAD_tools.preparation import prepare_params
from typing import TypedDict
from dataclasses import dataclass
from numpy.random import binomial

Filecoin = float
Days = float


@dataclass
class Deal():
    created_at: Days
    payment: Filecoin
    duration: Days
    collateral: Filecoin
    finished: bool
    slashed: bool

    def deal_payoff(self,
                    slash_penalty: float) -> float:
        S = slash_penalty if self.slashed else 1.0

        if self.finished:
            if self.slashed:
                return (self.duration * self.collateral * self.finished * S / self.payment)
            else:
                return (self.duration * self.finished * S / self.payment)
        else:
            return 0.0


@dataclass
class Provider():
    created_at: Days
    deals: list[Deal]

    def reputation_payoff(self,
                          slash_penalty: float,
                          alpha: float) -> float:

        return sum(d.deal_payoff(slash_penalty) ** alpha
                   for d
                   in self.deals)


class ModelState(TypedDict):
    days_passed: Days
    providers: list[Provider]
    clients: int


class ModelParams(TypedDict):
    C_a_1: float
    C_a_2: float
    C_b: float
    C_c: float
    p_C: float
    mu_D: float
    sigma_D: float
    mu_D_tau: float
    sigma_D_tau: float


initial_state = ModelState(
    days_passed=0.0,
    providers=[],
    clients=0
)


def s_days_passed(params: ModelParams,
                  _2,
                  _3,
                  state: ModelState,
                  _5) -> VariableUpdate:
    value = state['days_passed'] + params['days_per_timestep']
    return ('days_passed', value)


def s_clients(params: ModelParams,
              _2,
              _3,
              state: ModelState,
              _5) -> VariableUpdate:

    N_c_max = params['C_a_1'] * (1 - exp(-params['C_a_2'] * state['days_passed']))
    N_c_max += params['C_b'] * state['days_passed']
    N_c_max += params['C.c']

    n = N_c_max - state['clients']
    p = params['p_C']

    round(binomial(n, p))

    return ('clients', None)


timestep_block: list[dict] = [
    {
        'label': 'Time Tracking',
        'policies': {

        },
        'variables': {
            'days_passed': s_days_passed
        }
    },
    {
        'label': 'Agent Arrival Processes',
        'policies': {

        },
        'variables': {
            'clients': s_clients,
            'providers': s_providers
        }
    },
    {
        'label': 'Deal Arrival Processes',
        'policies': {

        },
        'variables': {
            'deals': s_clients
        }
    }
]

timestep_block = [block
                  for block in timestep_block
                  if block.get('ignore', False) is not True]
