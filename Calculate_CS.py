"""A Simple Python calculator, to calculate a host's cs & a player's boosted level in Payday 2"""

def main():
    def Find_CS_Mission(string_value:str)-> int|None:
        cs_map_rotation:dict= {
                "airport": 4,
                "swing vote": 4,
                "the revenge": 4,
                "the yacht heist": 4,
                "bank heist": 5,
                "car shop": 5,
                "fbi server": 5,
                "lab rats": 5,
                "murky station": 5,
                "prison nightmare": 5,
                "shadow raid": 5,
                "transport: crossroads": 5,
                "transport: harbor": 5,
                "transport: park": 5,
                "transport: underpass": 5,
                "truck load": 6,
                "framing": 7,
                "stealing xmas": 7,
                "transport: train heist": 7,
                "white xmas": 7,
                "alaskan deal": 8,
                "brooklyn 10-10": 8,
                "brooklyn bank": 8,
                "four floors": 8,
                "santa's workshop": 8,
                "scarface mansion": 8,
                "the bomb: dockyard": 8,
                "birth of sky": 9,
                "counterfeit": 9,
                "beneath the mountain": 10,
                "first world bank": 10,
                "hotline miami": 10,
                "the breakout": 10,
                "the diamond": 10,
                "the lion's den": 10,
                "undercover": 10,
                "aftershock": 12,
                "green bridge": 12,
                "heat street": 12,
                "panic room": 12,
                "slaughterhouse": 12,
                "cook off": 13,
                "the big bank": 13,
                "engine problem": 14,
                "the search": 15,

                "interception": 0
            }
        map_name:str= " ".join(string_value.strip().lower().replace('the ','').split())
        map_rotation_keys:list= cs_map_rotation.keys()

        found_key:str|None=None
        for key in map_rotation_keys:
            if map_name in key:
                found_key=key
                break

        return cs_map_rotation[found_key] if found_key is not None else None
    def Calculate_Players_Boosted_CS(host_cs_lvl:int|None=None,player_cs_lvl:int|None=None,cs_mission:int|None=None):
        if host_cs_lvl is None: host_cs_lvl:int= int(input("What is the host's level Crime Spree?\n> ").strip().replace(",",""))
        if player_cs_lvl is None: player_cs_lvl:int= int(input("What is the player's level Crime Spree?\n> ").strip().replace(",",""))
        if cs_mission is None:
            while True:
                input_mission:str= str(input("What is the upcoming mission?\n> ")).strip().replace(",","")
                try:
                    cs_mission:int= int(input_mission)
                except Exception:
                    potential_find:int|None= Find_CS_Mission(input_mission)
                    if potential_find is None:
                        print(f"Failed to find {input_mission}! Please try again...")
                        continue
                    else:
                        cs_mission=potential_find
                        break
                        
        
        if host_cs_lvl<0: host_cs_lvl=0
        if player_cs_lvl<0: player_cs_lvl=0
        if cs_mission<3: cs_mission=3
        elif cs_mission>15: cs_mission=15

        # Inserts commas every third placement on the left strarting from the decimal point
        formatted_int:str= lambda result_format_request: (format(result_format_request,',d'))

        results:int= round((host_cs_lvl-player_cs_lvl)*(3.5+float(f'0.0{cs_mission}'))/100) if host_cs_lvl>player_cs_lvl else player_cs_lvl
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
main()
