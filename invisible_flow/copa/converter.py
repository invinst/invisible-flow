
def convert_sql_alchemy_obj_to_dict(sql_alchemy_obj):
    dict_like = sql_alchemy_obj.__dict__.copy()
    dict_like.pop('_sa_instance_state', None)

    return dict_like
