const botoes = document.querySelectorAll(".cardBtn")

botoes.forEach(btn=>{

    btn.addEventListener("click",async (e)=>{
        e.preventDefault()
        const id = btn.id
        let data = await fetch ("/json/persona/" + id)
        data = await data.json() 
        console.log(data)
        const megacard = document.getElementById("megaCard")
        megacard.classList.remove("none")
        megacard.innerHTML = "<p>" + await data.name + "</p><p>" + await data.text + "</p>"
    })


})