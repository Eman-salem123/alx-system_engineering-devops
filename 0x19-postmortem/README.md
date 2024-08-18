# Postmortem: Calculator Service Outage

## Issue Summary

**Duration:**  
August 10, 2024, 14:00 UTC - August 10, 2024, 15:30 UTC (1 hour 30 minutes)

**Impact:**  
The Calculator service was unavailable during the outage. Users experienced timeouts and inability to perform basic arithmetic operations via the web application. Approximately 85% of the users were affected, with most experiencing either long delays or complete failure in accessing the service.

**Root Cause:**  
The outage was caused by an unhandled edge case in the service's backend logic, where a division by zero operation triggered an infinite loop. This resulted in the CPU of the server being maxed out, which caused a complete service breakdown.

## Timeline

- **14:00 UTC** - Issue detected via monitoring alert showing 100% CPU utilization on the primary server.
- **14:05 UTC** - Initial investigation begins. Suspected a memory leak or an infinite loop in the recent deployment.
- **14:15 UTC** - A thorough review of the recent code changes showed no obvious issues. Assumed the problem was related to server load and attempted to scale up additional servers.
- **14:30 UTC** - Escalated to the backend engineering team after noticing that scaling had no effect on the issue.
- **14:40 UTC** - Backend team identified a division by zero error in the arithmetic operations handler causing the infinite loop.
- **15:00 UTC** - A hotfix was deployed to handle division by zero correctly, preventing the loop.
- **15:10 UTC** - Service functionality began to restore gradually as server load decreased.
- **15:30 UTC** - Full recovery confirmed, and the service was back to normal operation.

## Root Cause and Resolution

### Root Cause:
The outage was triggered by a specific edge case where a user attempted to divide a number by zero. This edge case was not handled in the recent code update, leading to an infinite loop in the calculation handler. The loop caused the server's CPU to spike to 100%, effectively rendering the service unavailable to other users.

### Resolution:
The backend engineering team identified the root cause by reviewing the error logs, which pointed to the division operation. A hotfix was developed to check for division by zero before performing the operation. If detected, the service now returns an appropriate error message to the user instead of attempting the division. The hotfix was tested and deployed, which resolved the CPU issue and restored service functionality.

## Corrective and Preventative Measures

### Improvements:
- **Code Review:** Implement stricter code reviews, especially around edge cases and input validation.
- **Automated Testing:** Expand automated test coverage to include more edge cases, particularly those involving arithmetic operations.
- **Monitoring Enhancements:** Improve monitoring to detect and alert on potential infinite loops or unusual CPU usage patterns more quickly.

### Tasks:
- [ ] Patch the division by zero issue in the Calculator service.
- [ ] Add automated tests to cover division by zero and other edge cases in arithmetic operations.
- [ ] Improve the monitoring setup to include alerts for infinite loops and high CPU usage.
- [ ] Conduct a team training session on edge case handling and input validation best practices.

This postmortem serves as a reminder of the importance of thorough testing and edge case handling, particularly in services involving critical computations.
