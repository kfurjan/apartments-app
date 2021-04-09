
-- name: get-user-by-email^
SELECT id,
       email,
       password,
FROM users
WHERE email = :email
LIMIT 1;

-- name: create-new-user<!
INSERT INTO users (email, password)
VALUES (:email, :password)
RETURNING
    id, email, password;
