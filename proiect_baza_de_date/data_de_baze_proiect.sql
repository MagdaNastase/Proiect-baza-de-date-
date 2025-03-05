-- Creare baza de date
CREATE DATABASE IF NOT EXISTS LibrarieOnline;

-- Folosirea bazei de date
USE LibrarieOnline;

-- Creare tabel pentru Produse
CREATE TABLE Produse (
    ID_Produs INT AUTO_INCREMENT PRIMARY KEY,
    Denumire VARCHAR(255) NOT NULL,
    Pret DECIMAL(10, 2) CHECK(Pret >= 0),
    Descriere TEXT,
    Stoc INT NOT NULL
);

-- Creare tabel pentru Clienți
CREATE TABLE Clienti (
    ID_Client INT AUTO_INCREMENT PRIMARY KEY,
    Nume VARCHAR(255) NOT NULL,
    Prenume VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Telefon VARCHAR(15),
    DataInregistrare DATE,
    Adresa TEXT
);

-- Creare tabel pentru Angajati
CREATE TABLE Angajati (
    ID_Angajat INT AUTO_INCREMENT PRIMARY KEY,
    Nume VARCHAR(255) NOT NULL,
    Prenume VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Telefon VARCHAR(15),
    DataAngajare DATE NOT NULL,
    Salariu DECIMAL(10, 2) CHECK(Salariu >= 0)
);

-- Creare tabel pentru Comenzi
CREATE TABLE Comenzi (
    ID_Comanda INT AUTO_INCREMENT PRIMARY KEY,
    ID_Client INT,
    ID_Angajat INT,
    DataComanda DATE NOT NULL,
    Total DECIMAL(10, 2),
    FOREIGN KEY (ID_Client) REFERENCES Clienti(ID_Client),
    FOREIGN KEY (ID_Angajat) REFERENCES Angajati(ID_Angajat)
);

-- Creare tabel pentru DetaliiComenzi
CREATE TABLE DetaliiComenzi (
    ID_Comanda INT,
    ID_Produs INT,
    Cantitate INT NOT NULL,
    PretUnitar DECIMAL(10, 2),
    FOREIGN KEY (ID_Comanda) REFERENCES Comenzi(ID_Comanda),
    FOREIGN KEY (ID_Produs) REFERENCES Produse(ID_Produs),
    PRIMARY KEY (ID_Comanda, ID_Produs)
);



-- Vizualizare conținutul tabelului Produse
SELECT * FROM Produse;

-- Vizualizare conținutul tabelului Clienti
SELECT * FROM Clienti;

-- Vizualizare conținutul tabelului Angajati
SELECT * FROM Angajati;

-- Vizualizare conținutul tabelului Comenzi
SELECT * FROM Comenzi;

-- Vizualizare conținutul tabelului DetaliiComenzi
SELECT * FROM DetaliiComenzi;


-- Pentru a vedea detalii despre tabelul Produse
DESCRIBE Produse;

-- Pentru a vedea detalii despre tabelul Clienti
DESCRIBE Clienti;

-- Pentru a vedea detalii despre tabelul Angajati
DESCRIBE Angajati;

-- Pentru a vedea detalii despre tabelul Comenzi
DESCRIBE Comenzi;

-- Pentru a vedea detalii despre tabelul DetaliiComenzi
DESCRIBE DetaliiComenzi;


-- Introducere exemple în tabelul Produse
INSERT INTO Produse (Denumire, Pret, Descriere, Stoc) VALUES 
    ('Harry Potter și Piatra Filozofală', 29.99, 'Primul volum din seria Harry Potter', 100),
    ('Jocurile Foamei', 24.50, 'Romanul SF distopic al Suzannei Collins', 75),
    ('1984', 19.99, 'Clasicul antiutopiei scrise de George Orwell', 120),
    ('O mie și una de nopți', 35.00, 'Culegere de povești orientale', 50),
    ('Cronicile din Narnia', 28.99, 'Serie de romane fantasy scrise de C.S. Lewis', 80);

-- Introducere exemple în tabelul Clienti
INSERT INTO Clienti (Nume, Prenume, Email, Telefon, DataInregistrare, Adresa) VALUES 
    ('Ionescu', 'Ana', 'ana.ionescu@example.com', '0712345678', '2024-05-19', 'Str. Libertății nr. 10, București'),
    ('Popescu', 'Mihai', 'mihai.popescu@example.com', '0723456789', '2024-05-18', 'Bd. Independenței nr. 25, Cluj-Napoca'),
    ('Dumitrescu', 'Maria', 'maria.dumitrescu@example.com', '0734567890', '2024-05-20', 'Aleea Rozelor nr. 15, Iași'),
    ('Georgescu', 'Andrei', 'andrei.georgescu@example.com', '0745678901', '2024-05-17', 'P-ța Victoriei nr. 5, Timișoara'),
    ('Constantinescu', 'Elena', 'elena.constantinescu@example.com', '0756789012', '2024-05-16', 'B-dul Unirii nr. 30, Constanța');

-- Introducere exemple în tabelul Angajati
INSERT INTO Angajati (Nume, Prenume, Email, Telefon, DataAngajare, Salariu) VALUES 
    ('Popa', 'Andreea', 'andreea.popa@example.com', '0711111111', '2023-02-15', 3000.00),
    ('Mihai', 'Cristian', 'cristian.mihai@example.com', '0722222222', '2022-09-10', 3200.00),
    ('Georgescu', 'Maria', 'maria.georgescu@example.com', '0733333333', '2024-01-20', 3500.00),
    ('Ionescu', 'Alex', 'alex.ionescu@example.com', '0744444444', '2023-11-05', 3300.00),
    ('Dumitrescu', 'Elena', 'elena.dumitrescu@example.com', '0755555555', '2022-12-30', 3100.00);

-- Introducere exemple în tabelul Comenzi
INSERT INTO Comenzi (ID_Client, ID_Angajat, DataComanda, Total) VALUES 
    (1, 1, '2024-05-20', 150.00),
    (2, 2, '2024-05-19', 280.00),
    (3, 3, '2024-05-18', 200.00),
    (4, 4, '2024-05-17', 320.00),
    (5, 5, '2024-05-16', 250.00);

-- Introducere exemple în tabelul DetaliiComenzi
INSERT INTO DetaliiComenzi (ID_Comanda, ID_Produs, Cantitate, PretUnitar) VALUES 
    (1, 1, 2, 29.99),
    (2, 2, 1, 24.50),
    (3, 3, 3, 19.99),
    (4, 4, 1, 35.00),
    (5, 5, 2, 28.99);
