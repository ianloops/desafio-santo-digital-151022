from collections import defaultdict
import sqlite3

from fastapi import FastAPI

app = FastAPI()
connection = sqlite3.connect("university.db")


def execute_query(query):
    cursor = connection.cursor()
    cursor.execute(query)

    return cursor.fetchall()


def make_response(columns, items):
    data = []

    for values in items:
        result = {}

        for column, value in zip(columns, values):
            result[column] = value

        data.append(result)

    return data


@app.get("/api/course/students/list")
async def get_list_students_by_course(rating: int):
    query = """
        SELECT course_id, student_id, rating
        FROM registration
        JOIN course USING (course_id)
    """

    result = execute_query(query)

    data = defaultdict(list)
    for item in result:
        data[(item[0], item[2])].append(item[1])

    final_result = []

    for key, value in data.items():
        if rating is not None and rating != key[1]:
            continue

        final_result.append({
            'course_id': key[0],
            'rating': key[1],
            'students': value,
        })

    return {"data": final_result}


@app.get("/api/report/student/rank")
async def get_report_top_students():
    query = """
        SELECT student_id, intelligence, ranking
        FROM student
        ORDER BY ranking, intelligence DESC
        LIMIT 5
    """

    result = execute_query(query)
    data = make_response(['student_id', 'intelligence', 'ranking'], result)

    return {"data": data}


@app.get("/api/report/teacher/popularity")
async def get_report_teacher_popularity():
    query = """
        SELECT prof_id, popularity
        FROM prof
        ORDER BY popularity DESC
    """

    result = execute_query(query)
    data = make_response(['prof_id', 'popularity'], result)

    return {"data": data}


@app.get("/api/report/course/students")
async def get_report_students_by_course():
    query = """
        SELECT course_id, COUNT(student_id) AS "students_qty"
        FROM registration
        GROUP BY course_id
        ORDER BY COUNT(student_id) DESC
    """

    result = execute_query(query)
    data = make_response(['course_id', 'students_qty'], result)

    return {"data": data}
