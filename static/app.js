document.querySelector('form').onsubmit = function(event) {
    event.preventDefault();
    var song_id = document.querySelector('input[name="song_id"]').value;
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'song_id=' + song_id
    }).then(response => response.json()).then(data => {
        const recommendationsDiv = document.getElementById('recommendations');
        recommendationsDiv.innerHTML = '<h2>Recommended Songs:</h2>';
        data.forEach(song => {
            recommendationsDiv.innerHTML += `<p>${song.name} by ${song.artists}</p>`;
        });
    });
};
