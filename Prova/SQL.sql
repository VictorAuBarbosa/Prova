CREATE TABLE Professor (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome TEXT,
    email TEXT,
    CPF VARCHAR(11) UNIQUE,
    senha TEXT
);

CREATE TABLE Turmas (
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome_turma TEXT,
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
);

CREATE TABLE Atividades (
    id_atividade INT AUTO_INCREMENT PRIMARY KEY,
    atividade TEXT
);

CREATE TABLE Adicionar_atividade (
    id_add INT AUTO_INCREMENT PRIMARY KEY,
    id_turma INT,
    id_atividade INT,
    FOREIGN KEY (id_turma) REFERENCES Turmas(id_turma),
    FOREIGN KEY (id_atividade) REFERENCES Atividades(id_atividade)
);
