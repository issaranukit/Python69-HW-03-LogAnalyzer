from collections import Counter, defaultdict

def analyze_user_activity(log_file_path: str) -> dict:
    action_counts = Counter()
    user_duration = defaultdict(float)
    login_times = []

    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) != 4:
                continue

            timestamp, user_id, action, duration = parts

            try:
                duration = float(duration)
            except ValueError:
                continue

            action_counts[action] += 1

            user_duration[user_id] += duration

            if action == "login":
                login_times.append(duration)

    average_session_time = (
        sum(login_times) / len(login_times)
        if login_times else 0.0
    )

    most_active_user = None
    if user_duration:
        most_active_user = max(user_duration, key=user_duration.get)

    return {
        "total_users": len(user_duration),
        "action_counts": dict(action_counts),
        "most_active_user": most_active_user,
        "average_session_time": average_session_time,
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)

# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}
