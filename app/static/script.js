// Alteração entre abas
function showTab(tabName) {
  // Esconder todas as abas
  document.querySelectorAll(".tab-content").forEach((tab) => {
    tab.classList.remove("active")
  })

  // Remover classe active de todos os botões
  document.querySelectorAll(".tab-btn").forEach((btn) => {
    btn.classList.remove("active")
  })

  // Mostrar aba selecionada
  document.getElementById(tabName + "-tab").classList.add("active")

  // Adicionar classe active ao botão clicado
  event.target.classList.add("active")
}


function copyResponse() {
     const reponseText = document.querySelector(".response-text").textContent
     navigator.clipboard.writeText(responseText).then(() => {
        const btn = document.querySelector(".btn-copy")
        const originalText = btn.textContent
        btn.textContent = "✅ Copiado!"
        btn.style.backgroud = "#28a745"

         setTimeout(() => {
      btn.textContent = originalText
      btn.style.background = "#28a745"
    }, 2000)
     })
}

document.getElementById("fileInput").addEventListener("change", (e) => {
    const fileName = e.target.files[0]?.name
    if (fileName) {
        const label = document.querySelector('label[for = "fileInput"]')
        label.textContent = `📎 ${fileName}`
        label.style.color = "#28a745"
    }
})

// Animação de loading no formulário
document.getElementById("emailForm").addEventListener("submit", (e) => {
  const btn = document.querySelector(".btn-primary")
  btn.textContent = "🔄 Processando..."
  btn.disabled = true
})

