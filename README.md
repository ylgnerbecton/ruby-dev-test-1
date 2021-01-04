# ruby-dev-test-1

Desenvolver a camada de modelos de um sistema de arquivos persistido em um banco de dados SQL onde seja possível criar diretórios e arquivos. Os diretórios poderão conter sub-diretórios e arquivos. O conteúdo dos arquivos podem estar ser persistidos como blob, S3 ou mesmo em disco.

A soluçãos deverá ser escrita majoritariamente em Ruby com framework Ruby on Rails.

Realizar um fork deste repositório.

------------------------------------------------------------------------------------------

Bem-vindo ao projeto.

### INFO ###

* Plataforma: Python / Django.

* Versão: 0.0.1

instalação rápida:
~~~~~~~~~~~~
    git clone https://github.com/ylgnerbecton/ruby-dev-test-1.git
    cd ruby-dev-test-1
    mv sample.env .env

    python3:
        python3 -m venv .env
        source .env/bin/activate
        pip3 install -r requirements.txt
        python3 manage.py migrate
        python3 manage.py runserver
    
    docker:
        docker-compose up -d --build
        docker ps 
        docker logs -f ruby-dev-test-1_web_1
