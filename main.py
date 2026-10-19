# AccessGuard Cybersecurity Project
# Security Event Monitoring System

print("Welcome to AccessGuard!")
print("Security Monitoring System")
print("--------------------------")
# Simulated failed login attempts
failed_logins = 3

print("Failed login attempts:", failed_logins)

# Check for suspicious login activity
if failed_logins >= 5:
   print("SECURITY ALERT: Suspicious login activity!")
else:
   print("Login activity is normal.")

   # Lesson 3: Windows Security Event Analysis

security_events = [4625, 4625, 4624, 4625, 4625, 4625]

failed_events = security_events.count(4625)
successful_events = security_events.count(4624)

print("Windows Security Event Analysis")
print("Failed logins:", failed_events)
print("Successful logins:", successful_events)
