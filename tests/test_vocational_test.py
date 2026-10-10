from usecases.vocational_test_auth import (
    unanswered_questions,
    valid_area_interest,
    calculate_profile_scores,
)

responses = {
    "Q01": 4,
    "Q02": 5,
    "Q03": 3,
    "Q04": 5,
    "Q05": 4,
    "Q06": 5,
    "Q07": 3,
    "Q08": 3,
    "Q09": 4,
    "Q10": 5,
    "Q11": 4,
    "Q12": 5,
    "Q13": 2,
    "Q14": 3,
    "Q15": 2,
    "Q16": 4,
    "Q17": 4,
    "Q18": 3,
}

print("Perguntas pendentes:")
print(unanswered_questions(responses))

print("\nÁrea de Computação válida?")
print(valid_area_interest("computing"))

print("\nÁrea de Medicina válida?")
print(valid_area_interest("medicina"))

print("\nPontuações dos perfis:")
print(calculate_profile_scores(responses))
