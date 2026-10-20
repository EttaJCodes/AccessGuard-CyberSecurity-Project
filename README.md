# 🔐 AccessGuard — Cybersecurity Event Monitoring System

**Python | Cybersecurity | Windows Security Events | Threat Detection**

## 📌 Project Overview

AccessGuard is a Python-based cybersecurity portfolio project that simulates Windows authentication events, analyzes login activity, and identifies potentially suspicious behavior.

The project demonstrates foundational skills in Python programming, security event analysis, detection logic, and technical troubleshooting.

**Status:** In Development — Lessons 1–3 Completed

## 🛡️ Current Features

- Simulates failed login attempts using Python variables.
- Uses conditional statements to trigger basic security alerts.
- Analyzes simulated Windows Event IDs 4624 and 4625.
- Automatically counts successful and failed events from a Python list.
- Displays security analysis results in the terminal.
- Demonstrates basic Python debugging and testing.

## 🔍 Windows Security Event IDs

| Event ID | Description |
| --- | --- |
| 4624 | Successful Windows logon |
| 4625 | Failed Windows logon |

AccessGuard currently uses simulated events. It does not collect live Windows Event Logs.

## 🛠️ Technologies Used

- **Python 3** — Programming and security analysis
- **Visual Studio Code** — Code development
- **Windows PowerShell** — Program execution and testing
- **Git** — Version control
- **GitHub** — Source code hosting and documentation

## 🚀 Installation and Usage

1. Install Python 3.
2. Download this repository or clone it with Git.
3. Open the project folder in Visual Studio Code.
4. Open a terminal in the project directory.
5. Run the following command:

python main.py

If Windows does not recognize the python command, try:

py main.py

### Example Output

Welcome to AccessGuard!
Security Monitoring System
--------------------------
Failed login attempts: 3
Login activity is normal.
Windows Security Event Analysis
Failed logins: 5
Successful logins: 1

The first detection example uses a manually entered count. The second analyzes a simulated list of Windows Event IDs. Automated alerting based on the event list is planned for Lesson 4.

## 📈 Development Progress

- [x] Lesson 1 — Python setup and program execution
- [x] Lesson 2 — Basic failed-login detection
- [x] Lesson 3 — Windows security event analysis
- [ ] Lesson 4 — Automated alerts from security event counts
- [ ] Lesson 5 — Username and IP address investigation
- [ ] Analyze structured security log files
- [ ] Integrate SQL for security event storage
- [ ] Develop a security monitoring dashboard
- [ ] Add automated tests and investigation reports

## 💡 Skills Demonstrated

- Python programming fundamentals
- Conditional logic and event counting
- Windows authentication event identification
- Security monitoring fundamentals
- Basic security alert development
- Debugging and technical troubleshooting
- Git and GitHub version control

## 🎯 Future Development

Future versions of AccessGuard will aim to:

- Associate login events with usernames and source IP addresses.
- Analyze event timestamps and suspicious login sequences.
- Store and investigate events using SQL.
- Generate investigation-friendly alerts and reports.
- Provide an interactive security monitoring dashboard.

**Long-term goal:** Build a portfolio-ready security monitoring application suitable for demonstrating entry-level cybersecurity and application support skills.

## ⚠️ Disclaimer

AccessGuard is an educational project. All current security events are simulated. The application is not connected to live systems and should not be used for production threat detection. The five-failure threshold is an example training rule, not proof of an attack.

## 👩🏽‍💻 Developer

**Etta J**

Computer Science Graduate | Aspiring Cybersecurity Professional

**GitHub:** https://github.com/EttaJCodes

*Building practical cybersecurity skills, one project and one commit at a time.*

GitHub: https://github.com/EttaJCodes

Building practical cybersecurity skills, one project and one commit at a time.

