from invisible_flow.transformers.complainant_transformer import ComplainantTransformer
from invisible_flow.transformers.transformer_base import TransformerBase
from invisible_flow.transformers import CaseInfoAllegationsTransformer, InvestigatorTransformer
from invisible_flow.transformers.victim_transformer import VictimTransformer


class TransformerFactory:

    @staticmethod
    def get_transformer(response_type) -> TransformerBase:
        if response_type == 'case_info':
            return CaseInfoAllegationsTransformer()
        elif response_type == 'investigators':
            return InvestigatorTransformer()
        elif response_type == 'complainant':
            return ComplainantTransformer()
        elif response_type == 'victim':
            return VictimTransformer()
        else:
            raise Exception('Unable to handle this type of file')
