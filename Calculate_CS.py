"""A Simple Python calculator, to calculate a host's cs & a player's boosted level in Payday 2"""

def Calculate_Players_Boosted_CS(host_cs_lvl:int|None=None,player_cs_lvl:int|None=None,cs_mission:int|None=None):
    if host_cs_lvl is None:
        host_cs_lvl:int= int(input("What is the host's level Crime Spree?\n> ").strip().replace(",",""))
    if player_cs_lvl is None:
        player_cs_lvl:int= int(input("What is the player's level Crime Spree?\n> ").strip().replace(",",""))
    if cs_mission is None:
        cs_mission:int= int((input("What is the crimespree modifier bonus?\n> ")).strip().replace(",",""))
    
    if host_cs_lvl<0: host_cs_lvl=0
    if player_cs_lvl<0: player_cs_lvl=0
    if cs_mission<3: cs_mission=3
    elif cs_mission>15: cs_mission=15

    # Inserts commas every third placement on the left strarting from the decimal point
    formatted_int:str= lambda result_format_request: (format(result_format_request,',d'))

    results:int= round((host_cs_lvl-player_cs_lvl)*(3.5+float(f'0.0{cs_mission}'))/100)
    formatted_result:str= formatted_int(results)

    host_cs_lvl:int= host_cs_lvl+cs_mission
    formatted_host_cs_lvl:str= formatted_int(host_cs_lvl)

    print(f"Host's New Level: {formatted_host_cs_lvl}")
    print(f"Player Resulting Boosted Level: {formatted_result}")
    return {"host lvl":host_cs_lvl,"player lvl":results}
def run_again()->bool:# User input y/n=True/False
    q:str= input("Would you like to run this again? (y/n)\n> ").strip().lower()
    q2:str= input("Would you like to reuse the old results?(y/n)\n> ").strip().lower()

    if q.startswith('y') and len(q)<4 and len(q)>0: q='y'
    else: SystemExit(0) # Close Successfully

    if q2.startswith('y') and len(q2)<4 and len(q2)>0: q2='y'
    else: q2='n'

    return True if q2=='y' else False

placeholder:dict=Calculate_Players_Boosted_CS()
print()

while True:
    results=placeholder
    match run_again():
        case True: placeholder=Calculate_Players_Boosted_CS(host_cs_lvl=results.get('host lvl',None))
        case False: placeholder=Calculate_Players_Boosted_CS()
    print()