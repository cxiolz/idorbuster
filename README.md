# IDORBuster by Caio Luchetti
Ferramenta automática para detecção de **IDOR (Insecure Direct Object Reference)** em APIs REST.


---

## ⚙️ Funcionalidades

✅ Substituição dinâmica de `{id}` na URL  
✅ Requisições paralelas com controle de concorrência  
✅ Suporte a headers personalizados (Authorization, Cookie, etc)  
✅ Análise de status code, tamanho e prévia da resposta  
✅ Exportação dos resultados em JSON  

---


## 🚀 Demonstração no terminal

```bash
$ python idorbuster.py --help                                 
                                                                                                                                                                       
 Usage: idorbuster.py [OPTIONS]                                                                                                                                        
                                                                                                                                                                       
 Executa o scanner de IDOR na URL informada                                                                                                                            
                                                                                                                                                                       
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --url                       TEXT     URL com {id} [default: None] [required]                                                                                     │
│    --method                    TEXT     Método HTTP [default: GET]                                                                                                  │
│    --auth-header               TEXT     Header de autenticação [default: None]                                                                                      │
│    --cookie                    TEXT     Cookie de sessão [default: None]                                                                                            │
│ *  --id-range                  TEXT     Intervalo de ID (ex: 1-1000) [default: None] [required]                                                                     │
│    --concurrency               INTEGER  Número de threads [default: 5]                                                                                              │
│    --output                    TEXT     Arquivo de saída JSON [default: report.json]                                                                                │
│    --install-completion                 Install completion for the current shell.                                                                                   │
│    --show-completion                    Show completion for the current shell, to copy it or customize the installation.                                            │
│    --help                               Show this message and exit.                                                                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


```

---

## 🛠️ Como usar

```bash
python idorbuster.py scan \
  --url "https://site.com/api/user/{id}" \
  --id-range 1-100 \
  --auth-header "Bearer SEU_TOKEN" \
  --cookie "PHPSESSID=abc123" \
  --concurrency 10
```

- `-u`, `--url`: 	URL alvo com placeholder {id}
- `-m`, `--method`: Método HTTP (GET, POST, etc.)  
- `-t`, `--auth-header`: Header de autenticação (opcional)
- `-o`, `--cookie`: Cookie de sessão (opcional)
- `-m`, `--id-range`: Intervalo de IDs para testar (ex: 1-100)
- `-t`, `--concurrency`: Nº de threads simultâneas
- `-o`, `--output`: Arquivo de saída JSON (default: report.json)

---

## 🚀 Instalação

```bash
git clone https://github.com/cxiolz/idorbuster.git
cd idorbuster
pip install -r requirements.txt
```

---

## 👨‍💻 Autor

**Caio Luchetti**  
🔗 [LinkedIn](https://www.linkedin.com/in/caio-luchetti/)  
🐙 GitHub: [@cxiolz](https://github.com/cxiolz)

---

## 🧠 Licença

MIT — Faça o que quiser, só não diga que foi você que fez 😎
