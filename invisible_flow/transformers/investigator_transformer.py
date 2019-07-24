from invisible_flow.transformers.transformer_base import TransformerBase


class InvestigatorTransformer(TransformerBase):

    def transform_investigator_csv_to_entity_list(self):
        pass

    def transform(self, response_type, file_content: str):
        return self.transform_investigator_csv_to_entity_list()
