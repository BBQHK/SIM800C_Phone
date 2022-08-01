# SIM800C_Phone
Make the computer become a phone using ATK-SIM800C + Audio Repeater

## Hardware connection setup
Please follow the illustration below to connect SIM800C to the computer.

<img width="1000" alt="image" src="https://user-images.githubusercontent.com/43085343/182063712-eaf90801-f020-447b-a342-51268ef627e2.png">

If you want to learn more about SIM800C, please find the usage document of SIM800C from internet.

## Software setup
### Step 1: Setup two virtual sound cables
Please follow the images below to start up two Audio Repeater (MME).

<img width="500" alt="image" src="https://user-images.githubusercontent.com/43085343/182063963-7e44e5e4-94d1-4d3d-9871-22aa9739d0c2.png">
Please run two Audio Repeater (MME) as administrator.

<img width="700" alt="image" src="https://user-images.githubusercontent.com/43085343/182064036-4db102a7-7605-4eb5-a425-51cb26336cf1.png">

Please select “Wave in” and “Wave out” of 2 Audio Repeater by following below:
|       | Wave in | Wave out |
| :-----| :----: | :----: |
| Audio Repeater 1 | Front panel audio input | USB sound card audio output |
| Audio Repeater 2 | USB sound card audio input | Front panel audio output |

After that, just start it.

### Step 2: Change serial device name of SIM800C (you can find that name using XCOM V2.0 or other serial monitoring tools)

<img width="700" alt="image" src="https://user-images.githubusercontent.com/43085343/182064649-6722a949-b2c5-4289-8b68-a0ecaf1cd669.png">

## Usage
Just run main.py and enjoy.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/43085343/182064732-7002afef-3306-4ff4-88c7-c73aac2f6ee7.png">





