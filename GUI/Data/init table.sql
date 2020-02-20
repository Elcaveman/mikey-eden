CREATE TABLE AnimeInfo
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- primary key column
    URL CHAR(200) NOT NULL UNIQUE,
    Title CHAR(100) NOT NULL,
    Keyword CHAR(100) NOT NULL,
    episode INT NOT NULL
);
