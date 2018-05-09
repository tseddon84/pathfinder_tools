from random import randint
import village_current
import io
import datetime as datetime
import math


def roll_dice(value,modifer):
	die_value=randint(1, value)
	if die_value==1:
		die_value=-10
	if die_value==20:
		die_value=30
	die_value=die_value+modifer
	return die_value

def hunt_food(number,modifer):
	if number==0:
		return 0
	provision=0
	for x in range(number):
		result=roll_dice(20,modifer)
		if result>=10:
			result=result-10
			result=result/2
			provision=provision+1+result
	return provision

def build_shelter(number,modifer):
#craft or survival dc 12
#+2 houses assitional person
	if number==0:
		return 0
	shelter=0
	for x in range(number):
		result=roll_dice(20,modifer)
		if result>=12:
			result=result-12
			result=result/2
			shelter=shelter+1+result
	return shelter

def gather_animals(number,modifer):
#handle animal 16 recover an animal
#10+animals
#provsion 1/3 days
	if number==0:
		return 0
	animal=0
	for x in range(number):
		result=roll_dice(20,modifer)
		#print(result)
		if result>=16:
			animal+=1
	return animal


def manage_herd(herd,number):
	goal=int(math.ceil(herd/10))
	#print(goal, "Goal")
	modifer=math.floor((number-goal)/goal)*2
	modifer+=15
	success=0
	for count in range(0,goal):
		die_roll=roll_dice(20,modifer)
		#print(die_roll,'die roll')
		if(die_roll>=20):
			success+=1
	#print(success,"Success")
	if(success==goal):
		return herd/3
	else:
		return 0

def tend_herds(number,modifer):
	success=0
	for count in range(0,number):
		die_roll=roll_dice(20,modifer)
		if(die_roll>=10):
			success+=1
	return success



def scouting(number,modifer):
#survival check dc 10
#disover point of interst or reduce random encounter chance
	if number==0:
		return 0
	find=0
	for x in range(number):
		result=roll_dice(20,modifer)
		if result>=10:
			find=find+1
	return find
def stand_watch(number,modifer):
#prevent nighttime encounter
	if number==0:
		return 0
	prevent=0
	for x in range(number):
		result=roll_dice(20,modifer)
		if result>=10:
			prevent=prevent+1
	return prevent

def gather_alchemy(number,modifer):
#survivale or craft 16 recover aclhemy supplies
	if number==0:
		return 0
	alchemy=0
	for x in range(number):
		result=roll_dice(20,modifer)
		if result>=16:
			alchemy=alchemy+result
	return alchemy/10

def gather_magic(number,modifer):
#survivale or craft 16 recover aclhemy supplies
	if number==0:
		return 0
	magic=0
	for x in range(number):
		result=roll_dice(20,modifer)
		#print(result)
		if result>=16:
			magic=magic+result
			#print(magic)
	return magic/10

def treat_Villagers(number,modifer):
#survivale or craft 16 recover aclhemy supplies
	if number==0:
		return 0
	heal=0
	for x in range(number):
		result=roll_dice(20,modifer)
		if result>=16:
			heal=heal+6
	return heal

def craft_project(number,dc,modifer):
	project=0
	for count in range(0,number):
		die_roll=roll_dice(20,modifer)
		if(die_roll>=dc):
			project+=(die_roll*dc/5)
	return project


def harvest_minerals(number,modifer):
	minerals=0
	for count in range(0,number):
		die_roll=roll_dice(20,modifer)
		if(die_roll>=10):
			minerals+=float(die_roll)
	return minerals/10

def harvest_wood(number,modifer):
	wood=0
	for count in range(0,number):
		die_roll=roll_dice(20,modifer)
		if(die_roll>=10):
			wood+=float(die_roll)
	return wood/10

def convert_month(month):
	if month=='January':
		new_month='Abadius'
	if month=='February':
		new_month='Calistril'
	if month=='March':
		new_month='Pharast'	
	if month=='April':
		new_month='Gozran'
	if month=='May':
		new_month='Desnus'
	if month=='June':
		new_month='Sarenith'
	if month=='July':
		new_month='Erastus'	
	if month=='August':
		new_month='Arodus'
	if month=='September':
		new_month='Rova'
	if month=='October':
		new_month='Lamashan'
	if month=='November':
		new_month='Neth'	
	if month=='December':
		new_month='Kuthona'
	return new_month

