var text = `Hay, my name is Ikhwananda Rizaldi you can call me Aldi. 
            I'm a passionate web developer and designer with 5+ years of experience in creating visually appealing and user-friendly websites. I'm always looking for new challenges and opportunities to grow as a developer. When I'm not coding, you can find me playing guitar, watching movies, or traveling to new places.`;
var i = 0;
var speed = 50; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
    if (i < text.length) {
        document.getElementById("typing-text").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

window.onload = function() {
    typeWriter();
};