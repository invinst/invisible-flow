from invisible_flow.transformers import CaseInfoAllegationsTransformer
from invisible_flow.transformers.complainant_transformer import ComplainantTransformer
from invisible_flow.transformers.transformer_base import TransformerBase


class TransformerFactory:

    @staticmethod
    def get_transformer(response_type) -> TransformerBase:
        if response_type == 'case_info':
            return CaseInfoAllegationsTransformer()
        elif response_type == 'complainant':
            return ComplainantTransformer()
        else:
            raise Exception('Unable to handle this type of file')
