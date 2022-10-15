-- Querie 1 
SELECT p.prof_id, count(student_id) AS total_de_alunos, p.teaching_ability FROM prof AS p 
JOIN ra USING(prof_id) 
GROUP BY prof_id;

-- Querie 2
SELECT prof_id, count(DISTINCT course_id) AS total_de_cursos FROM ra JOIN registration AS r USING(student_id)
JOIN course AS c USING(course_id)
GROUP BY prof_id
ORDER BY prof_id; 

-- Querie para conferência da segunda questão

SELECT * FROM ra JOIN registration AS r USING(student_id)
JOIN course AS c USING(course_id)
ORDER BY prof_id, student_id, course_id;