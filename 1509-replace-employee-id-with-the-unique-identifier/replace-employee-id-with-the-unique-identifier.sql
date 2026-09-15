-- Write your PostgreSQL query statement below
SELECT f.unique_id, e.name as name
FROM Employees e LEFT OUTER JOIN EmployeeUNI f
ON e.id = f.id