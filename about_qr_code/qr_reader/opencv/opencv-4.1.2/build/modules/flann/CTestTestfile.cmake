# CMake generated Testfile for 
# Source directory: /home/pi/opencv/opencv-4.1.2/modules/flann
# Build directory: /home/pi/opencv/opencv-4.1.2/build/modules/flann
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_flann "/home/pi/opencv/opencv-4.1.2/build/bin/opencv_test_flann" "--gtest_output=xml:opencv_test_flann.xml")
set_tests_properties(opencv_test_flann PROPERTIES  LABELS "Main;opencv_flann;Accuracy" WORKING_DIRECTORY "/home/pi/opencv/opencv-4.1.2/build/test-reports/accuracy")
