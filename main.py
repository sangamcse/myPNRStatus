import json
import logging
import os.path
import requests

from tabulate import tabulate


def getAPI():
    __dir__ = os.path.dirname(__file__)
    apifile = os.path.join(__dir__, 'api.json')
    with open(apifile, encoding='utf-8') as api_data:
        api = json.loads(api_data.read())

    return api['api']


def getData(url):
    try:
        response = requests.get(url)
    
    except Exception as e:
        raise e

    content = response.json()
    if content['response_code'] is 200:
        displayInfo(content)
    else:
        logging.warn("Given information is wrong...")


def displayInfo(content):
    pnr = content['pnr']
    train_no = content['train']['number']
    train_name = content['train']['name']
    from_name = content['from_station']['name']
    boarding_name = content['boarding_point']['name']
    upto_name = content['reservation_upto']['name']
    journey_class = content['journey_class']['code']
    journey_date = content['doj']
    if content['chart_prepared']:
        chart_status = 'Yes'
    else:
        chart_status = 'No'
    passenger_count = content['total_passengers']
    status = [x for x in content['passengers']]
    booking_status = [status[i]['booking_status'] for i in range(len(status))]
    current_status = [status[i]['current_status'] for i in range(len(status))]
    
    msg = ('\n*** You Queried For : PNR Number: {} ***\n'
           'Charting Status: {}\tNo. of Passengers: {}\n'.format(
            pnr, chart_status, passenger_count))
    table = tabulate([[train_no, train_name, journey_date, from_name, 
                       upto_name, upto_name, boarding_name, journey_class]],
                     headers=['Train Number', 'Train Name', 'Boarding Date',
                              'From', 'To', 'Reserved Upto', 'Boarding Point',
                              'Class'])
    tablelist = [[i, booking_status[i], current_status[i]] for i \
                 in range(passenger_count)]
    passenger_table = tabulate(tablelist,
                               headers=['S. No.', 'Booking Status (Coach No ,'
                                        ' Berth No., Quota)', '*Current Status'
                                        ' (Coach No , Berth No.)'])
    print(msg)
    print('{}\n'.format(table))
    print(passenger_table)
    

def main():
    pnr = str(input("Enter your PNR: "))
    if len(pnr) is not 10:
        logging.warn("Enter a valid PNR...")
        return

    api = getAPI()
    url = ("https://api.railwayapi.com/v2/pnr-status/pnr/{}/apikey/"
           "{}".format(pnr, api))
    getData(url)  


if __name__ == '__main__':
    main()
