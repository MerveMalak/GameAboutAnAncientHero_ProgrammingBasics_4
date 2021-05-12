#260201043 =====> MY STUDENT ID
def read_file():  # read file and return nested list 
    f = open("TaskList.txt")
    task_list = []
    for task in f:
        if task.startswith("Task"):   #if line does not start with task, line have a hall of fame name. 
            task_info = task.split("\n")[0]
            task_list.append(task_info.split(","))
    for tasks in task_list:
        tasks[1] = int(tasks[1])
        tasks[2] = int(tasks[2])
        tasks[3] = int(tasks[3]) 
    f.close()
    return task_list

def print_remaining_tasks(task_list,controller):
    if len(task_list) == 0:
        print("")
    else:
        task =task_list[0]
        if controller ==True:
            print("Here are the tasks left that hero needs to complete:")
            print("-"*55)
            print("|" + " TaskName" + (" "*3) + "|" + " ByFootDistance" + (" "* 2) + "|" + " ByPegasus" + (" ") + "|" + " HPNeeded" + (" ") + "|")
            print("-"*55)
            controller = False
        if len(task_list) == 1:
            taskname = ("| "+ task[0]).ljust(13)
            byfootdistance = ("| " + str(task[1]) + " km").ljust(18)
            bypegasusdistance = ("| " + str(task[2]) + " km").ljust(12)
            hpneeded = ("| " + str(task[3])).ljust(11)
            print(taskname + byfootdistance + bypegasusdistance + hpneeded + "|")
            print("-"*55)
        else:
            taskname = ("| "+ task[0]).ljust(13)
            byfootdistance = ("| " + str(task[1]) + " km").ljust(18)
            bypegasusdistance = ("| " + str(task[2]) + " km").ljust(12)
            hpneeded = ("| " + str(task[3])).ljust(11)
            print(taskname + byfootdistance + bypegasusdistance + hpneeded + "|")
            print_remaining_tasks(task_list[1:],controller)

def check_destination_and_travel(task_list,destination,hero_hp,pegasus_hp): 
    #check special case 
    for task in task_list:
        if task[0] == destination:
            if task[1] == -1:
                by_foot_needed_hp = -1 
            else:
                by_foot_needed_hp = (task[1]/hero_speed) * hero_lost
            by_pegasus_needed_hp = (task[2]/pegasus_speed)* pegasus_lost
            if task[1] == -1 and (by_pegasus_needed_hp > pegasus_hp):
                # The situation where there is no possibility to walk and the hp of the pegasus is not enough
                return False
            elif (by_foot_needed_hp > hero_hp) and (by_pegasus_needed_hp > pegasus_hp):
                # pegasus and hero do not have enough hp
                return False # game over
            elif (by_pegasus_needed_hp <= pegasus_hp) and  hero_needed_hp(task_list,destination,hero_hp) == False:
                return True
            elif (by_foot_needed_hp > hero_hp) and hero_needed_hp(task_list,destination,hero_hp) == False:
                return False 
            return True

def hero_needed_hp(task_list,destination,hero_hp):
    #check hero has enough hp to defeat the monster
    for task in task_list:
        if task[0] == destination:
            if task[3]  <= hero_hp:
                return True
            else:
                return False

def hero_and_pegasus_needed_hp(task_list,destination, travel_type, hero_hp,pegasus_hp):
    # check travel_type-hp
    for task in task_list:
        if task[0] == destination:
            if travel_type == "foot" and task[1] == -1:   # only pegasus
                print("You cannot go there by foot.")
                return False
            by_foot_needed_hp = (task[1]/hero_speed) * hero_lost
            by_pegasus_needed_hp = (task[2]/pegasus_speed)* pegasus_lost
            if (by_foot_needed_hp > hero_hp) and (by_pegasus_needed_hp > pegasus_hp):
            # pegasus and hero do not have enough hp
                return "gameover" # game over
            elif travel_type == "foot" and (by_foot_needed_hp > hero_hp):
                print("Hero does not have enough HP")
                return False    #ask the travel_type again
            elif travel_type == "pegasus" and (by_pegasus_needed_hp > pegasus_hp):
                print("Pegasus does not have enough HP.")
                return False   #ask the travel_type again
            elif hero_needed_hp(task_list,destination,hero_hp) == False: #if hero has not enough hp then game over
                return "gameover"
            return True

def calculate_hero_or_pegasus_hp(task_list,destination, travel_type, where_hero, total_time, hero_hp, pegasus_hp):
    # calculate to new herohp pegasushp and total time
    for task in task_list:
        if task[0] == destination:
            if travel_type == "foot":
                total_time = total_time + (task[1]/hero_speed)
                by_foot_needed_hp = (task[1]/hero_speed) * hero_lost
                hero_hp -= by_foot_needed_hp
            else:
                total_time = total_time + (task[2]/pegasus_speed)
                by_pegasus_needed_hp = (task[2]/pegasus_speed)* pegasus_lost
                pegasus_hp -= by_pegasus_needed_hp
            if where_hero == "task": 
                print("Hero defeated the monster.")
                hero_hp -= task[3]   # hero lost the HP 
            else:
                print("Hero arrived home.")
            hero_hp,total_time,pegasus_hp = int(hero_hp), int(total_time), int(pegasus_hp)
            print("Time passed :", total_time, "hour")
            return hero_hp,pegasus_hp,total_time

