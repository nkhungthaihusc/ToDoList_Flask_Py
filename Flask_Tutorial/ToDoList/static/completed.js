function markCompleted(noteId) {
        const row = document.getElementById(`note-${noteId}`);
        if (row) {
            row.classList.add('completed-row');
        }
    }
