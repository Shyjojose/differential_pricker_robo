# Differential picker robot 
  ## prerequisite
    world file is house.launch you get it by installing the turtlebot3_simulation.git
    click ctrl+shift+v to render Readme.md

![alt text](screnshot/screen1.png)

    $ cd ~/catkin_ws/src/
    $ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
    $ cd ~/catkin_ws && catkin_make

## launching riviz for map making 

    $ roslaunch finaldesign_description  gazebo.launch

![alt text](screnshot/SCREEN2.png)

    $ roslaunch finaldesign_description  slam.launch

! need to add displays in the riviz tool 

![alt text](screnshot/screen3.png)

click add-> By display type> RobotModel <br>
click add-> by topic -> map <br>
click add-> by topic -> LaserSCan <br>

    $ roslaunch finaldesign_description keyboard.launch

## run robot to make map and save it use below code 

    $ rosrun map_server map_saver -f ~/map

## for navigation run gazebo.launch then navigation.launch in different terminal 

    $ roslaunch finaldesign_description  gazebo.launch
    $ roslaunch finaldesign_description navigation.launch map_file:=$HOME/map.yaml

 ## need to add the displays for the riviz tool
![alt text](screnshot/screen4.png)

click add-> By display type> RobotModel <br>
click add-> by topic -> map <br>
click add-> by topic -> LaserSCan <br>
click add-> by topic -> /global_costmap ->/costmap-> map <br>
click add-> by topic -> /local_costmap ->/costmap-> map <br>
click add-> by topic -> LaserSCan <br>
click add-> by topic -> /NavfnROs ->/plan ->path <br>
set the 2d post estimate and also give final 2d navigaton goal <br>


 # moveit_arm movement





