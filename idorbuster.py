# idorbuster.py
import typer
import requests
import concurrent.futures
import json
import time

app = typer.Typer()

def print_logo():
    typer.secho(r"""
@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@@   @@@  @@@   @@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@  
@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@ 
@@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  !@@         @@!    @@!       @@!  @@@ 
!@!  !@!  @!@  !@!  @!@  !@!  @!@  !@   @!@  !@!  @!@  !@!         !@!    !@!       !@!  @!@ 
!!@  @!@  !@!  @!@  !@!  @!@!!@!   @!@!@!@   @!@  !@!  !!@@!!      @!!    @!!!:!    @!@!!@!  
!!!  !@!  !!!  !@!  !!!  !!@!@!    !!!@!!!!  !@!  !!!   !!@!!!     !!!    !!!!!:    !!@!@!   
!!:  !!:  !!!  !!:  !!!  !!: :!!   !!:  !!!  !!:  !!!       !:!    !!:    !!:       !!: :!!  
:!:  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!      !:!     :!:    :!:       :!:  !:! 
 ::   :::: ::  ::::: ::  ::   :::   :: ::::  ::::: ::  :::: ::      ::     :: ::::  ::   ::: 
:    :: :  :    : :  :    :   : :  :: : ::    : :  :   :: : :       :     : :: ::    :   : :   
                      by Caio | IDOR Scanner 🔥
""", fg=typer.colors.BRIGHT_GREEN)


def make_request(url, method, headers, id_value):
    try:
        full_url = url.replace("{id}", str(id_value))
        response = requests.request(method, full_url, headers=headers, timeout=10)
        return {
            "id": id_value,
            "status": response.status_code,
            "length": len(response.text),
            "body": response.text[:200]
        }
    except requests.RequestException as e:
        return {
            "id": id_value,
            "error": str(e)
        }


@app.command()
def scan(
    url: str = typer.Option(..., help="URL com {id}"),
    method: str = typer.Option("GET", help="Método HTTP"),
    auth_header: str = typer.Option(None, help="Header de autenticação"),
    cookie: str = typer.Option(None, help="Cookie de sessão"),
    id_range: str = typer.Option(..., help="Intervalo de ID (ex: 1-1000)"),
    concurrency: int = typer.Option(5, help="Número de threads"),
    output: str = typer.Option("report.json", help="Arquivo de saída JSON"),
):
    """Executa o scanner de IDOR na URL informada"""
    print_logo()
    headers = {}
    if auth_header:
        headers["Authorization"] = auth_header
    if cookie:
        headers["Cookie"] = cookie

    id_start, id_end = map(int, id_range.split("-"))
    ids = range(id_start, id_end + 1)
    results = []

    typer.secho(f"[+] Iniciando ataque com {concurrency} threads...", fg="cyan")
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(make_request, url, method, headers, i) for i in ids]
        for future in concurrent.futures.as_completed(futures):
            r = future.result()
            if "error" in r:
                typer.secho(f"[x] ID {r['id']} → ERRO: {r['error']}", fg="red")
            else:
                typer.secho(f"[✓] ID {r['id']} → {r['status']} [{r['length']} bytes]", fg="green")
            results.append(r)

    duration = time.time() - start
    with open(output, "w") as f:
        json.dump(results, f, indent=2)
    typer.secho(f"[✔] Finalizado em {duration:.2f}s | Resultados salvos em {output}", fg="bright_yellow")

if __name__ == "__main__":
    app()
