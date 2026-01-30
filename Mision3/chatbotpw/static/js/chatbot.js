const form=document.getElementById("chatForm"); /* cuando declaramos constante es decir que no cmabia pero todo su comportamiento interno si cambia */
const input= document.getElementById("userInput");
const messages=document.getElementById("messages");
form.addEventListener("submit",async (e)=>{
    e.preventDefault();
    const text=input.value.trim();
    if(!text)return;
    messages.innerHTML+=`<div class="msg user">Tú:${text}</div>`;
    /* cuando se crea una constante nunca se le puede volver a poner =, es decir, no se le peude volver a asignar (solo una vez) */
    input.value="";
    const response =await fetch("/chat",{
        method:"POST",
        headers:{"Content-Type": "application/x-www-form-urlencoded"},
        body:`message=${encodeURIComponent(text)}`
    });
    const data = await response.json();
    messages.innerHTML+=`<div class="msg bot">Bot:${data.response}</div>`;
    messages.scrollTop=messages.scrollHeight;
})