from os import spawnve
import time, requests, threading
from .models import Coin, Condition
from radarcx import settings
from .notif import *
from radarcxapp.models import *
#string_test = "logs:\n"


def conditionsChecker():
    #here we check whether any of conditions has been triggerd or #
    ''' note: we have not implemented 'equal' and 'moving_average','volume' yet. '''
    conditions = Condition.objects.all()
    for condition in conditions:
        coin_quantity = Coin.objects.filter(name=condition.coin).last().realtime_price
        if condition.smaller_or_greater == ">" and coin_quantity >= condition.quantity :
            username = User.objects.filter(id=condition.creator_id).first()
            coinName= condition.coin
            Bodytext = coinName + " is now " + str(coin_quantity) + "$ --- ( > " + str(condition.quantity) + "$ )"
            user  = User.objects.filter(id=condition.creator_id).first()
            usertokens = user.usertoken_set.all()
            one_user_tokens = [ record.token for record in usertokens ]
            NajveResponse = send_to_users(body= Bodytext,
            subscriber_tokens= one_user_tokens,
            sent_time=UTC_to_IR_TimeZone())

        if condition.smaller_or_greater == "<" and coin_quantity <= condition.quantity :
            username = User.objects.filter(id=condition.creator_id).first()
            coinName= condition.coin
            Bodytext = coinName + " is now " + str(coin_quantity) + "$ --- ( < " + str(condition.quantity) + "$ )"
            user  = User.objects.filter(id=condition.creator_id).first()
            usertokens = user.usertoken_set.all()
            one_user_tokens = [ record.token for record in usertokens ]
            NajveResponse = send_to_users(body= Bodytext,
            subscriber_tokens= one_user_tokens,
            sent_time=UTC_to_IR_TimeZone())



def fetchData_and_check():
    # while(True): 
    # print("here I receive data of all coins and store them in DB")
    url = 'https://min-api.cryptocompare.com/data/price'

    parameters = {'fsym': "BTC",
                'tsyms': "USD"}
    exchange = ''

    if exchange:
        print('exchange: ', exchange)
        parameters['e'] = exchange

    # response comes as json
    response = requests.get(url, params=parameters)
    data = response.json()

    c = Coin.objects.filter(name=parameters["fsym"]).first()
    c.realtime_price=data[parameters["tsyms"]]
    c.save()
    conditionsChecker()  # Synchronizicly we runn this fun & wait till it ends