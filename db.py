import logging

from pymongo import MongoClient
from datetime import date, datetime

from settings import MONGO_DB, MONGO_PORT, MONGO_USERNAME, MONGO_PASSWORD, DB_NAME

# TODO: sign in to connect to mongodb
client = MongoClient(MONGO_DB, MONGO_PORT)
db = client[DB_NAME]

attendance = db.attendance_results
plenary = db.plenary_session_results

# change this value to `date.today().replace(year = date.today().year - 1)` if you wanna test
today = date.today()

DATE_FROM = today.replace(day = 1)
DATE_TO = DATE_FROM.replace(month = DATE_FROM.month + 1) if DATE_FROM.month < 12 else DATE_FROM.replace(year = today.year + 1, month = 1)

def classify_attendances(data):
    # TODO: add more options such as '기권'
    return {
        'attendance': [session for session in data if session['attend'] == '출석'],
        'absent': [session for session in data if session['attend'] != '출석']
    }

def get_attends_on_month(data):
    return [session for session in data
        if (DATE_FROM <= datetime.utcfromtimestamp(session['date']/1000.0).date() and
        DATE_TO > datetime.utcfromtimestamp(session['date']/1000.0).date())]

def get_attendances_by_assembly(assembly):
    data = attendance.find_one({'assembly_id': assembly})
    
    # TODO: error handling if result is None
    main_attend = get_attends_on_month(data['main_attend'])
    sub_attend = get_attends_on_month(data['sub_attend'])

    main_sessions = classify_attendances(main_attend)
    sub_sessions = classify_attendances(sub_attend)
    
    return {
        'main_sessions': main_sessions,
        'sub_sessions': sub_sessions
    }
    
def get_vote_results_by_assembly(assembly):
    votes = plenary.find({'처리날짜': {'$gt': DATE_FROM.isoformat(), '$lt': DATE_TO.isoformat()}})    

    results = [{ 'title': v['의안명'], 'date': v['처리날짜'], 'result': result['type']} for v in votes for result in v['vote_results'] if assembly in result['member_idxs']]

    return results

if __name__ == '__main__':
    # test
    print('이번 달 출석 현황')
    print(get_attendances_by_assembly(709))
    print('이번 달 표결 현황')
    print(get_vote_results_by_assembly(813))
