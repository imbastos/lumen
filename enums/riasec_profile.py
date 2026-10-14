from enum import Enum


class RiasecProfile(Enum):
    R = (
        "Realista",
        """
[bold $primary]🔧 Realista (R) — O executor[/bold $primary]

Pessoas com perfil realista gostam de atividades práticas...

[bold $secondary]Áreas profissionais:[/bold $secondary] [italic]Engenharia, Mecânica, Agronomia e Construção Civil.[/italic]
""",
    )
    I = ("Investigativo", """
[bold $primary]🔬 Investigativo (I) — O pesquisador[/bold $primary]

Pessoas com perfil investigativo têm curiosidade, gostam de analisar informações, investigar problemas e compreender como as coisas funcionam. Sentem-se motivadas por desafios intelectuais, pesquisas, experimentos e atividades que exigem raciocínio lógico e pensamento crítico.

[bold $secondary]Áreas profissionais:[/bold $secondary] [italic]Ciência, Medicina, Tecnologia da Informação, Biologia, Química, Pesquisa Científica, Análise de Dados e Psicologia com foco em pesquisa.[/italic]
""")
    A = ("Artístico", """
[bold $primary]🎨 Artístico (A) — O criador[/bold $primary]

Pessoas com perfil artístico valorizam a criatividade, a imaginação e a liberdade de expressão. Gostam de desenvolver ideias originais, criar projetos e explorar diferentes formas de comunicar sentimentos e pensamentos. Geralmente preferem ambientes flexíveis, que permitam inovação e experimentação.

[bold $secondary]Áreas profissionais:[/bold $secondary] [italic]Design, Artes Visuais, Música, Publicidade, Arquitetura, Moda, Cinema, Fotografia, Escrita e Produção de Conteúdo.[/italic]
""")
    S = ("Social", """
[bold $primary]🤝 Social (S) — O ajudador[/bold $primary]

Pessoas com perfil social gostam de interagir com outras pessoas, ensinar, orientar, cuidar e contribuir para o desenvolvimento humano. São motivadas por atividades que envolvem colaboração, comunicação, empatia e resolução de necessidades sociais.

[bold $secondary]Áreas profissionais:[/bold $secondary] [italic]Educação, Psicologia, Serviço Social, Enfermagem, Recursos Humanos, Fisioterapia, Terapia Ocupacional e Orientação Educacional.[/italic]
""")
    E = ("Empreendedor", """
[bold $primary]🚀 Empreendedor (E) — O influenciador[/bold $primary]

Pessoas com perfil empreendedor gostam de liderar, negociar, apresentar ideias, tomar decisões e mobilizar pessoas para alcançar objetivos. Sentem-se motivadas por desafios, oportunidades de crescimento e atividades que envolvem persuasão, iniciativa e gestão de projetos.

[bold $secondary]Áreas profissionais:[/bold $secondary] [italic]Administração, Empreendedorismo, Direito, Marketing, Gestão Comercial, Vendas, Relações Públicas, Gestão de Projetos e Liderança Empresarial.[/italic]
""")
    C = ("Convencional", """
[bold $primary]📊 Convencional (C) — O organizador[/bold $primary]

Pessoas com perfil convencional valorizam a organização, o planejamento, a precisão e o cumprimento de procedimentos. Gostam de trabalhar com dados, documentos, números e sistemas estruturados, buscando eficiência, clareza e atenção aos detalhes.

[bold $secondary]Áreas profissionais:[/bold $secondary] [italic]Contabilidade, Administração, Finanças, Logística, Gestão de Documentos, Análise Financeira, Departamento Pessoal e Controle de Qualidade.[/italic]
""")
