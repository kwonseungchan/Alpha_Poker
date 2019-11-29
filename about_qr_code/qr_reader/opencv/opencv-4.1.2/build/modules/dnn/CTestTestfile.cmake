# CMake generated Testfile for 
# Source directory: /home/pi/opencv/opencv-4.1.2/modules/dnn
# Build directory: /home/pi/opencv/opencv-4.1.2/build/modules/dnn
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_dnn "/home/pi/opencv/opencv-4.1.2/build/bin/opencv_test_dnn" "--gtest_output=xml:opencv_test_dnn.xml")
set_tests_properties(opencv_test_dnn PROPERTIES  LABELS "Main;opencv_dnn;Accuracy" WORKING_DIRECTORY "/home/pi/opencv/opencv-4.1.2/build/test-reports/accuracy")
add_test(opencv_perf_dnn "/home/pi/opencv/opencv-4.1.2/build/bin/opencv_perf_dnn" "--gtest_output=xml:opencv_perf_dnn.xml")
set_tests_properties(opencv_perf_dnn PROPERTIES  LABELS "Main;opencv_dnn;Performance" WORKING_DIRECTORY "/home/pi/opencv/opencv-4.1.2/build/test-reports/performance")
add_test(opencv_sanity_dnn "/home/pi/opencv/opencv-4.1.2/build/bin/opencv_perf_dnn" "--gtest_output=xml:opencv_perf_dnn.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_dnn PROPERTIES  LABELS "Main;opencv_dnn;Sanity" WORKING_DIRECTORY "/home/pi/opencv/opencv-4.1.2/build/test-reports/sanity")
