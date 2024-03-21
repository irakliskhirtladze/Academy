from modules.db import conn, curs


class Student:

    def __init__(self, name, surname, primary_key=None):
        self.name = name
        self.surname = surname
        self.student_id = primary_key

    def create(self):
        """Create a new student in the database"""
        curs.execute("INSERT INTO student (name, surname) VALUES (?, ?)", (self.name, self.surname))
        self.student_id = curs.lastrowid
        conn.commit()

    def get_advisor_id(self, advisor_name, advisor_surname):
        """Get advisor ID for based on given advisor name and surname"""
        curs.execute("SELECT id FROM advisor WHERE name = ? AND surname = ?", (advisor_name, advisor_surname))
        return curs.fetchone()[0]

    def add_advisor_student_relation(self, advisor_id):
        """Establish advisor-student relationship in a junction table"""
        curs.execute("INSERT INTO advisor_student (advisor_id, student_id) VALUES (?, ?)", (advisor_id, self.student_id))
        conn.commit()


class Advisor:

    def __init__(self, name, surname, primary_key=None):
        self.name = name
        self.surname = surname
        self.advisor_id = primary_key

    def get_students(self, advisor_id):
        """Get students for the given advisor"""

        query = """
            SELECT s.id, s.name, s.surname
            FROM student s JOIN advisor_student a_s ON s.id = a_s.student_id
            WHERE a_s.advisor_id = ?
            """
        
        curs.execute(query, (advisor_id,))
        rows = curs.fetchall()
        return rows
    
    def get_students_count(self, advisor_id):
        query = """SELECT COUNT (DISTINCT student_id)
                     FROM advisor_student WHERE advisor_id = ?"""
        curs.execute(query, (advisor_id,))
        return curs.fetchone()[0]
        
    