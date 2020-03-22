import requests
from bs4 import BeautifulSoup
import csv
from random import sample, choice

URL = 'https://igra.msl.ua/megalote/uk/archive'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}


def get_html(url, params=None):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def content(html):
    soup = BeautifulSoup(html, 'html.parser')


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        content(html.text)
    else:
        print('Error')

    print(html)


parse()


def transform():
    """get csv file and return 2 lists with numbers"""
    temp_list = []  # empty list for temporary computation within function
    all_data = []  # empty list for adding all numbers from csv file

    with open('big_data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')  # open csv file

        for row in spamreader:
            temp_list.append((', '.join(row)))  # add all numbers from csv file to temp_list

        for i in temp_list:
            new_int = int(i)
            all_data.append(new_int)  # Transform all numbersfrom str to int and add to all_data list

    super_ball = all_data[6::7]  # determing super ball (every 7 numbers
    del all_data[6::7]  # deleting superball from all plural
    return all_data, super_ball


def calculate():
    """func gets all_data and superball lists and return min_list and max_lists where contain numbers
    with minimum and maximum chance of fall out by diving chance of occur to average chance of occur. """
    all_data, super_ball = transform()  # call transform func and assign its value to variable
    chance = []  # empty list for calculating hance of chance of falling out

    for i in range(0, 42):  # 0-42 posible total numbers
        chance.append((all_data.count(i)) / len(all_data) * 100)    #calculate chance of fall out by iterating dividing occurence 1-42 numbers to len all data list.
    average = sum(chance) / len(chance)     #determine average chance of fall out for all 1-42 numbers
    min_list = []       #emty list for further adding numbers which chance of fall are lower than average
    max_list = []       #emty list for further adding numbers which chance of fall are bigger than average

    for index, item in enumerate(chance):

        if item < average:
            min_list.append(index + 1)  #determine and adding to min list numbers which lower chance to fall out than average chance

        elif item >= average:
            max_list.append(index + 1)  #determine and adding to max list numbers which bigger chance to fall out than average chance

    return min_list, max_list, super_ball


def result():
    '''Get min and max list and print 6 numbers from each list by random + 1 number from super_ball list'''
    min_list, max_list, super_ball = calculate()
    print('First attempt: ', sample(min_list, 6), 'Superball', '', choice(super_ball))
    print('The second attempt: ', sample(max_list, 6), 'Superball', '', choice(super_ball))


if __name__ == '__main__':
    result()
