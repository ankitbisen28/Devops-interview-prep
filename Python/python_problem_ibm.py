from collections import defaultdict

logs = [
  "INFO auth login success",
  "ERROR payment timeout",
  "ERROR auth invalid token",
  "INFO order placed",
  "ERROR payment gateway down"
]

from collections import defaultdict

def count_errors(logs):
    error_count = defaultdict(int)

    for log in logs:
        if log.startswith("ERROR"):
            service = log.split()[1]
            error_count[service] += 1

    return dict(error_count)

print(count_errors(logs))
