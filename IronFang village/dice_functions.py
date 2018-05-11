from random import randint
from math import floor

def roll_dice(number,sides,modifer):
	""" This function simulates rolling dice.  
	It a house rule for d20's to reset the value if a 20 or a 1 is rolled. 

	Number covers the number of dice to roll before applying the modifer.
	(NOTE: THIS IS NOT TO BE USED TO REPEAT A DICE ROLL, IT ASSUMES 
	THIS MANY DICE ARE NEEDED TO COMPLETE A SINGLE ROLL.)

	Sides is the number of sides on the die to roll.

	Modifer is the amount to be added after the die roll.

	It returns the die result plus the modifer.
	"""
	die_total=0
	for dice in range(0,number):
		die_value=randint(1, sides)
		if die_value==1 and sides=20:
			die_value=-10
		if die_value==20 and sides=20:
			die_value=30
		die_total+=die_value
	die_total=die_total+modifer
	return die_total

def skill_check(modifer,DC):
	""" This function handles a pass/fail skill check.
	
	modifer is the character's bonus to the skill.
	
	DC is the target number they must meet or exceed.
	
	It returns a 1 or 0 based on if you passed or failed.
	This shouldn't be used if there is an increased penalty if you fail by a value.
	"""

	value=roll_dice(1,20,modifer)
	if value>=DC:
		return 1
	return 0

def skill_check_threshold(modifer,DC,threshold):
	""" This function handles skill checks where there is a DC for success and a threshold for multiple successes.
	This is to be used when the exact value is not important, but rather the number of successes as defined as 1 
	for surpasssing the DC and additional 1 for every threshold above the DC round down.

	Modifer is the character bonus to the skill chec.

	DC is the number they must meet or exceed to pass.

	Threshold is the number by which they gain additional successes for every whole number multiple by which they exceed the DC.
	"""
	success=0
	value=roll_dice(1,20,modifer)
	if value>=DC:
		success+=1
		value-=DC
		success+=floor(value/threshold)
	return success

def skill_check_cf(modifer,DC,fail):
	"""
	This function handles a skill check where what is important to know if they passed, failed, 
	or failed by a threshold>X. This does not return the value of the roll, just a string to know the result.

	Modifer is the character bonus to the skill chec.

	DC is the number they must meet or exceed to pass.

	Fail is the number by which if they faily by that much or more they critically fail.
	"""

	value=roll_dice(1,20,modifer)
	if value>=DC:
		return 'success'
	if value<=DC-fail
		return'critical_fali'
	return 'failue'

def skill_check_value(modifer,DC):
		"""
	This function handles a skill check where you want the value of the roll if they pass.
	If the check fails it will return 0.

	Modifer is the character bonus to the skill chec.

	DC is the number they must meet or exceed to pass.

	"""
	value=roll_dice(1,20,modifer)
	if value>=DC:
		return value
	return 0

def skill_check_cf_value(modifer,DC,fail):
		"""
	This function handles a skill check where what is important to know if they passed, failed, 
	or failed by a threshold>X. This returns the value of the roll on a Pass, a 0 on failure and -1 on critical faliure.

	Modifer is the character bonus to the skill chec.

	DC is the number they must meet or exceed to pass.

	Fail is the number by which if they faily by that much or more they critically fail.

	"""

	value=roll_dice(20,modifer)
	if value>=DC:
		return value
	if value<=DC-fail
		return -1
	return 0