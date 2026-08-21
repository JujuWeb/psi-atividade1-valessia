1. Onde está cada camada do MVC no seu projeto? O que aconteceria se a lógica de acesso aos dados
fosse escrita direto dentro das rotas?

Models (M) em models.py que contém todas os dados precisos;
View (V) em templates-base.html que contém o html e css que é aquilo que o usuário vê;
Controlls (C) em app.py que liga os dados ao usuário através das ações que ele recebe, por exemplo, busca por livro.