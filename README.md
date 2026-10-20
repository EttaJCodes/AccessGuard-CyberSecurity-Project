🔐 AccessGuard Cybersecurity Event Monitoring System
Python | Cybersecurity | Security Event Analysis | Threat Detection

Project Overview
AccessGuard is a Python-based cybersecurity learning project designed to simulate Windows security events, analyze login activity, and identify potentially suspicious behavior.

The goal is to develop practical skills in cybersecurity monitoring, Python programming, security event analysis, and incident investigation.

This project is being developed incrementally, with new functionality added and documented throughout the development process.

Project Status: In Development — Lessons 1–3 Completed

Current Features
Simulates failed login attempts using Python variables.
Generates a basic security alert when failed login attempts meet a configurable threshold.
Simulates Windows Security Event IDs 4624 and 4625.
Counts successful and failed login events automatically from a Python list.
Displays security analysis results in the terminal.
Demonstrates Python conditional statements, variables, lists, and event counting.
Windows Security Events
Event ID

Description

4624

Successful Windows logon

4625

Failed Windows logon

These events are commonly examined during authentication-related security investigations.

AccessGuard currently uses simulated event IDs rather than collecting live Windows Event Logs.

Technologies Used
Python 3 — Core programming language
Visual Studio Code — Development environment
Git — Version control
GitHub — Project hosting and documentation
Windows PowerShell — Running and testing Python scripts
How to Run AccessGuard
Install Python 3.
Download or clone this repository.
Open the project folder in Visual Studio Code.
Open a terminal in the project directory.
Run python main.py.
On some Windows systems, use py main.py instead.

The program displays simulated login results and security analysis information in the terminal.

Development Progress
☑ Lesson 1: Python setup and program execution
☑ Lesson 2: Basic failed-login detection
☑ Lesson 3: Windows security event analysis
☐ Lesson 4: Automated security alerts based on event counts
☐ Lesson 5: Username and IP address investigation
☐ Add security log file analysis
☐ Integrate SQL for security event storage
☐ Develop a security monitoring dashboard
☐ Add automated tests and investigation reports
Skills Demonstrated
This project develops practical experience in:

Python programming and debugging
Cybersecurity fundamentals
Windows authentication event identification
Security monitoring concepts
Basic detection-rule development
Technical troubleshooting
Git and GitHub version control
Future Development
Future versions of AccessGuard will aim to analyze structured login records, associate suspicious activity with accounts and source IP addresses, identify patterns across timestamps, and provide investigation-friendly reports.

The long-term goal is to develop a portfolio-ready security monitoring application.

Disclaimer
AccessGuard is an educational cybersecurity project. All current login events are simulated. The application is not currently connected to live security systems and should not be relied upon for production threat detection.

Developer
Etta J

Computer Science Graduate | Aspiring Cybersecurity Professional

GitHub: https://github.com/EttaJCodes

Building practical cybersecurity skills, one project and one commit at a time.