def convert_year(year):
	#print(year)
	year=year+2692
	#print(year)
	return year

def determine_date(days):
	date=datetime.datetime(2017, 1, 1) + datetime.timedelta(days - 1)
	#print(date)
	#print(type(date))
	month=date.strftime('%B')
	#print(month)
	day=date.strftime('%d')
	year=int(date.strftime('%Y'))
	#print(type(year))
	path_year=convert_year(year)
	path_month=convert_month(month)
	path_date="{0} {1}, {2}".format(path_month,day,path_year)
	#print(path_date)
	return path_date

def update_record(village):
	with open('village_history.txt','a') as game_file:
		date=determine_date(village['day'])
		line='---------------------------------------\n'
		game_file.write(line)
		line=date
		game_file.write(line)
		line='\n---------------------------------------\n'
		game_file.write(line)
		for element in village:
			line = "{0}={1}\n".format(element,village[element])
			game_file.write(line)
		line='---------------------------------------\n'
		game_file.write(line)

def update_current(village):
	with open('village_current.py','w') as game_file:
		line='village={0}'.format(village)
		game_file.write(line)

def update_population (village):
	option=eval(input('How many Aristocrats did you add? ') or '0')
	village['population']+=option
	village['Aristocrat']+=option
	option=eval(input('How many Adept did you add? ') or '0')
	village['population']+=option
	village['Adept']+=option
	option=eval(input('How many Commoner did you add? ') or '0')
	village['population']+=option
	village['Commoner']+=option
	option=eval(input('How many Expert did you add? ') or '0')
	village['population']+=option
	village['Expert']+=option
	option=eval(input('How many Warrior did you add? ') or '0')
	village['population']+=option
	village['Warrior']+=option
	option=eval(input('How many NPC did you add? ') or '0')
	village['population']+=option