def check_destination(task_list):
    #destination is valid or not valid, valid => return destination, not valid => "game over"
    tasks = []
    for task in task_list:
        tasks.append(task[0])
    while True:
        destination = input("Where should Hero go next? ")
        if destination not in tasks:
            print("Invalid input")
        elif check_destination_and_travel(task_list,destination,hero_hp,pegasus_hp) == False:
            return False 
        else:
            return destination

def print_hp(hero_hp, pegasus_hp):
    print("")
    print("Remaining HP for Hero :", hero_hp)
    print("Remaining HP for Pegasus:", pegasus_hp)
    print("")

def travel_type(task_list,destination,where_hero):
    travels = ["foot", "pegasus"]
    while True:
        if where_hero == "task":
            travel = input("How do you want to travel?(Foot/Pegasus)").lower()
        else:
            travel = input("How do you want to go home?(Foot/Pegasus)").lower()
        if travel not in travels:
            print("Invalid input")
        else:   
            control = hero_and_pegasus_needed_hp(task_list,destination,travel,hero_hp,pegasus_hp)
            if control == "gameover":  # no possibility to win
                return False
            elif control:
                return travel   # hero_and_pegasus_needed_hp is True then travel show to how hero go to destination 
                                # hero_and_pegasus_needed_hp is False then ask again

def remove_task(task_list, task):
    if len(task_list) == 0:
        return []
    else:
        line = task_list[0]
        if line[0] == task:
            task_list.remove(line)
            return remove_task(task_list, task)
        else:
            return [line] + remove_task(task_list[1:], task)

def writing_file(total_time):
    name = input("What is your name : ")
    f = open("TaskList.txt","a+")
    f.seek(0)
    one_list = []
    for line in f:
        one_list.append([line])
    if one_list[-1][0].startswith("Task"):      # if the last line start with Task then we put the "\n" last line  
        f.write("\n")
    f.write(name+","+str(total_time)+"\n")
    f.close()

def reading_hall_of_fame():
    total_times = []
    names = []
    f = open("TaskList.txt")
    for line in f:
        if not line.startswith("Task"):    # if the line start with Task we skip, is not read the name and total time
            line = line[:-1]
            name,total_time = line.split(",")[0], int(line.split(",")[1])
            names.append(name)
            total_times.append(total_time)
    f.close()
    total_times.sort()
    total_times = total_times[:3]
    zip_list = list(zip(names,total_times))
    print("Hall of fame")
    print("-"*35)
    hall_of_fame = ("| " + "Name".ljust(15) + "| " + "Finish Time".ljust(15) + "|")
    print(hall_of_fame)
    print("-"*35)
    for i in total_times:
        for k,v in zip_list:
            if v == i:
                print("| "+ k.ljust(15) + "| " + str(v) + (" hour").ljust(12) +"|")
                print("-"*35)
                zip_list.remove((k,v))
                break

hero_speed = 20
pegasus_speed = 50
hero_lost = 10  
pegasus_lost = 15
hero_hp = 3000
pegasus_hp = 550
total_time = 0

def main():
    flag = False
    global hero_hp
    global pegasus_hp
    global total_time
    task_list = read_file()
    print("Welcome to Hero’s 5 Labors!")
    print_hp(hero_hp,pegasus_hp)
    print_remaining_tasks(task_list,True)
    while  True:
        if len(task_list) == 0:   # if tasks finish and enough hp tehn win 
            print("Congratulations, you have completed the task.")
            flag = True
            break
        destination = check_destination(task_list)  # if no possibility to go to island because of pegasus have not enough hp
        if  destination == False:
            print("Game Over")
            break
        else:
            travel = travel_type(task_list,destination, "task") # if pegasus and hero have not enough hp to go to task
            if travel == False:
                print("Game Over")
                break
            hero_hp,pegasus_hp,total_time = calculate_hero_or_pegasus_hp(task_list,destination,travel,"task",total_time,hero_hp,pegasus_hp)
            if hero_needed_hp(task_list,destination,hero_hp) == False:   #hero go to island but do not have enough HP to defeat the monster
                print("Game Over")
                break          
            if not check_destination_and_travel(task_list, destination,hero_hp,pegasus_hp):
                print("Game Over")              # check special case if it is then game over
                break
            else:
                print_hp(hero_hp,pegasus_hp)    # if it is not print remaining hp of hero and pegasus and continue the game
            travel = travel_type(task_list,destination, "home")
            if travel == False: # if pegasus and hero have not enough hp to return home
                print("Game Over")
                break
            hero_hp,pegasus_hp,total_time = calculate_hero_or_pegasus_hp(task_list,destination,travel,"home",total_time,hero_hp,pegasus_hp)
            print_hp(hero_hp,pegasus_hp)
            task_list = remove_task(task_list,destination)# hero return home and task is finished 
            print_remaining_tasks(task_list,True)
    if flag:  # all tasks are finished you win
        writing_file(total_time)   # name is recorded the TaskList file
        reading_hall_of_fame()          # winners are reading
main()
# I played four times and win TaskList is updated my scores.