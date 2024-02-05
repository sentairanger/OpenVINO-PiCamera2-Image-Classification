# OpenVINO-PiCamera2-Image-Classification

## Introduction

This project takes images using a Pi Camera with the `picamera2` module. The images are then classified using OpenVINO and the Intel NCS2. 

## Getting Started

As of now, this works on Raspberry Pi OS Bullseye 64 Bit but I will test on Bookworm to see if it works. All you need is to have Raspberry Pi OS Bullseye running on your Pi and install OpenVINO using [this](https://gist.github.com/sentairanger/caf11a2432ceebd715c6b33c224f4960) gist provided. I made updates since the original installation method had errors. Once you have OpenVINO installed and the NCS2 is working properly be sure to run the sample inference code as shown in the installation guide. Also, be sure to reference your user name when running the code. For example, if your username is `pi` then be sure to replace `<user-name>` with `pi`. This will only work in the terminal so make sure to run the code with `python3 button-classification.py`. Press the first button to take the image and the second to classify the image.
