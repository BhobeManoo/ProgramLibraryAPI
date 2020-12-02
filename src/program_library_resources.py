from flask import Flask
from flask_restful import Api,Resource
import mysql.connector
from mysql.connector import Error
import config
import collections
import json
import query_helper
import result_formatter

app=Flask(__name__)
api=Api(app, prefix="/api/v1")

class DatabaseConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(host=config.DATABASE_CONFIG['host'],
                                                database=config.DATABASE_CONFIG['dbname'],
                                                user=config.DATABASE_CONFIG['user'],
                                                password=config.DATABASE_CONFIG['password']
                                                )
        self.cursor = self.connection.cursor()

    def query(self,sql_query,to_filter):
        self.cursor.execute(sql_query,to_filter)
        return  self.cursor.fetchall() 

    def __del__(self):
        if (self.connection.is_connected()):
            self.connection.close()
            self.cursor.close()

class Programs(Resource):
    def get(self):
        db=DatabaseConnection()
        sql_query = query_helper.get_program_sql_query()
        to_filter=[]
        programList = db.query(sql_query,to_filter)
        return result_formatter.get_programs_json(programList)


class Sections(Resource):
    def get(self,program_id):
        sql_query =  query_helper.get_section_sql_query()
        to_filter=[]
        to_filter.append(program_id)
        db=DatabaseConnection()
        sectionList = db.query(sql_query, to_filter)   
        return result_formatter.get_sections_json(sectionList);  

class Activities(Resource):
    def get(self,section_id):
        sql_query =  query_helper.get_activity_sql_query()
        to_filter=[]
        to_filter.append(section_id)
        db=DatabaseConnection()
        activityList = db.query(sql_query, to_filter)     
        return result_formatter.get_activities_json(activityList);  

class ActivityQuestionnaires(Resource):
    def get(self,section_id):
        sql_query = query_helper.get_activity_questionnaire_sql_query()
        to_filter=[]
        to_filter.append(section_id)
        db=DatabaseConnection()
        activityList = db.query(sql_query, to_filter)   
        return result_formatter.get_activityQuestionnaires_json(activityList);  

api.add_resource(Programs,'/programs/')
api.add_resource(Sections,'/programs/sections/<program_id>')
api.add_resource(Activities,'/programs/activities/<section_id>')
api.add_resource(ActivityQuestionnaires,'/programs/activity_questionnaires/<section_id>')

if __name__ == "__main__":
    app.run(debug=True)