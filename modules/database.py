import sqlite3

DB_NAME = "raigap.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessments (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        organization TEXT,

        department TEXT,

        ai_system TEXT,

        owner TEXT,

        industry TEXT,

        ai_type TEXT,

        deployment TEXT,

        criticality TEXT,

        overall_score REAL,

        risk TEXT,

        assessment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()

    conn.close()


def save_assessment(
        organization,
        department,
        ai_system,
        owner,
        industry,
        ai_type,
        deployment,
        criticality,
        overall_score,
        risk
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO assessments(

        organization,
        department,
        ai_system,
        owner,
        industry,
        ai_type,
        deployment,
        criticality,
        overall_score,
        risk

    )

    VALUES(?,?,?,?,?,?,?,?,?,?)
    """,(

        organization,
        department,
        ai_system,
        owner,
        industry,
        ai_type,
        deployment,
        criticality,
        overall_score,
        risk

    ))

    conn.commit()

    conn.close()


def load_assessments():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM assessments
    ORDER BY assessment_date DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data