import collections
import json
def get_programs_json(programList):
    program_detail = []
    for program in programList:
        programJSON = collections.OrderedDict()
        programJSON['id'] = program[0]
        programJSON['name'] = program[1]
        programJSON['description'] = program[2]
        programJSON['imageurl'] = program[3]
        program_detail.append(programJSON)
    return json.dumps(program_detail)

def get_sections_json(sectionList):
    section_detail = []
    ind = 0
    for section in sectionList:
        ind= ind+1
        sectionJSON = collections.OrderedDict()
        sectionJSON['id'] = section[0]
        sectionJSON['name'] = section[1]
        sectionJSON['description'] = section[2]
        sectionJSON['imageurl'] = section[4]
        sectionJSON['order_index']=ind
        section_detail.append(sectionJSON)
    return json.dumps(section_detail)

def get_activities_json(activityList):
    activity_detail = []
    for activity in activityList:
        activityJSON = collections.OrderedDict()
        activityJSON['id'] = activity[0]
        activityJSON['text'] = activity[1]
        activity_detail.append(activityJSON)
    return json.dumps(activity_detail)

def get_activityQuestionnaires_json(activityList):
    res = []
    mapping = []
    for activity in activityList:
        temp_res = {}
        temp_op = {}
        temp_op['option_id']=activity[2]
        temp_op['option']= activity[3]
        if not activity[0] in mapping:
            mapping.append(activity[0])
            temp_res['question_id']=activity[0]
            temp_res['question']=activity[1]
            temp_res['options']=[]
            temp_res['options'].append(temp_op)
            res.append(temp_res)
        else:
            ind = mapping.index(activity[0])
            temp_res['question_id']=res[ind]['question_id']
            temp_res['question']=res[ind]['question']
            temp_res['options']=res[ind]['options']
            temp_res['options'].append(temp_op)
            res[ind]=temp_res
    return json.dumps(res)
    
