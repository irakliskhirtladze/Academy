import sqlite3

conn = sqlite3.connect('academy.db')
curs = conn.cursor()


def create_data():
    # Create and populate tables with initial data
    try:
        curs.executescript(''' 
        CREATE TABLE IF NOT EXISTS advisor( 
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL,
        surname TEXT NOT NULL
        ); 
    
        CREATE TABLE IF NOT EXISTS student( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        surname TEXT NOT NULL
        ); 
                        
        CREATE TABLE IF NOT EXISTS advisor_student (
            advisor_id INTEGER,
            student_id INTEGER,
            PRIMARY KEY (advisor_id, student_id),
            FOREIGN KEY (advisor_id) REFERENCES advisor(id),
            FOREIGN KEY (student_id) REFERENCES student(id)
        );
    
        INSERT INTO advisor(id, name, surname) VALUES 
        (1,"John", "Paul"), 
        (2,"Anthony", "Roy"), 
        (3,"Samantha", "Shepherd"), 
        (4,"Sam"," Reeds"), 
        (5,"Arthur", "Clintwood"); 
    
        ''')

        conn.commit()

    except sqlite3.IntegrityError:
        pass

