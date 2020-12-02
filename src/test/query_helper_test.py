import unittest
from ..query_helper import get_program_sql_query
from ..query_helper import get_section_sql_query
from ..query_helper import get_activity_sql_query
from ..query_helper import get_activity_questionnaire_sql_query

class QueryValidate(unittest.TestCase):
    def test_program_query(self):
        query = get_program_sql_query()
        expected_query = "select id, name, description, imageurl from program"
        self.assertEqual(query, expected_query)

    def test_section_query(self):
        query = get_section_sql_query()
        expected_query = "select id, name, description, program_id, imageurl from section where program_id = %s"
        self.assertEqual(query, expected_query)

    def test_activity_query(self):
        query = get_activity_sql_query()
        expected_query = "select id, text from activity where section_id = %s"
        self.assertEqual(query, expected_query)

    def test_activity_questionnaire_query(self):
        query = get_activity_questionnaire_sql_query()
        expected_query = "select q.id as question_id, q.question as question, op.id as option_id, op.questionnaire_option as questionnaire_option from activity_questionnaire q left outer join activity_questionnaire_option_list op on q.id=op.activity_questionnaire_id where section_id = %s "
        self.assertEqual(query, expected_query)

if __name__ == "__main__":
    unittest.main()