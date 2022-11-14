import schedule
from datetime import datetime
from time import sleep

def saludo(texto):
    print('\r',texto,datetime.now())

job_5s = schedule.every(5).seconds.do(saludo, texto = 'cada 5 segundos')

job_10s = schedule.every(10).seconds.do(saludo, texto = 'cada 10 segundos')

job_minute = schedule.every(1).minutes.do(saludo, texto = 'cada 1 minuto')

job_3hours = schedule.every(3).hours.do(saludo, texto = 'cada 3 horas')

# ejecucion hasta un momento

job_monday = schedule.every().monday.until('2023-8-1').do(saludo, texto = 'Hasta el 1/8/2023')


# ejecucion en un momento concreto

job_day = schedule.every().day.at('04:00').do(saludo, texto = 'cada dia a las 4:00')

job_sunday = schedule.every().sunday.at('23:00').do(saludo, texto = 'domingos a las 23:00')

# cancelar una tarea
schedule.cancel_job(job_5s) # cancelamos la tarea

# podemos etiquetar las tareas

job_sunday.tag('weekly')
job_monday.tag('weekly')


job_10s.tag('minutely')
job_5s.tag('minutely')

job_minute.tag('hourly')
job_3hours.tag('hourly')


# podemos ver las tareas pendientes

print('Todos los jobs')
jobs_all = schedule.get_jobs()

for job in jobs_all:
    print(job,job.tags)

print('jobs minutely')
jobs_minutely = schedule.get_jobs('minutely')
for job in jobs_minutely:
    print(job,job.tags)

print('Ultima ejecucion de 10s fue',job_10s.last_run)

# bucle para que comprobar y ejecutar las tareas

while True:
    schedule.run_pending()

    fecha = datetime.now()
    msg = 'tic'
    if fecha.second % 2 == 0:
        msg = 'tic'
    else:
        msg = 'tac'
    print(msg,fecha,end = '\r') # no hay salto de linea y volvermos al principio de la linea
    sleep(1)
 