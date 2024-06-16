function submitForm() {
    const form = document.getElementById('dictionary-form');
    const formData = new FormData(form);

    const data = {
        term: formData.get('term'),
        part_of_speech: formData.get('part_of_speech'),
        definitions: formData.getAll('definitions'),
        english_sentence: formData.get('english_sentence'),
        ibibio_sentence: formData.get('ibibio_sentence'),
        related_terms: formData.get('related_terms')
    };

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Redirect or update UI as needed
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
