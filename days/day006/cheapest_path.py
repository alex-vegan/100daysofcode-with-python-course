# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:43:45 2018
100DaysOfCode --- TalkPython --- Pybites
4-6days --- collections module
@author: Alexey Sidorov 
"""

from collections import deque

#this graph contains all adjacent cities with cost for flight
bonds = {'Yekaterinburg': {'Kiev':101, 'St Peterburg':85, 'Moscow':65, 'Georgia':100},
         'Kiev': {'Yekaterinburg':101, 'Berlin':60, 'Vienna':50, 'Sofia':50, 'Georgia':70},
         'Rome': {'Paris':50, 'Madrid':60, 'Berlin':55, 'Sofia':40},
         'Paris': {'Madrid':50, 'London':15, 'Berlin':40, 'Rome':50},
         'Berlin': {'Paris':40, 'Rome':55, 'Vienna':25, 'Kiev':60, 'Moscow':80},
         'London': {'Paris':15, 'Oslo':55},
         'Oslo': {'London':55, 'Helsinki':40},
         'Helsinki': {'Oslo':40, 'Moscow':45, 'St Peterburg':15},
         'St Peterburg': {'Helsinki':15, 'Moscow':30, 'Yekaterinburg':85},
         'Moscow': {'Yekaterinburg':65, 'St Peterburg':30, 'Helsinki':45, 'Georgia':80, 'Berlin':80, 'Vienna':85},
         'Vienna': {'Madrid':80, 'Berlin':25, 'Sofia':40, 'Kiev':50, 'Moscow':85},
         'Sofia': {'Rome':40, 'Vienna':40, 'Kiev':50, 'Istanbul':25},
         'Istanbul': {'Sofia':25, 'Georgia':60},
         'Georgia': {'Istanbul':60, 'Kiev':70, 'Moscow':80, 'Yekaterinburg':100},
         'Madrid': {'Paris':50, 'Vienna':80, 'Rome':60}}


START_CITY = 'Yekaterinburg'
FINISH_CITY = 'Madrid'


def dijkstra(bond_grapth, start_city=START_CITY):
    que_que = deque()   # queue type from collection module
    cheapest_paths = {}  # shortest path dict
    cheapest_paths[start_city] = 0
    que_que.append(start_city)
    while que_que:
        v = que_que.popleft()   # one vertex from queue yet
        for u in bond_grapth[v]:    # neighbours of city
            if (u not in cheapest_paths or cheapest_paths[v] + bond_grapth[v][u] < cheapest_paths[u]):
                cheapest_paths[u] = cheapest_paths[v] + bond_grapth[v][u]
                que_que.append(u)
    return cheapest_paths


def reveal_cheapest_path(bond_grapth, cheapest_paths, finish_city=FINISH_CITY):
    cheapest_path = [finish_city]    
    v = finish_city     # vertex of graph in the end of shortest path list
    while cheapest_paths[v] != 0:
        for u in bond_grapth[v]:    # neighbours of current city
            if cheapest_paths[v] - bond_grapth[v][u] == cheapest_paths[u]:
                cheapest_path.append(u)
                break
        v = u
    return cheapest_path


def main():
    '''
    this function counts of flight cost between cities
    1) first input start city from list:
    
    Yekaterinburg, Kiev, Rome, Paris, Berlin, London, Oslo, Helsinki, 
    St Peterburg, Moscow, Vienna, Sofia, Istanbul, Georgia, Madrid
    
    !!! be sure that name of city start from Capital letter !!!
    
    2) second input stop city from same list
    
    3) receive path and cost of it
    '''
    start = input("From what city to start? ")
    while start not in bonds:
        start = input("That city isn't possible for flight. " +
                      "From what city to start? ")
    cheapest_paths = dijkstra(bonds, start)
    finish = input("To what city to build the path? ")
    while finish not in bonds:
        finish = input("That city isn't possible for flight. " +
                       "To what city to build the path? ")
    cheapest_path = reveal_cheapest_path(bonds, cheapest_paths, finish)
    print('\ncheapest path is {}\ncheapest path cost'
          ' = {}$'.format(str(cheapest_path[::-1]), str(cheapest_paths[finish])))
    return None


if __name__ == "__main__":
    main()
