Home Intrusion Detection System
Arpita Das1, Rimi Sengupta1, Saptarshi Mukherjee*1, Ankita Saha1, Debanjana Das1

1Department of Electronics & Communication Engineering, University of Engineering & Management, Kolkata, University Area, Plot No. III – B/5, New Town, Action Area – III, Kolkata – 700160
* Corresponding author
E-mail id of corresponding author: saptarshi03official@gmail.com

Abstract:
Concerns regarding the safety and security of residential settings have grown in recent years as a result of an increase in home invasion incidences. The installation of strong security systems, such as Home Intrusion Detection Systems, has become crucial to combating this expanding threat. The aim of this project is to use an ultrasonic sensor to create a radar system which we will use to sense unauthorized access into our homes. With the help of MQTT we will receive messages from MQTT broker and we as a subscriber if there’s any intruders breaking into the premises exceeding a certain threshold within a certain distance from the setup an alarm with the help buzzer will go live and with the help of SMTP and simple python scripts a picture of the intruder will be taken through webcam and sent to predefined mail ID and if there’s not an intruder the radar system will keep sweeping. When we send messages to MQTT broker and finally to the python application ensuring no intruders are present and if it's only (us authenticated using MQTT messages) it makes the Arduino trigger a relay which in turn turns on desired home appliances.
Keywords: Radar System, Ultrasonic Sensors, Servo Motor, Arduino, MQTT, SMTP, Intrusion Detection


    1. INTRODUCTION

The security of our homes and the protection of our loved ones and belongings are of paramount importance. With the increasing instances of home invasions and burglaries, it has become crucial to implement effective security measures that can detect and deter unauthorized access. This is where Home Intrusion Detection Systems come into play. A Home Intrusion Detection System [1-4] is a comprehensive security solution designed specifically for residential environments. It combines various sensors, surveillance cameras, and intelligent algorithms to detect and respond to potential intrusions in real-time. The primary goal is to provide homeowners with early warning signs of unauthorized entry attempts, allowing them to take immediate action and minimize the risk of loss or harm. Advanced sensors can detect suspicious activities such as unauthorized entry attempts, broken windows, or unusual movements within the property. Once an anomaly is detected, the system can immediately send notifications to the homeowners' smartphones or other connected devices, allowing them to assess the situation and take appropriate action, such as contacting the authorities or activating security measures. A Home Intrusion Detection System is essential for its ability to improve the security and safety of domestic surroundings. Installing
security cameras, motion sensors, and alarm systems provide a clear message that the property is secure and monitored, discouraging unauthorized access. It provides early warning signs of potential intrusions, enabling homeowners to take immediate action. With the help of machine learning real-time notifications and alerts are sent to homeowners, allowing them to assess the situation and contact authorities promptly and minimize potential damages. This also offers peace of mind by allowing homeowners to keep an eye on their properties, check the status of security devices, and ensure the safety of their loved ones and belongings from anywhere at any time. Home Intrusion Detection System may be effortlessly linked with smart home automation systems, increasing the ease and efficiency with which home security is managed. Integration with smart locks, security lighting, and other devices enables homeowners to operate and monitor their security systems from a single interface, resulting in a comprehensive and linked security environment. The methodology along with the circuit diagram and results is discussed in the following sections of the paper.

    2. METHODOLOGY

The idea behind the proposed work is to use ultrasonic sensors to create a radar system which we will use to sense unauthorized access into our homes. With the help of MQTT [paho.mqtt 1.6.1] we will receive messages from MQTT broker and we as a subscriber if there’s any intruders breaking into the premises exceeding a certain threshold within a certain distance from the setup an alarm with the help buzzer will go live and with the help of SMTP and simple python scripts a picture of the intruder will be taken through webcam and sent to predefined mail ID and if there’s not an intruder the radar system will keep sweeping. For the proposed work, the hardware components used are Arduino Uno [5], Ultrasonic sensor [6], servo motor [7], touch sensor (TTP233B) [8], buzzer, LED and relay and software used Arduino IDE, Python, MQTT, SMTP, OpenCV [opencv-python(4.7.0.72)].
Circuit Diagram:
![image](https://github.com/sap03rocks/Home-Intrution-Detection-System/assets/100368245/ebf8cbd9-0613-4137-a50b-16f4a8626e28)


Figure 1: circuit diagram of our proposed solution using Fritzing Software
Algorithm:

Figure 2: An algorithmic chart of our proposed solution

By using the start button which is a TTP223B touch sensor we first initialize the radar system consisting of a servo motor and ultrasonic sensor which checks if the threshold value of the ultrasonic sensor corresponds to 40 cm or not. If an object is detected which is breaching less than 40 cm threshold placed, it communicates with the user via serial reading from arduino to MQTT messaging platform. It listens to users reply to confirm if it's an intruder or the user itself. If it's the user they can confirm the same and can use the setup as a home automation setup by turning on or off the appliances. On the other hand if the user confirms that it's an intruder the setup can ring an alarm using buzzer and LED and also take an image of the intruder using openCV package and send it via SMTP to the user mail ID. This alarm continues until users confirmation is received.


    3. RESULTS


Figure 3: Our Experimental Setup


Figure 4: All Readings from the Ultrasonic Sensor Received by Python Script.




Figure 5: MQTT Dashboard with 2 publish topics one for sending messages from the apparatus and one to receive then command


Figure 6: SMTP message from the setup about intruder (automated)



    4. CONCLUSION:

Home Intrusion Detection Systems has grown as an important component in protecting residential surroundings from unauthorized access and invasions. This provides early detection, real-time warning, and proactive security measures by integrating modern sensors, surveillance cameras, and intelligent algorithms. The importance of this rests in their capacity to dissuade prospective attackers, provide peace of mind to homeowners, and enable fast reaction to any security risks. Homeowners can improve the security of their houses and protect their loved ones and belongings by installing Home Intrusion Detection Systems. The multi-layered defense mechanisms provided by this, combined with integration with smart home automation systems, form a comprehensive security ecosystem that strengthens the total property defense. Homeowners can keep an eye on their properties and respond quickly even while they are away thanks to real-time monitoring and remote access features.
REFERENCE

    1. Yang, J., & Sun, L. (2022). A Comprehensive Survey of Security Issues of Smart Home System:“Spear” and “Shields”, Theory and Practice. IEEE Access.
    2. Baich, M., Hamim, T., Sael, N., &Chemlal, Y. (2022). Machine Learning for IoT based networks intrusion detection: a comparative study. Procedia Computer Science, 215, 742-751.
    3. Batalla, J. M., Vasilakos, A., &Gajewski, M. (2017). Secure smart homes: Opportunities and challenges. ACM Computing Surveys (CSUR), 50(5), 1-32.
    4. Alghayadh, F., &Debnath, D. (2021). A hybrid intrusion detection system for smart home security based on machine learning and user behavior. Advances in Internet of Things, 11(1), 10-25.
    5. https://docs.arduino.cc/hardware/uno-rev3
    6. https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf
    7. https://www.towerpro.com.tw/product/sg90-7
    8. https://files.seeedstudio.com/wiki/Grove-Touch_Sensor/res/TTP223.pdf


























