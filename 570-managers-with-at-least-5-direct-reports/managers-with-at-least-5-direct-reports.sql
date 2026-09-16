-- Write your PostgreSQL query statement below
SELECT e.name
FROM Employee e
WHERE (SELECT COUNT(*) FROM Employee f WHERE f.managerID = e.id) >= 5