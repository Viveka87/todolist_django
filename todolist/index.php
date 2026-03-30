<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Todo List</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-10">
    <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-lg">
        <h2 class="text-2xl font-bold mb-4">Todo List</h2>
        
        <form action="add_task.php" method="POST" class="flex gap-2">
            <input type="text" name="task" placeholder="Enter a new task..." required 
                   class="flex-1 border p-2 rounded">
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Add</button>
        </form>

        <ul class="mt-6">
            </ul>
    </div>
</body>
</html>