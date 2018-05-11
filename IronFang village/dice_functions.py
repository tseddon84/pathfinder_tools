from random import randint
from math import floor

def roll_dice(value,modifer):
	die_value=randint(1, value)
	if die_value==1:
		die_value=-10
	if die_value==20:
		die_value=30
	die_value=die_value+modifer
	return die_value

def skill_check(modifer,DC)
	value=roll_dice(20,modifer)
	if value>=DC:
		return 1
	return 0

def skill_check_threshold(modifer,DC,threshold)
	success=0
	value=roll_dice(20,modifer)
	if value>=DC:
		success+=1
		value-=DC
		success+=floor(value/threshold)
	return success

def skill_check_cf(modifer,DC,fail)
	value=roll_dice(20,modifer)
	if value>=DC:
		return 'success'
	if value<=DC-fail
		return'critical_fali'
	return 'failue'

def skill_check_value(modifer,DC)
	value=roll_dice(20,modifer)
	if value>=DC:
		return value
	return 0

def skill_check_cf_value(modifer,DC,fail)
	value=roll_dice(20,modifer)
	if value>=DC:
		return value
	if value<=DC-fail
		return -1
	return 0