def assign_jobs(village):
	assist=0
	herd_gained=0
	provision_gained=0
	magic_gained=0
	alchemy_gained=0
	shelters_gained=0
	scouting_gained=0
	sentry_gained=0
	villagers_healed=0
	minerals_harvested=0
	craft_progress=0
	wood_harvested=0
	success=0
	for villager in village['type']:
		assigned=0
		hunters=0
		builders=0
		crafters=0
		gather_animal=0
		herders=0
		alchemy=0
		magic=0
		medic=0
		miners=0
		scout=0
		sentry=0
		crafters=0
		foresters=0
		nothing=0
		while assigned!=village[villager]:
			print('You have {0} {1}'.format(village[villager],villager))
			hunters=eval(input('How many {0} will you send hunting? '.format(villager)) or '0')
			builders=eval(input('How many {0} will you have build shelters? '.format(villager)) or '0')
			crafters=eval(input('How many {0} will you have build your project? '.format(villager)) or '0')
			gather_animal=eval(input('How many {0} will you have search for animals? '.format(villager)) or '0')
			herders=eval(input('How many {0} will you have tend the herd? '.format(villager)) or '0')
			alchemy=eval(input('How many {0} will you have gather alchemical supplies? '.format(villager)) or '0')
			magic=eval(input('How many {0} will you have gather magic supplies? '.format(villager)) or '0')
			miners=eval(input('How many {0} will you have mine minerals? '.format(villager)) or '0')
			foresters=eval(input('How many {0} will you have harvest wood? '.format(villager)) or '0')
			medic=eval(input('How many {0} will you have tend injured? '.format(villager)) or '0')
			scout=eval(input('How many {0} will you have scout the area? '.format(villager)) or '0')
			sentry=eval(input('How many {0} will you have stand watch? '.format(villager)) or '0')
			nothing=eval(input('How many {0} will you have do nothing? '.format(villager)) or '0')
			assigned=hunters+builders+crafters+gather_animal+herders+alchemy+magic+miners+medic+scout+sentry+nothing+foresters
		
		if villager=='Adept':
			provision_gained+=hunt_food(hunters,6)
			assist+=tend_herds(herders,0)
			shelters_gained+=build_shelter(builders,0)
			herd_gained+=gather_animals(gather_animal,0)
			scouting_gained+=scouting(scout,0)
			villagers_healed+=treat_Villagers(medic,6)
			sentry_gained+=stand_watch(sentry,0)
			magic_gained+=gather_magic(magic,6)
			alchemy_gained+=gather_alchemy(alchemy,0)
			minerals_harvested+=harvest_minerals(miners,0)
			wood_harvested+=harvest_minerals(foresters,0)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,0)		
		if villager=='Adept_2':
			provision_gained+=hunt_food(hunters,15)
			assist+=tend_herds(herders,1)
			shelters_gained+=build_shelter(builders,1)
			herd_gained+=gather_animals(gather_animal,0)
			scouting_gained+=scouting(scout,0)
			villagers_healed+=treat_Villagers(medic,5)
			sentry_gained+=stand_watch(sentry,1)
			magic_gained+=gather_magic(magic,15)
			alchemy_gained+=gather_alchemy(alchemy,0)
			minerals_harvested+=harvest_minerals(miners,3)
			wood_harvested+=harvest_minerals(foresters,2)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,8)	
		if villager=='Aristocrat':
			provision_gained+=hunt_food(hunters,4)
			assist+=tend_herds(herders,0)
			shelters_gained+=build_shelter(builders,4)
			herd_gained+=gather_animals(gather_animal,0)
			scouting_gained+=scouting(scout,4)
			villagers_healed+=treat_Villagers(medic,0)
			sentry_gained+=stand_watch(sentry,0)
			magic_gained+=gather_magic(magic,4)
			alchemy_gained+=gather_alchemy(alchemy,4)
			minerals_harvested+=harvest_minerals(miners,0)
			wood_harvested+=harvest_minerals(foresters,0)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,0)
		if villager=='Commoner':
			provision_gained+=hunt_food(hunters,0)
			assist+=tend_herds(herders,8)
			shelters_gained+=build_shelter(builders,8)
			herd_gained+=gather_animals(gather_animal,8)
			scouting_gained+=scouting(scout,0)
			villagers_healed+=treat_Villagers(medic,0)
			sentry_gained+=stand_watch(sentry,6)
			magic_gained+=gather_magic(magic,0)
			alchemy_gained+=gather_alchemy(alchemy,0)
			minerals_harvested+=harvest_minerals(miners,0)
			wood_harvested+=harvest_minerals(foresters,0)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,0)
		if villager=='Expert':
			provision_gained+=hunt_food(hunters,5)
			assist+=tend_herds(herders,4)
			shelters_gained+=build_shelter(builders,8)
			herd_gained+=gather_animals(gather_animal,4)
			scouting_gained+=scouting(scout,5)
			villagers_healed+=treat_Villagers(medic,0)
			sentry_gained+=stand_watch(sentry,5)
			magic_gained+=gather_magic(magic,5)
			alchemy_gained+=gather_alchemy(alchemy,5)
			minerals_harvested+=harvest_minerals(miners,0)
			wood_harvested+=harvest_minerals(foresters,0)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,0)
		if villager=='Expert_2':
			provision_gained+=hunt_food(hunters,6)
			assist+=tend_herds(herders,6)
			shelters_gained+=build_shelter(builders,10)
			herd_gained+=gather_animals(gather_animal,5)
			scouting_gained+=scouting(scout,6)
			villagers_healed+=treat_Villagers(medic,1)
			sentry_gained+=stand_watch(sentry,7)
			magic_gained+=gather_magic(magic,6)
			alchemy_gained+=gather_alchemy(alchemy,6)
			minerals_harvested+=harvest_minerals(miners,7)
			wood_harvested+=harvest_minerals(foresters,11)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,17)
		if villager=='Warrior':
			provision_gained+=hunt_food(hunters,0)
			assist+=tend_herds(herders,5)
			shelters_gained+=build_shelter(builders,0)
			herd_gained+=gather_animals(gather_animal,5)
			scouting_gained+=scouting(scout,5)
			villagers_healed+=treat_Villagers(medic,0)
			sentry_gained+=stand_watch(sentry,5)
			magic_gained+=gather_magic(magic,0)
			alchemy_gained+=gather_alchemy(alchemy,0)
			minerals_harvested+=harvest_minerals(miners,0)
			wood_harvested+=harvest_minerals(foresters,0)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,0)
		if villager=='Ranger':
			provision_gained+=hunt_food(hunters,8)
			assist+=tend_herds(herders,10)
			shelters_gained+=build_shelter(builders,1)
			herd_gained+=gather_animals(gather_animal,9)
			scouting_gained+=scouting(scout,6)
			villagers_healed+=treat_Villagers(medic,1)
			sentry_gained+=stand_watch(sentry,7)
			magic_gained+=gather_magic(magic,8)
			alchemy_gained+=gather_alchemy(alchemy,8)
			minerals_harvested+=harvest_minerals(miners,9)
			wood_harvested+=harvest_minerals(foresters,8)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,8)
		if villager=='Ranger_2':
			provision_gained+=hunt_food(hunters,9)
			assist+=tend_herds(herders,11)
			shelters_gained+=build_shelter(builders,1)
			herd_gained+=gather_animals(gather_animal,10)
			scouting_gained+=scouting(scout,7)
			villagers_healed+=treat_Villagers(medic,1)
			sentry_gained+=stand_watch(sentry,8)
			magic_gained+=gather_magic(magic,9)
			alchemy_gained+=gather_alchemy(alchemy,9)
			minerals_harvested+=harvest_minerals(miners,10)
			wood_harvested+=harvest_minerals(foresters,9)
			if crafters>0:
				DC=eval(input("What is the DC of the project? ") or '15')
				craft_progress+=craft_project(crafters,DC,8)
	if assist>0:
		
		success=manage_herd(village['herd'],assist)
		provision_gained+=success
	village['provisions']+=provision_gained
	village['herd']+=herd_gained
	village['shelter']+=shelters_gained
	village['alchemy']+=alchemy_gained
	village['magic']+=magic_gained
	village["project"]+=craft_progress
	village["minerals"]+=minerals_harvested
	village["wood"]+=wood_harvested
	if success:
		print('Herd tended ', success)
	print('provisions gained ',provision_gained)
	print('magic gained ',magic_gained)
	print('alchemy gained ',alchemy_gained)
	print('shelter gained ',shelters_gained)
	print('herd gained ',herd_gained )
	print('scouting gained ',scouting_gained)
	print('sentry gained ',sentry_gained)
	print('Minerals mined ',minerals_harvested)
	print('Wood gathered ',wood_harvested)
	print('Crafting project progress ',craft_progress)

