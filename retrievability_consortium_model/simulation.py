from dataclasses import dataclass
from random import random, randrange, choice




FIL: float


@dataclass
class Simulation():


    def provider_acceptance_criteria(self, payment: FIL) -> bool:
        pass



    def run(self):


        payment_proposal: FIL = random() * 100
        deal_is_accepted = self.provider_acceptance_criteria(payment_proposal)
        if deal_is_accepted:
            deal_epochs = randrange(100, 2000)
            for epoch in range(deal_epochs):
                client_tries_to_retrieve = choice([True, False])
                if client_tries_to_retrieve:
                    client_retrieves_file = choice([True, False])
                    if client_retrieves_file is False:
                        client_appeals = choice([True, False])
                        if client_appeals:
                            appeal_result_slash = None
                        if appeal_result_slash is True:
                            pass
                            break
                        else:
                            pass

            

