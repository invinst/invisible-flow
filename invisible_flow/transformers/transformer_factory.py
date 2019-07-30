from invisible_flow.transformers import CaseInfoAllegationsTransformer, InvestigatorTransformer


class TransformerFactory:

    @staticmethod
    def get_transformer(response_type):
        if response_type == 'case_info':
            return CaseInfoAllegationsTransformer()
        elif response_type == 'investigators':
            return InvestigatorTransformer()
        else:
            raise Exception('Unable to handle this type of file')
