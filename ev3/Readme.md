# This is Tar file consists of ev3dev/debian-stretch-armel-cross with ros installed on it using docker


# process

GET AND RUN DOCKER IMAGE

$ docker pull ev3dev/debian-stretch-armel-cross
$ docker tag ev3dev/debian-stretch-armel-cross ev3-stretch
$ docker run --rm -it -v /mnt/catkin_ws/:/home/compiler/catkin_ws -w /home/compiler/catkin_ws ev3-stretch


then follow this


Install ros_comm:

sudo apt-get update
sudo apt-get install build-essential

Install the ROS system dependencies using apt-get install.
I've added them in list so that they can be updated and maintained easily.

sudo wget https://raw.githubusercontent.com/moriarty/ros-ev3/master/ros-dependencies.debs
sudo bash ros-dependencies.debs

    Next install the some python packages available through pip

sudo pip install -U rosdep rosinstall_generator wstool rosinstall catkin_pkg rospkg

    sbcl needs to be downloaded, there is a armel binary available for 1.2.7
    http://www.sbcl.org/platform-table.html
    Downlad, unpack it, change to the directory and run the install script:

sudo wget http://netcologne.dl.sourceforge.net/project/sbcl/sbcl/1.2.7/sbcl-1.2.7-armel-linux-binary.tar.bz2
sudo tar -xjf sbcl-1.2.7-armel-linux-binary.tar.bz2
cd sbcl-1.2.7-armel-linux
sudo INSTALL_ROOT=/usr/local sh install.sh
cd ..

Initialize rosdep:

rosdep init

    Debian jessie is not officially supported by ROS, so we need to change where it will look for some packages
    Open the 20-default.list file:

sudo nano /etc/ros/rosdep/sources.list.d/20-default.list

Add the following line to the beginning, in the os-specific listing section.

# os-specific listings first
yaml https://raw.githubusercontent.com/moriarty/ros-ev3/master/ev3dev.yaml

update rosdep.

sudo rosdep update

    I created and changed to a new directory ros_comm, just to keep things organized.
    Then create the rosinstall file, initialize the ros workspace, and check the ros dependencies are all met. Note: only ros_comm and common_msgs will be installed, if you need more, add them to rosinstall_generator command.

mkdir ros_comm && cd ros_comm
rosinstall_generator ros_comm common_msgs --rosdistro kinetic --deps --wet-only --tar > kinetic-ros_comm-wet.rosinstall
wstool init src kinetic-ros_comm-wet.rosinstall
rosdep install --from-paths src --ignore-src --rosdistro kinetic -y --os=debian:jessie

    It's time to install ros using catkin_make_isolated.

./src/catkin/bin/catkin_make_isolated --install --install-space /opt/ros/kinetic -DCMAKE_BUILD_TYPE=Release

This step might take a while.

    Exit the brickstrap shell and create a tar of the brickstrap rootfs and a disk image from the tar. The python bindings for ev3dev are available by default.

then install brick strap and create tar and image file 


brickstrap create-tar
brickstrap create-image


#  This process might work or not its still in progreaa



