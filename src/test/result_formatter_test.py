import unittest
from  ..result_formatter import get_programs_json
from  ..result_formatter import get_sections_json
from  ..result_formatter import get_activities_json
from  ..result_formatter import get_activityQuestionnaires_json
import json

class ResultValidate(unittest.TestCase):
    def test_program_result(self):
        programList = [(1, 'Program1', 'description of Program1', 'image url for Program1'), (2, 'Program2', 'description of Program2', 'image url for Program2')]
        programs = get_programs_json(programList)
        expected_result = [{"id": 1, "name": "Program1", "description": "description of Program1", "imageurl": "image url for Program1"}, {"id": 2, "name": "Program2", "description": "description of Program2", "imageurl": "image url for Program2"}]
        self.assertEqual(programs, json.dumps(expected_result))

    def test_section_result(self):
        sectionList=[(1, 'section1', 'section1 description', 1, 'section1 url'), (2, 'section2', 'section2 description', 1, 'section2 url'), (3, 'section3', 'section3 description', 1, 'section3 url'), (4, 'section4', 'section4 description', 1, 'section4 url')]
        sections = get_sections_json(sectionList)
        expected_result = [{"id": 1, "name": "section1", "description": "section1 description", "imageurl": "section1 url", "order_index": 1}, {"id": 2, "name": "section2", "description": "section2 description", "imageurl": "section2 url", "order_index": 2}, {"id": 3, "name": "section3", "description": "section3 description", "imageurl": "section3 url", "order_index": 3}, {"id": 4, "name": "section4", "description": "section4 description", "imageurl": "section4 url", "order_index": 4}]
        self.assertEqual(sections,json.dumps(expected_result))

    def test_activity_result(self):
        activityList = [(1, 'activity1'), (2, 'activity2')]
        activities = get_activities_json(activityList)
        expected_result = [{"id": 1, "text": "activity1"}, {"id": 2, "text": "activity2"}]
        self.assertEqual(activities, json.dumps(expected_result))

    def test_activity_questionnaire_result(self):
        activityList = [(1, 'question1', 1, 'option1'), (1, 'question1', 2, 'option2'), (1, 'question1', 3, 'option3'), (1, 'question1', 4, 'option4'), (3, 'question2', 7, 'option1'), (3, 'question2', 8, 'option2')]
        activities = get_activityQuestionnaires_json(activityList)
        expected_result = [{"question_id": 1, "question": "question1", "options": [{"option_id": 1, "option": "option1"}, {"option_id": 2, "option": "option2"}, {"option_id": 3, "option": "option3"}, {"option_id": 4, "option": "option4"}]}, {"question_id": 3, "question": "question2", "options": [{"option_id": 7, "option": "option1"}, {"option_id": 8, "option": "option2"}]}]
        self.assertEqual(activities, json.dumps(expected_result))

if __name__ == "__main__":
    unittest.main()