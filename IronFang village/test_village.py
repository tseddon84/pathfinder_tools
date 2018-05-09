from village_functions import *
from village_current import *

village['day']+=1
assign_jobs(village)
feed_people (village)
option=input('Do you need to update resources Y/N 'or 'N')
if option=='Y':
	update_resources(village)
option=input('Do you need to update population Y/N ' or 'N')
if option=='Y':
	update_population(village)
update_current(village)
update_record(village)