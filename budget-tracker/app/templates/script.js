document.getElementById("expense-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get the input values
    const expenseName = document.getElementById("expense-name").value;
    const expenseAmount = parseFloat(document.getElementById("expense-amount").value);
    const expenseQuantity = parseInt(document.getElementById("expense-quantity").value, 10);
    const expenseCategory = document.getElementById("expense-category").value;
    const expenseDate = document.getElementById("expense-date").value;

    if (!expenseName || !expenseAmount || !expenseQuantity || !expenseCategory || !expenseDate) {
        return alert("All fields must be filled out.");
    }

    // Calculate total cost for the expense
    const totalAmount = expenseAmount * expenseQuantity;

    // Create a new row for the expense
    const tableRow = document.createElement("tr");

    // Add cells to the row
    tableRow.innerHTML = `
        <td>${expenseName}</td>
        <td>$${expenseAmount.toFixed(2)}</td>
        <td>${expenseQuantity}</td>
        <td>$${totalAmount.toFixed(2)}</td>
        <td>${expenseCategory}</td>
        <td>${expenseDate}</td>
        <td><button class="delete-btn">Delete</button></td>
    `;

    // Add the new row to the table
    document.getElementById("expense-list").appendChild(tableRow);

    // Update the total amount displayed
    updateTotalAmount();

    // Clear the form fields
    document.getElementById("expense-form").reset();
});

// Function to update the total amount of all expenses
function updateTotalAmount() {
    const rows = document.querySelectorAll("#expense-list tr");
    let total = 0;

    rows.forEach(row => {
        const totalCell = row.cells[3]; // Total is in the 4th column (index 3)
        const totalValue = parseFloat(totalCell.textContent.replace('$', ''));
        total += totalValue;
    });

    document.getElementById("total-amount").textContent = total.toFixed(2);
}

// Delete functionality for each row
document.getElementById("expense-list").addEventListener("click", function(event) {
    if (event.target && event.target.classList.contains("delete-btn")) {
        const row = event.target.closest("tr");
        row.remove();
        updateTotalAmount();
    }
});
