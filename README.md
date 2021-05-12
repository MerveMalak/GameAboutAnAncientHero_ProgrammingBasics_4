# CENG113-PROGRAMMING BASICS
# ASSINGMENT4-GameAboutAnAncientHero_ProgrammingBasics_4

You are expected to write a Python program for a game about an ancient hero that is half-god. In order to become immortal, he is challenged to complete 5 tasks.
world.
At the beginning of the game, the hero starts his journey from his home. He also has a pegasus companion with whom he can travel to the given task’s destinations.
In the given TaskList.txt, you can find each task’s distance from his home by foot,by pegasus and the needed HP to kill the monster of the task. 

You have to read TaskList.txt, and create a nested list named task_list that has each task as a list:

task_list = [[Task1,-1,400,50],[Task2,-1,500,100]....]

As you can see from the TaskList file, if there is no route to go to the given task by foot, the distance is given as -1. Therefore, you have to use Pegasus in order to reach these destinations. In the beginning of the game, the hero has 3000HP, while the pegasus has 550HP. The hero can walk at the speed of 20km/hour . The pegasus can fly at the speed of 50km/hour. For each hour of the journey, the hero loses 10HP, while the pegasus loses 15HP . At the end of each task, the hero must return to his home and continue from there.
After completing each task, the program should remove that task from the task list. At each turn, the program should display the remaining tasks and their distances from the hero’s home, and ask for the hero’s next move.

★ You should write remove_task(task_list) and print_remaining_tasks(task_list) in a recursive manner.

The program finishes when there is no task left (“ Congratulations, you have completed the task. ” message is printed) , or the HP of the hero is not enough to kill the monster of the task or the HP of the hero and pegasus is not enough to travel to the given destination (“ Game Over ” is printed). If the user succeeds the game, you have to ask his/her name and save the user’s name with the time the game took to finish. Also, you have to show the Hall of Fame at the end of each successful game which shows the best 3 results so far.

★ Details are shown in HW4.pdf file!
