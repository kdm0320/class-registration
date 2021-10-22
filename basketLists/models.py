from registrations import models as regist_model


def default_time_table_dict():
    return {"월": [], "화": [], "수": [], "목": [], "금": []}


class List(regist_model.registration):
    class Meta:
        proxy = True
