# Flight Simulation of Drones in Closed Environment

## Introduction:
The popularization of the drone in recent years has led people to use drones for filming entertainment on the internet, however, the use of these Unmanned Aerial Vehicles (UAVs), goes beyond entertainment, the study on the coordinated control of the flight of Drones recently gained strength, being very useful in civil applications, surveillance, mapping and monitoring areas.
The leader-follower method of forming UAVs carried out in a fixed inertial system in closed environments, aims to create trajectories in real time, these trajectories can be described manually after the drones finish their current actions, or through a script pre-defined, which were perfected and developed during the period of this project. Also during this period, studies on the UAVs formation methods, persecution methods and simulation algorithms previously developed were necessary, involving quadrirotor drones.

## Description
The work developed, aims to use the algorithm with a drone flight script, previously simulated. This work uses the algorithms created by the student Amador Marcelino de Souza Neto, in his report "Flight of Quadrotours in Leader-Follower Formation", they were modified, maintaining only the original basis of the persecution method, the objective of this work being, the continuity and application of drone flight indoors.
In the simulations, the other drones follow a specific leader drone that receives the instructions, the change in the simulations has the objective of applying the drone flight in a closed environment of a greenhouse, for that I set up an environment in the gazebo simulation platform and i created a Flight Route.

## Quadrirotors
A quadrirotor is a drone composed of four propellers in the shape of a cross. In this way the vehicle remains stable with a balance of angular moments, with one pair of propellers rotating clockwise and the other pair rotating counterclockwise.
Quadrirotors are able to move in a linear fashion with ease, and the speed difference in the propellers can define where the drone will be directed, if all rotate fast, the drone goes up, if it goes slower it goes down, if one of the pairs rotates slower that the other the drone turns to one side or the other, among other movements.

## Persecution Method
The persecution method used in this simulation is the Global Fixed Difference (DGF) method, one of the simplest persecution methods, it consists of defining a single drone that will receive a system of X, Y and Z coordinates, these coordinates accessed by a or more drones, but only one of them will take the coordinates, the others will also receive small changes in X, Y and / or Z, so that the drones do not overlap.
All movements that the main drone (the one with coordinates in the script) receives the other drones will also receive, as soon as they perform movements similar to the main drone, they always stop with the same distance from the main drone that was stipulated 
initially.
The DGF method follows the following algorithm:
- 1. The relative position of the follower in relation to the leader is defined before the chase occurs (the vector d = (x, y, z) is defined);
- 2. Leader position PL = (XL, YL, ZL) is received by the follower;
- 3. The objective position of the PO follower receives PL + d = (XL + x, YL + y, ZL + z);
- 4. The objective PO position is transferred to the UAV control;
- 5. Steps ii through iv are repeated in a loop.

## Dependencies:
 - *ROS & Gazebo*

In the simulation, the ROS (Robotic Operating System) is used to create nodes and communication topics between the algorithms written in Python and Gazebo. Gazebo is a 3D simulation platform, with the ability to simulate robots in different environments, it is possible to build environments such as streets, tracks, rooms, among other environments, in addition to being able to manipulate different types of robots in these environments.
The communication between the parties is done via the Linux terminal, where the integration of ros and gazebo is done, through the “gazebo_ros_pkgs” packages, in the terminal  where we start the gazebo, we call the algorithms that create the communication bridge between the drones on the scene and also we started the flight plan.

## Flight Location:
For this project, as the objective is this simulation in an environment, the Estufa environment was created, inspired by a real greenhouse, greenhouse has the proportions 30m x 30m, has 3 divisions of 10m x 30m, the drones fly over pots with 1 meter wide, 1 meter length and 60 depth deep, arranged at a distance of 40 meters per row.

## Flight Path:
The Roteiro Script, has an essential role in this project, through it the user does not need to inserted the coordinates step by step, before it was necessary to wait for the drone to finish an action, to be inserted a new objective coordinate, with the Roteiro, the coordinates will be automatically sent and updated.
This is the path of the leading drone, which is the one that will constantly communicate with the Roteiro, the drone is initially resting at position X = 8.05 Y = 0 and Z = 0.81, it will rise to a height of 2 meters, it will fly over 26 meters ahead, so together with the follower they will have flown over all the elements of the 1st division of the greenhouse, after that they will fly over 10 meters to the left, 26 meters backwards, they will have already flown over the elements of the 2nd division , to map the rest, remembering that it is a closed place, the drone will advance 26 meters forward, 10 meters to the left and 26 meters backwards in this way, mapping the 3rd and last division of the greenhouse, the drones will descend at the height of the lower base of the 3rd greenhouse division and rest with the coordinates of the leader being X = -11.95, Y = 0 and Z = 0.81.

## Results:
https://www.youtube.com/watch?v=UQhVMauFclg (video in Portuguese-Br)
