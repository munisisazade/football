import subprocess


def python_shell():
    subprocess.call("scrapy startproject footballdata",shell=True)
    # subprocess.call("python manage.py migrate", shell=True)