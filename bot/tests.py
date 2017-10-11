import os
#os.system('cd C:\project\python\wxpybot python manage.py runserver')

tmp = os.popen('cd C:\project\python\wxpybot \n python manage.py runserver').readlines()
print(tmp)
