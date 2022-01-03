import os, requests, time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
from colorama import Fore, Style


def screen_clear():
    _ = os.system('cls')


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def laravelcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/.env" or "/test/.env" or "api/.env"or"laravel/.env"or"admin/.env"or"vendor/.env"or"sites/.env"or"blog/.env"or"system/.env"or"public/.env"or"shop/.env"
    check = requests.get(url, headers=headers, timeout=3)
    resp = check.text
    try:
        if "DB_HOST" in resp:
            print(f"Laravel {gr}OK{res} => {star}\n")
            mrigel = open("Laravel.txt", "a")
            mrigel.write(f'{star}\n')
        else:
            print(f"{red}Not{res} Laravel => {star}\n")
    except:
        pass
def wpcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/wp-content/"
    check = requests.get(url, headers=headers, timeout=3)
    try:
        if check.status_code == 200:
            print(f"Wordpress {gr}OK{res} => {star}\n")
            mrigel = open("Wordpress.txt", "a")
            mrigel.write(f'{star}\n')
        else:
            print(f"{red}Not{res} Wordpress => {star}\n")
    except:
        pass


def filter(star):
    try:
       laravelcheck(star)
       wpcheck(star)
    except:
       pass


def main():
    print('''

    \033[33m

            \033[36m    ___       __      _______               ______                _____
\033[0m                __ |     / /_____ ___    |_____________ ___  / _____ _______ ____(_)______ _______
\033[31m                __ | /| / / _  _ \__  /| |__  ___/_  _ \__  /  _  _ \__  __ `/__  / _  __ \__  __ $
\033[0m                __ |/ |/ /  /  __/_  ___ |_  /    /  __/_  /___/  __/_  /_/ / _  /  / /_/ /_  / / /
            \033[34m    ____/|__/   \___/ /_/  |_|/_/     \___/ /_____/\___/ _\__, /  /_/   \____/ /_/ /_/
                                                                  /____/
    ''')
    list = input(f"{gr}Give Me Your List.txt/{red}Mylegion> {gr}${res} ")
    star = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(50)
       ThreadPool.map(filter, star)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass

if __name__ == '__main__':
    screen_clear()
    main()
