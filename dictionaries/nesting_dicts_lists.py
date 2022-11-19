student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 91:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "fail"

print(student_grades)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting Dictionary in Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},

    "Germany": {"german_cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total visits": 5},
}

# Nesting Dictionary in List

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12},

    {"country": "Germany",
        "german_cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total visits": 5},
]
