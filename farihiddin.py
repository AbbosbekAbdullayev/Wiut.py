
def assess_submission():
	circumstances = {
		"is_on_time": False,
		"within_24_hours": False,
		"within_5_days": False,	
		"late_submission": {
			"has_valid_reason": "",
			"is_accepted": False
		},
		"deferral_reassessment": False,
		"mark": 0
	}
	print(circumstances["mark"])
	on_time = input("Is your submission on time(yes or no): ")
	if(on_time == "yes"):
		circumstances["is_on_time"]=True
		circumstances["mark"]=100
	else:
		within_24_hours = input("After deadline, did you submit within 24 hours?(yes or no) ")
		if(within_24_hours == "yes"):
			circumstances["within_24_hours"]=True
			valid_reason = input("Do you have valid reason?(yes or no): ")
			reason = input("Write your reason: ")
			if(valid_reason == "yes"):
				circumstances["late_submission"]["has_valid_reason"] = reason
				if(reason):
					circumstances["late_submission"]["is_accepted"] = True
					circumstances["mark"] = 100
				else: 
					if(circumstances["mark"] > 40):
					  	circumstances["mark"] = circumstances["mark"]-10
			else:
				if(circumstances["mark"] > 40):
					  	circumstances["mark"] = circumstances["mark"]-10
		else:
			within_5_days = input("After deadline, is your submission within 5 days?(yes or no")
			if(within_5_days == "yes"):
				circumstances["within_5_days"]=True
				valid_reason = input("Do you have valid reason?(yes or no): ")
				reason = input("Write your reason: ")
				if(valid_reason):
					circumstances["late_submission"]["has_valid_reason"] = reason
					if(reason):
						circumstances["late_submission"]["is_accepted"] = True
						circumstances["mark"] = 100
					else:
						circumstances["mark"] = 0
				else:
					circumstances["mark"] = 0
			else:
				valid_reason = input("Do you have valid reason?(yes or no): ")
				reason = input("Write your reason: ")
				if(valid_reason):
					circumstances["late_submission"]["is_accepted"] = True
					circumstances["deferral_reassessment"] = True
					return "deferral_reassessment"
	print(circumstances["mark"])
	return circumstances["mark"]

assess_submission()