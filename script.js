// Portfolio Website Loaded
console.log("Portfolio Website Loaded Successfully!");

// Welcome Message
window.onload = function() {
    alert("Welcome to My Portfolio Website!");
};

// Smooth Scroll Effect
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// Dynamic Footer Year
const footer = document.querySelector("footer p");

if(footer){
    footer.innerHTML = `© ${new Date().getFullYear()} B sai sree charan. All Rights Reserved.`;
}

// Contact Button Example
function showMessage() {
    alert("Thank you for visiting my portfolio!");
}