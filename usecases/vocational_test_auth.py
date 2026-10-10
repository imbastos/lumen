#

#
RIASEC_PROFILES = {
     "R": "Realista",
    "I": "Investigativo",
    "A": "Artístico",
    "S": "Social",
    "E": "Empreendedor",
    "C": "Convencional",
}

#
SCALE_OPTIONS = [
    {"value": 1, "label": "Discordo totalmente"},
    {"value": 2, "label": "Discordo"},
    {"value": 3, "label": "Neutro"},
    {"value": 4, "label": "Concordo"},
    {"value": 5, "label": "Concordo totalmente"},
]

#
QUESTIONS = [
    {
        "id": "Q01",
        "text": ( "Tenho interesse em descobrir e observar como os aparelhos e equipamentos funcionam." ),
        "profile": "R",
    },
  
    {
        "id": "Q02",
        "text": (
            "Quando algum objeto ou equipamento apresenta defeito, tento descobrir o que aconteceu e consertá-lo."
        ),
        "profile": "R",
    },
    {
        "id": "Q03",
        "text": (
            "Quando aprendo algo novo, ao invés de focar na teoria, começo colocando a mão na massa."
        ),
        "profile": "R",
    },
    {
        "id": "Q04",
        "text": (
            "Quando realizo uma pesquisa, me aprofundo no assunto e busco informações além das primeiras respostas."
        ),
        "profile": "I",
    },
    {
        "id": "Q05",
        "text": (
            "Analiso todas as informações antes de chegar a uma conclusão."
        ),
        "profile": "I",
    },
    {
        "id": "Q06",
        "text": (
            "Tenho interesse em analisar resultados de pesquisas, exames ou experimentos para entender o que revelam."
        ),
        "profile": "I",
    },
    {
        "id": "Q07",
        "text": (
            "Costumo me expressar através de formas artísticas (desenho, música, escrita…)."
        ),
        "profile": "A",
    },
    {
        "id": "Q08",
        "text": (
            "Quando estou produzindo um slide, costumo criar um modelo original ao invés de utilizar um já pronto."
        ),
        "profile": "A",
    },
    {
        "id": "Q09",
        "text": (
            "Depois de assistir um filme, reflito além das mensagens transmitidas."
        ),
        "profile": "A",
    },
    {
        "id": "Q10",
        "text": (
            "Quando um amigo está desamparado, me ofereço para ouvi-lo e aconselhar."
        ),
        "profile": "S",
    },
    {
        "id": "Q11",
        "text": (
            "Quando explico algo a uma pessoa e ela não entende, não me importo em repetir e reformular até ela entender."
        ),
        "profile": "S",
    },
    {
        "id": "Q12",
        "text": (
            "Gosto de trabalhar em atividades nais quais possa orientar e ajudar pessoas."
        ),
        "profile": "S",
    },
    {
        "id": "Q13",
        "text": (
            "Em um trabalho em grupo, costumo tomar a iniciativa e liderar o grupo."
        ),
        "profile": "E",
    },
    {
        "id": "Q14",
        "text": (
            "Quando estou em um ambiente polarizado, me sinto à vontade para apresentar minhas ideias e defender meu ponto de vista."
        ),
        "profile": "E",
    },
    {
        "id": "Q15",
        "text": (
            "Gostaria de ser responsável por um projeto ou negócio."
        ),
        "profile": "E",
    },
    {
        "id": "Q16",
        "text": (
            "Me sinto confortável trabalhando com regras e instruções bem definidas."
        ),
        "profile": "C",
    },
    {
        "id": "Q17",
        "text": (
            "Tenho paciência para verificar erros nas informações."
        ),
        "profile": "C",
    },
    {
        "id": "Q18",
        "text": (
            "Mantenho meus gastos financeiros e/ou tarefas organizados por notas ou planilhas."
        ),
        "profile": "C",
    },
]

#
AREA_QUESTION = {
    "id": "I01",
    "text": "Qual área do conhecimento mais lhe atrai?",
    "options": [
        {
            "value": "computing",
            "label": "Computação e Tecnologia",
        },
        {
            "value": "stem",
            "label": "Engenharias e Ciências Exatas",
        },
        {
            "value": "health_biological",
            "label": "Saúde e Ciências Biológicas",
        },
        {
            "value": "social_humanities",
            "label": "Ciências Humanas e Sociais",
        },
        {
            "value": "education",
            "label": "Educação",
        },
        {
            "value": "art",
            "label": "Artes, Design e Comunicação",
        },
        {
            "value": "business_management",
            "label": "Negócios e Gestão",
        },
        {
            "value": "environmental",
            "label": "Ciências Agrárias e Meio Ambiente",
        },
    ],
}

#
def unanswered_questions(responses):
    unanswered = []
    for question_review in QUESTIONS:
        answer_found = responses.get(question_review["id"])
        if (
            not isinstance(answer_found, int) 
            or answer_found < 1 
            or answer_found > 5
        ):
             unanswered.append(question_review["id"])

    return unanswered

def valid_area_interest(area_interest):
    valid_areas = []
    for option in AREA_QUESTION["options"]:
        valid_areas.append(option["value"])

    return area_interest in valid_areas

def calculate_profile_scores(responses):
    pending_questions = unanswered_questions(responses)

    if pending_questions:
        raise ValueError("Verifique as questões sem resposta válida: " + ", ".join(pending_questions)
        )

    scores = {
        profile: 0
        for profile in RIASEC_PROFILES
    }

    for question in QUESTIONS:
        answer = responses[question["id"]]
        profile = question["profile"]

        scores[profile] += answer

    return scores

















    
