sudo apt-get update
sudo apt-get upgrade

sudo apt-get remove x264 libx264-dev

# Ubuntu commands for OpenCV dependency installation
sudo apt-get install --assume-yes build-essential checkinstall cmake pkg-config yasm
sudo apt-get install -y git gfortran
sudo apt-get install -y libjpeg8-dev libjasper-dev libpng12-dev

# If you are using Ubuntu 16.04
sudo apt-get install -y libtiff5-dev
 
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
sudo apt-get install -y libxine2-dev libv4l-dev
sudo apt-get install -y libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install -y qt5-default libgtk2.0-dev libtbb-dev
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libfaac-dev libmp3lame-dev libtheora-dev
sudo apt-get install -y libvorbis-dev libxvidcore-dev
sudo apt-get install -y libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install -y x264 v4l-utils
 
# Optional dependencies
sudo apt-get install -y libprotobuf-dev protobuf-compiler
sudo apt-get install -y libgoogle-glog-dev libgflags-dev
sudo apt-get install -y libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

# Install python dependencies
sudo apt-get install python-dev python-pip python3-dev python3-pip
sudo -H pip2 install -U pip numpy
sudo -H pip3 install -U pip numpy


cd ~/

git clone https://github.com/opencv/opencv.git
cd opencv 
git checkout 3.3.1 
cd ..

git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout 3.3.1
cd ..


cd opencv
mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D WITH_TBB=ON \
      -D WITH_V4L=ON \
      -D WITH_QT=ON \
      -D WITH_OPENGL=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..


# find out number of CPU cores in your machine
nproc
# substitute 1 by output of nproc
make -j1
sudo make install
sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig

find /usr/local/lib/ -type f -name "cv2*.so"


