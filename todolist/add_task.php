<?php
// 1. Include the database connection
include 'db.php';

if($_SERVER['REQUEST_METHOD'] == 'POST') {
    // 2. Get the task from the form input
    $task = $_pro_task = $_POST['task'];

    if (!empty($task)) {
        try {
            // 3. Prepare the SQL statement (Secure against SQL Injection)
            $sql = "INSERT INTO tasks (task_name) VALUES (:task_name)";
            $stmt = $conn->prepare($sql);
            
            // 4. Bind the value and execute
            $stmt->execute(['task_name' => $task]);

            // 5. Redirect back to the main page
            header("Location: index.php");
            exit();
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
    } else {
        header("Location: index.php?error=empty");
    }
}
?>