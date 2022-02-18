potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                        "hobbies": ["jogging", "music"], "city": "Hamburg"},
                       {"name": "Sasha", "gender": "male", "age": 18,
                        "hobbies": ["rock music", "art"], "city": "Berlin"},
                       {"name": "Maria", "gender": "female", "age": 35,
                        "hobbies": ["art"], "city": "Berlin"},
                       {"name": "Daniel", "gender": "non-conforming", "age": 50,
                        "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
                       {"name": "John", "gender": "male", "age": 41,
                        "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]


def select_dates(potential_dates):
    name = ''
    opt_age = 30
    for pdates in enumerate(potential_dates):
        if pdates[1]["age"] >= opt_age and "art" in pdates[1]["hobbies"] and pdates[1]["city"] == "Berlin":
            if name == '':
                name = (pdates[1]["name"])
            else:
                name = name + ', ' + (pdates[1]["name"])

    return name

select_dates(potential_dates)