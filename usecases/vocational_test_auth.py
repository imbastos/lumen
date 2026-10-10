RIASEC_PROFILES = {
    "R": "Realistic",
    "I": "Investigative",
    "A": "Artistic",
    "S": "Social",
    "E": "Enterprising",
    "C": "Conventional", }

SCALE_OPTIONS = [
    {"value": 1, "label": "Discordo totalmente"},
    {"value": 2, "label": "Discordo"},
    {"value": 3, "label": "Neutro"},
    {"value": 4, "label": "Concordo"},
    {"value": 5, "label": "Concordo totalmente"},
]

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
            "Gosto de trabalhar em atividades na qual possa orientar e ajudar pessoas."
        ),
        "profile": "S",
    },
    {
        "id": "Q13",
        "text": (
            "Em um trabalho em grupo, Costumo tomar a iniciativa e liderar o grupo."
        ),
        "profile": "E",
    },
    {
        "id": "Q14",
        "text": (
            "Quando estou em um ambiente polarizado, me sinto à vontade para apresentar suas ideias e defender seu ponto de vista."
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
            "para identificar possíveis erros."
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
