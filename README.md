# NOTE: THE EMAIL FEATURE IS NOT JET IMPLEMENTED.

## PROJECT NAME: MEDICAL RESERVE ALARM

## WHAT I WANT:
	I want a system that notifies my (ideally by email) when a medical hour is now available. I want to tell the 
	system the kind of physician I need and it tells me when an hour is now bookable.

## PROBLEM:
	It takes so much to find an appointment to a doctor at bupa's medical center. All the doctors has 
	full agendas and it is almost impossible to find an appointment days prior the day I'm looking.

## INSIGHTS:
	Bupa's appointments website it is kinda bad, and I can exploit it in order to be asking at all times 
	when it is the next appointment. Usually we can do this by hand but the process is very slow. Put your
	Rut, the kind of medical insurance you have and so on, until we navigate to the appointments page. 
	
	That queries are made to a public api with almost no security, so I think I can bypass the system 
	to query the appointments endpoint and make a cron to be constantly looking for new spaces on any doctor's
	agenda.

## PROBLEMS:
	- They could ban my Ip.
	- Is it really legal?

## SOLUTION:
	A python script that asks to the endpoint constantly and sends an email when a new appointment it's
	available.

## REQUIREMENTS
 - Create a results folder (or change the destination on get_appointments.py)
 - Python 3
 - Requests library
 - Docker (optional)

## HOW TO USE
    Right now (01/04/2023) the get_appointments.py gets a token and then queries all medical centers looking for
    appointments of the speciality you need and then stores the result of each medical center on the results folder.

    You just need to find the _id of the speciality you need, paste it on "Especialidad" and after, paste the id on "Categoria". You can find this data on the "especialidades.py" file.

    Finally, you just run the get_appointments.py


