### Starta webbservern

1. Öppna en terminal och navigera till mappen `flask-project`

2. Skapa ett "virtual environment" (om du inte har mappen venv)

    Windows: `py -3 -m venv venv`

    Linux/macOS: `python3 -m venv venv`

3. Aktivera ditt environment (detta behöver göras varje gång man öppnar en ny terminal, se nedan).

    Windows: `venv\Scripts\activate`

    Linux/macOS: `source venv/bin/activate`

    Ditt environment är aktiverat om du ser `(venv)` längst ner till vänster i terminalen.

4. Installera flask

    `pip install flask`

<!--
4. Kör följande kommandon för att "berätta" vart flask ska köras och sätta lösenordet för databasen

    Linux/macOS:
    ```
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    export DB_PASSWORD=*Ditt Lösenord*
    ```

    Windows PowerShell:
    ```
    $env:FLASK_APP = "flaskr"
    $env:FLASK_ENV = "development"
    $env:DB_PASSWORD = *Ditt Lösenord*
    ```

    Windows CMD:
    ```
    set FLASK_APP = "flaskr"
    set FLASK_ENV = "development"
    set DB_PASSWORD = *Ditt Lösenord*
    ```
-->
5. Starta flask genom att köra `flask run` i terminalen

6. För att se sidan, öppna http://localhost:5000 i en webbläsare


