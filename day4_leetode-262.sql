-- https://leetcode.com/problems/trips-and-users/

SELECT request_at AS Day, ROUND(SUM(status) / COUNT(*), 2) AS 'Cancellation Rate'
FROM (
    SELECT IF(Trips.status REGEXP 'cancelled_by_[driver,client]', 1, 0) AS status, Trips.request_at AS request_at
    FROM Trips 
        LEFT JOIN Users AS users_client ON Trips.client_id = users_client.users_id
        LEFT JOIN Users AS users_driver ON Trips.driver_id = users_driver.users_id
    WHERE users_client.banned = 'No' AND users_driver.banned = 'No'
) AS filtered_trips
GROUP BY request_at