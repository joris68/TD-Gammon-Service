# Backgammon Service

This service implements the famous TD-Gammon learning system from the Researcher Terald Gesauro.

    To gain a deeper understanding check out these sources:
        [Wikipedia] (https://en.wikipedia.org/wiki/TD-Gammon)
        [Google Scholar] (https://scholar.google.de/scholar?hl=de&as_sdt=0%2C5&q=td+gammon+1992&btnG=&oq=TD-Gammon)
        [Official Publication] (https://www.csd.uwo.ca/~xling/cs346a/extra/tdgammon.pdf)
    

Training the Model:

    Either define a proper main method, or just call a function in a module

    - cd backgammon_service
    - python -m src.<moduleNameHere>

    - you might even find a better way....

    the model will the be serialialized in the models folder for deploymemt / reuse


Running the Tests:

    pip install requirements.txt
    pytest test_main.py



Running the Service:

    cd backgammon_service
    docker run -p 8001:8081 backgammon_service



Contributing:

    - In know the project is not perfect (and entirely correct) but colloboration is highly appreciated.