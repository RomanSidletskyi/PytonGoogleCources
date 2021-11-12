 Qwiklabs provisions resources backed by Google Cloud that will be used to perform the tasks in the assessments. By using Qwiklabs, you won't have to purchase or install software yourself, and you can use the Linux operating system as if it was installed on your local machine.
 ## Important details:

You will have 90 minutes to complete each lab.

You'll experience a delay as the labs load, as well as for the working instances of Linux VMs. So, please wait a couple of minutes.

Make sure to access labs directly through Coursera and not in the Qwiklabs catalog. If you access labs through the Qwiklabs catalog, you will not receive a grade. (As you know, a passing grade is required to complete the course.)

You'll connect to a new VM for each lab with temporary credentials created for you; these will last only for the duration of the lab.

The grade is calculated when the lab is complete, so be sure to hit "End Lab" when you're done. Note: after you end the lab, you won't be able to access your previous work.

To get familiar with entering labs, find the links below for the operating system of the machine you are currently using for a visualization of the key steps. Note that while video resources linked below do not have a voiceover or any audio, all important details will still be housed in each lab’s set of instructions on the Qwiklabs platform.

If you receive the error "Sorry, your quota has been exceeded for the lab", please submit a request or reach out to the Qwiklabs support team directly via chat support on qwiklabs.com. 

Demo videos for accessing labs:

- [For Windows users](https://www.youtube.com/watch?v=Al1opDxb3ok)

- [For Mac users](https://www.youtube.com/watch?v=76VlwjMYIxg)

- [For Linux users](https://www.youtube.com/watch?v=YtrO8nW0ugM)

- [For Chrome OS users](https://youtu.be/HklttPmGGKc)


# Accessing the virtual machine
Please find one of the three relevant options below based on your device's operating system.

Note: Working with Qwiklabs may be similar to the work you'd perform as an IT Support Specialist; you'll be interfacing with a cutting-edge technology that requires multiple steps to access, and perhaps healthy doses of patience and persistence(!). You'll also be using SSH to enter the labs -- a critical skill in IT Support that you’ll be able to practice through the labs.

## Option 1: Windows Users: Connecting to your VM
In this section, you will use the PuTTY Secure Shell (SSH) client and your VM’s External IP address to connect.

Download your PPK key file

You can download the VM’s private key file in the PuTTY-compatible PPK format from the Qwiklabs Start Lab page. Click on Download PPK.

PPK

Connect to your VM using SSH and PuTTY

You can download Putty from here

In the Host Name (or IP address) box, enter username@external_ip_address.

Note: Replace username and external_ip_address with values provided in the lab.
Putty_1

In the Category list, expand SSH.

Click Auth (don’t expand it).

In the Private key file for authentication box, browse to the PPK file that you downloaded and double-click it.

Click on the Open button.

Note: PPK file is to be imported into PuTTY tool using the Browse option available in it. It should not be opened directly but only to be used in PuTTY.
Putty_2

Click Yes when prompted to allow a first connection to this remote SSH server. Because you are using a key pair for authentication, you will not be prompted for a password.
Common issues

If PuTTY fails to connect to your Linux VM, verify that:

You entered <username>@<external ip address> in PuTTY.

You downloaded the fresh new PPK file for this lab from Qwiklabs.

You are using the downloaded PPK file in PuTTY.

Option 2: OSX and Linux users: Connecting to your VM via SSH
Download your VM’s private key file.

You can download the private key file in PEM format from the Qwiklabs Start Lab page. Click on Download PEM.

PEM

Connect to the VM using the local Terminal application

A terminal is a program which provides a text-based interface for typing commands. Here you will use your terminal as an SSH client to connect with lab provided Linux VM.

Open the Terminal application.

To open the terminal in Linux use the shortcut key Ctrl+Alt+t.

To open terminal in Mac (OSX) enter cmd + space and search for terminal.

Enter the following commands.

Note: Substitute the path/filename for the PEM file you downloaded, username and External IP Address.
You will most likely find the PEM file in Downloads. If you have not changed the download settings of your system, then the path of the PEM key will be ~/Downloads/qwikLABS-XXXXX.pem

``chmod 600 ~/Downloads/qwikLABS-XXXXX.pem``

``ssh -i ~/Downloads/qwikLABS-XXXXX.pem username@External Ip Address``


