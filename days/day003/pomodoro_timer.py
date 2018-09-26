from datetime import datetime, timedelta
import time
import sys


def pomodoro_timer_show(timer: int, timer_name: str):
    '''
    functon for show timer
    '''
    start = datetime.now().replace(microsecond=0)
    finish = start + timedelta(minutes=timer)
    for i in range(timer*60):
        time.sleep(1)
        now = datetime.now().replace(microsecond=0)
        sys.stdout.write(f'\r{timer_name} : {finish - now}')
        sys.stdout.flush()
    print()
    return None


def pomodoro_cycle(pomodoro_timer: int = 25, short_break: int = 5, long_break: int = 30,
               max_checkmark: int = 4):
    '''
    this function start one cycle of pomodoro timer
    '''
    now = datetime.now().strftime('%H:%M:%S %m/%d/%Y')
    print(f'now {now}, start new cycle of pomodoro')
    checkmark = 0
    pomodoro_timer_show(pomodoro_timer, 'time for work')
    checkmark += 1
    while checkmark < max_checkmark:
        pomodoro_timer_show(short_break, 'time for short break')
        pomodoro_timer_show(pomodoro_timer, 'time for work')
        checkmark += 1
    pomodoro_timer_show(long_break, 'time for long break')
    return None


def pomodoro(pomodoro_timer: int = 25, short_break: int = 5, long_break: int = 30,
             max_checkmark: int = 4):
    '''
    pomodoro timer (from wikipedia):
    1) decide on the task to be done: YES or NO
    2) set pomodoro timer (25min by default)
    3) work on the task
    4) end work when the timer rings and add one checkmark
    5) if nums of checkmark < max_checkmark take a short break (5min by default)
       and go to step 2)
    6) if nums of checkmark == max_checkmark take a long break (30min by default),
       zeroize checkmark and go to step 1)
    '''
    #first ask at firson about start pomodoro timer or exit
    pomodoro_ative = True
    while pomodoro_ative:
        question = input("start new pomodoro timer or not (y/n)? : ")
        if question in ['y','Y']:
            #start one cycle of pomodoro timer
            pomodoro_cycle(pomodoro_timer, short_break, long_break, max_checkmark)
        elif question in ['n','N']:
            #stop pomodoro
            now = datetime.now().strftime('%H:%M:%S %m/%d/%Y')
            print(f'now {now}, pomodoro stopped\ngood bye & goodluck')
            pomodoro_ative = False
        else:
            print("wrong answer, just try again")
    return None


if __name__ == '__main__':
    pomodoro()
    #pomodoro(pomodoro_timer = 1, short_break = 1, long_break = 1, max_checkmark = 2)
