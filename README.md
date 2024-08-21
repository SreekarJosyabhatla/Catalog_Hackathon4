# Catalog_Hackathon4
# Three-Level Password System

## Overview

The Three-Level Password System is a security model intended for performing enhanced authentication by prompting users to enter three levels of passwords. This method is more secure since it verifies various implementation techniques, making unauthorized access harder. It includes session management, rate limiting and logging to model your real-world security practices.

## Features

- **Multi-Level Authentication**: All users have to put… — 3 different passwords.
- **Rate Limiting**: Limits the amount of attempts that can be made per minute so it's harder to perform brute-forcing.
- **Session Management**:  Stores active sessions for logged in users to allow secure logins and logs out.
- **Logging**: Logs all authentication attempts, successful logins, failed attempts and session terminations.

## File Structure

```plaintext
ThreeLevelPasswordSystem/
│
├── authentication.log
├── three_level_auth.py         
```
### 1)Registration:
Users can Registers New users With Unique user and Three Levels of Password
Passwords are stored as plain hashes for yet an extra layer of security.

### 2)Authentication:
The authentication is via user ID combined with all three passwords.
If it matches the credentials, then the Session will be created, and the user will be allowed to log in.

### 3)Session Management:
The user is authenticated, and a session is created, which logs the user in.
Users can log out to destroy that session.
### 4)Rate Limiting:
The system restricts the number of authentication trials within a certain period to mitigate brute-force attempts.
If the requests exceed this limit, it will block anything from that user for a while.

### 5)Logging:
The system logs all actions (registrations, successful/failed logins, session creation, and termination) with timestamps in authentication.log.

