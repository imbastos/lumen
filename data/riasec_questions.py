from enums.riasec_profile import RiasecProfile
from models.riasec_question import RiasecQuestion

questions = (
    # RiasecQuestion(
    #     profile=RiasecProfile.R,
    #     text="Tenho interesse em descobrir e observar como os aparelhos e equipamentos funcionam.",
    # ),
    # RiasecQuestion(
    #     profile=RiasecProfile.R,
    #     text="Quando algum objeto ou equipamento apresenta defeito, tento descobrir o que aconteceu e consertá-lo.",
    # ),
    RiasecQuestion(
        profile=RiasecProfile.R,
        text="Quando aprendo algo novo, ao invés de focar na teoria, começo colocando a mão na massa.",
    ),
    # RiasecQuestion(
    #     profile=RiasecProfile.I,
    #     text="Quando realizo uma pesquisa, me aprofundo no assunto e busco informações além das primeiras respostas.",
    # ),
    # RiasecQuestion(
    #     profile=RiasecProfile.I,
    #     text="Analiso todas as informações antes de chegar a uma conclusão.",
    # ),
    RiasecQuestion(
        profile=RiasecProfile.I,
        text="Tenho interesse em analisar resultados de pesquisas, exames ou experimentos para entender o que revelam.",
    ),
    # RiasecQuestion(
    #     profile=RiasecProfile.A,
    #     text="Costumo me expressar através de formas artísticas (desenho, música, escrita…).",
    # ),
    # RiasecQuestion(
    #     profile=RiasecProfile.A,
    #     text="Quando estou produzindo um slide, costumo criar um modelo original ao invés de utilizar um já pronto.",
    # ),
    RiasecQuestion(
        profile=RiasecProfile.A,
        text="Depois de assistir um filme, reflito além das mensagens transmitidas.",
    ),
    # RiasecQuestion(
    #     profile=RiasecProfile.S,
    #     text="Quando um amigo está desamparado, me ofereço para ouvi-lo e aconselhar.",
    # ),
    # RiasecQuestion(
    #     profile=RiasecProfile.S,
    #     text="Quando explico algo a uma pessoa e ela não entende, não me importo em repetir e reformular até ela entender.",
    # ),
    RiasecQuestion(
        profile=RiasecProfile.S,
        text="Gosto de trabalhar em atividades nas quais possa orientar e ajudar pessoas.",
    ),
    # RiasecQuestion(
    #     profile=RiasecProfile.E,
    #     text="Em um trabalho em grupo, costumo tomar a iniciativa e liderar o grupo.",
    # ),
    # RiasecQuestion(
    #     profile=RiasecProfile.E,
    #     text="Quando estou em um ambiente polarizado, me sinto à vontade para apresentar minhas ideias e defender meu ponto de vista.",
    # ),
    RiasecQuestion(
        profile=RiasecProfile.E,
        text="Gostaria de ser responsável por um projeto ou negócio.",
    ),
    # RiasecQuestion(
    #     profile=RiasecProfile.C,
    #     text="Me sinto confortável trabalhando com regras e instruções bem definidas.",
    # ),
    # RiasecQuestion(
    #     profile=RiasecProfile.C,
    #     text="Tenho paciência para verificar erros nas informações.",
    # ),
    RiasecQuestion(
        profile=RiasecProfile.C,
        text="Mantenho meus gastos financeiros e/ou tarefas organizados por notas ou planilhas.",
    ),
)
