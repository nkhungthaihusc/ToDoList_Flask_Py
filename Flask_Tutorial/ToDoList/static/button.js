document.getElementById("note").addEventListener("keydown", function(event) {
    // Nếu người dùng nhấn Enter (không giữ Shift)
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault(); // Ngăn xuống dòng
        this.form.submit();     // Gửi form
    }
});