def feed_people (village):
	village['provisions']=village['provisions']-village['population']+12
	village['granary']=village['provisions']/village['population']

def update_resources(village):
	resources=('herd','shelter','provisions','magic','alchemy','minerals','project','wood')
	for key, value in village.items():
		if key in resources:
			value+=eval(input('Current value of {0}  is {1}. How much did it change?'.format(key, value)) or '0')
			village[key]=value
	#print(village)
	#print(village["project"])
	progress=village["project"]
	#print(progress)
	print('Your current project progress is {0}'.format(progress))
	result=input("Id your project done? Y/N ")
	if result=='Y':
		village["project"]=0




#class     Attack roll     Damage roll    hp    con_check     skills+4
#Adept        -1             1d4-1         3        0         heal,knowledge(relgion),spellcraft
#Aristocrat    0             1d6           4        0         knowledge(history,local,nobility),sense motive,survival
#Commoner      1             1d4+1         3        1         craft(any one),Handle Animal,perception
#Expert        0             1d4           4        1         craft (any 2), Knowledge(dungeoneering,engineeering,geography),profession,stealth,survival
#warrior       2             1d6+1         6        1         Handle Animal


#Adept={'hunter':0,'builder':0,'gather_animal':0,'herder':0,'alchemy':0,'magic':4,'medic':4,'scout':0,'sentry':0}
#Aristocrat={'hunter':4,'builder':4,'gather_animal':0,'herder':0,'alchemy':4,'magic':4,'medic':0,'scout':4,'sentry':0}
#Commoner={'hunter':0,'builder':4,'gather_animal':4,'herder':4,'alchemy':0,'magic':0,'medic':0,'scout':0,'sentry':4}
#Expert={'hunter':4,'builder':4,'gather_animal':0,'herder':0,'alchemy':4,'magic':4,'medic':0,'scout':4,'sentry':0}
#Warrior={'hunter':0,'builder':0,'gather_animal':4,'herder':4,'alchemy':0,'magic':0,'medic':0,'scout':0,'sentry':4}
#Program steps
#feed population
#if short prompt who is underfed
#Print fed population
#prompt Adept assignments
#prompt Aristocrat assignments
#prompt Commoner assignments
#prompt expert assignments
#prompt Warrior assignments
#resolve assignments
#update resources
#prompt to add new NPC's
#prompt to update stats

#Stats
#herd
#provisions
#shelter
#aclhemy supplies
#Magic supplies
#Sick/injured