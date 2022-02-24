from random import randint


def generate_data(user_id, ts):
    return [{"user_id": user_id, "timestamp": ts, "heart_rate": randint(0, 220), "respiration_rate": randint(0, 44),
            "activity": randint(0, 10)}]

