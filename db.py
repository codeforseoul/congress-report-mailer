import logging

from pymongo import MongoClient
from settings import MONGO_USERNAME, MONGO_PASSWORD

client = MongoClient('localhost', 27017)
db = client.congress_report

attendance = db.attendance_results
plenary = db.plenary_session_results

def get_data_by_assembly(assembly, target):
    if target == 'attendance':
        db = attendance
    elif target == 'plenary':
        db = plenary
        
    return db.find_one({'assembly_id': assembly})

def calc_rate_of_attendance(data):
    try:
        times = 0
        for attend in data:
            print(attend)
            times = times + 1 if attend['attend'] == '출석' else times
        rate = round(times/len(data), 2) * 100
        return rate

    except Exception as e:
        logging.exception(e)
        return

def get_rate_of_attendance(assembly):
    data = get_data_by_assembly(assembly, 'attendance')
    
    main_attend = data['main_attend']
    sub_attend = data['sub_attend']
    
    main_rate = calc_rate_of_attendance(main_attend)
    sub_rate = calc_rate_of_attendance(sub_attend)
    
    return {
        'main_rate': main_rate,
        'sub_rate': sub_rate
    }

if __name__ == '__main__':
    print(get_rate_of_attendance(837))
