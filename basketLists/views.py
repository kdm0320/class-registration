import json
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models
from classs import models as class_model
from registrations import models as regist_model
from classs import views as class_view


@login_required
def basket(request):
    template_name = "basket.html"
    lists = models.List.objects.get_or_none(user=request.user)
    if lists:
        data = lists.subjects.values()
        temp_data = {}
        for i in range(len(data)):
            temp_data[f"class{i}"] = data[i]
        datas = json.dumps(temp_data, ensure_ascii=False, cls=DjangoJSONEncoder)

        return render(request, template_name, {"basket_datas": datas})
    else:
        return render(request, template_name)


def class_to_dictionary(data):
    output = {}
    output["subject_number"] = data.subject_number
    output["subject_name"] = data.subject_name
    output["grade"] = data.grade
    output["check_major"] = data.check_major
    output["credit"] = data.credit
    output["professor"] = data.professor
    output["time"] = data.time
    output["people"] = data.people
    output["universe"] = data.universe
    output["department"] = data.department
    return output


class HandleRegiTimeData(class_view.HandleTimeData):
    def remove_data(self, target_time, user_basket_data):
        if target_time[1] == "(":
            new_data = self.change_time_data(target_time)
            user_basket_data.time_table[target_time[0]].remove(new_data)
        else:
            check_time = []
            for index, data in enumerate(target_time[1:]):
                check_time.append(data)
                if len(check_time) == 2:
                    if check_time[1].isdigit():
                        time = "".join(check_time)
                        user_basket_data.time_table[target_time[0]].remove(time)
                    else:
                        user_basket_data.time_table[target_time[0]].remove(
                            check_time[0]
                        )
                    check_time = []
                elif len(check_time) == 1 and index == len(target_time[1:]) - 1:
                    user_basket_data.time_table[target_time[0]].remove(check_time[0])


@login_required
def send_to_regi(request):
    jsonObject = json.loads(request.body)
    target_pk = jsonObject.get("id")
    target = class_model.Class.objects.get(pk=target_pk)
    target_time = target.time.replace(" ", "")
    user_basket_data = models.List.objects.get(user=request.user)
    user_basket_list = user_basket_data.subjects
    split_subject_time = []
    if "/" in target_time:
        split_subject_time = target_time.split("/")
    handle_time_data = HandleRegiTimeData()

    message_data = {"messages": "nothing"}

    alpha_to_numbers = {
        "A": ["1", "2"],
        "B": ["3"],
        "C": ["4", "5"],
        "D": ["6"],
        "E": ["7", "8"],
        "F": ["9"],
        "G": ["10", "11"],
        "H": ["12"],
        "ND": ["13", "14"],
        "SC": ["15"],
    }
    numbers_to_alpha = {
        "1": "A",
        "2": "A",
        "3": "B",
        "4": "C",
        "5": "C",
        "6": "D",
        "7": "E",
        "8": "E",
        "9": "F",
        "10": "G",
        "11": "G",
        "12": "H",
        "13": "ND",
        "14": "ND",
        "15": "SC",
    }

    regi_list = regist_model.registration.objects.get_or_none(user=request.user)
    if regi_list is None:
        new_list = regist_model.registration.objects.create(user=request.user)
        new_list.subjects.add(target)
        if len(split_subject_time) == 0:
            handle_time_data.create_data(target_time, new_list)
            handle_time_data.remove_data(target_time, user_basket_data)
        else:
            for split_data in split_subject_time:
                handle_time_data.create_data(split_data, new_list)
                handle_time_data.remove_data(split_data, user_basket_data)
        new_list.credits += int(target.credit)
        user_basket_list.remove(target)
        user_basket_data.save()
        new_list.save()
    else:
        if regi_list.credits < 23:
            if len(split_subject_time) == 0:
                check_schedule = []
                handle_time_data.check_data(
                    target_time, regi_list, numbers_to_alpha, check_schedule
                )
                if True not in check_schedule:
                    user_basket_list.remove(target)
                    handle_time_data.remove_data(target_time, user_basket_data)
                    regi_list.subjects.add(target)
                    handle_time_data.regi_data(target_time, regi_list)
                    regi_list.credits += int(target.credit)
                else:
                    message_data["messages"] = "해당 시간에 과목이 이미 시간표에 존재합니다."

            else:
                check_schedule = []
                if split_subject_time[0][1] == "(":
                    for split_data in split_subject_time:
                        new_data = handle_time_data.change_time_data(split_data)
                        for number in alpha_to_numbers[new_data]:
                            if (number in regi_list.time_table[split_data[0]]) or (
                                new_data in regi_list.time_table[split_data[0]]
                            ):
                                check_schedule.append(True)

                    if True not in check_schedule:
                        regi_list.subjects.add(target)
                        for split_data in split_subject_time:
                            new_data = handle_time_data.change_time_data(split_data)
                            regi_list.time_table[split_data[0]].append(new_data)
                            handle_time_data.remove_data(split_data, user_basket_data)
                        user_basket_list.remove(target)
                        regi_list.credits += int(target.credit)
                    else:
                        message_data["messages"] = "해당 시간에 과목이 이미 시간표에 존재합니다."
                else:
                    for split_data in split_subject_time:
                        handle_time_data.check_data(
                            split_data, regi_list, numbers_to_alpha, check_schedule
                        )

                        if True not in check_schedule:
                            handle_time_data.regi_data(split_data, regi_list)
                            handle_time_data.remove_data(split_data, user_basket_data)
                            regi_list.subjects.add(target)
                            regi_list.credits += int(target.credit)
                            user_basket_list.remove(target)
                        else:
                            message_data["messages"] = "해당 시간에 과목이 이미 시간표에 존재합니다."
                            break
                    if True not in check_schedule:
                        regi_list.credits += int(target.credit)
                check_schedule = []
        else:
            message_data["messages"] = "수강가능 학점을 넘었습니다."

        user_basket_data.save()
        regi_list.save()
    message = json.dumps(message_data, ensure_ascii=False)
    return HttpResponse(message, content_type="application/json")


@login_required
def delete(request):
    pass
    # jsonObject = json.loads(request.body)
    # user_list = models.List.objects.get(user=request.user)
    # target_pk = jsonObject.get("id")
    # target = class_model.Class.objects.get(id=target_pk)
    # target_time = target.time.replace(" ", "")
    # split_subject_time = []
    # if "/" in target_time:
    #     split_subject_time = target_time.split("/")

    # delete_time = HandleRegiTimeData()

    # if len(split_subject_time) == 0:
    #     user_list.subjects.remove(target)
    #     delete_time.remove_data(target_time, user_list)
    # else:
    #     for split_data in split_subject_time:
    #         delete_time.remove_data(split_data, user_list)
    #     user_list.subjects.remove(target)
    # user_list.save()
    # non_data = {}
    # return JsonResponse(non_data)
