
def get_program_sql_query():
    return "select id, name, description, imageurl from program"

def get_section_sql_query():
    return "select id, name, description, program_id, imageurl from section where program_id = %s"

def get_activity_sql_query():
    return "select id, text from activity where section_id = %s"

def get_activity_questionnaire_sql_query():
    return "select q.id as question_id, q.question as question, op.id as option_id, op.questionnaire_option as questionnaire_option from activity_questionnaire q left outer join activity_questionnaire_option_list op on q.id=op.activity_questionnaire_id where section_id = %s "