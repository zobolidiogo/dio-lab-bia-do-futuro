# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Como Reproduzir o projeto

1. Crie uma pasta e faça download dos diretórios [`data/`](../data) e [`src/`](../src)
2. Instale o Ollama em [ollama.com](https://ollama.com)
   * No site, clique em **Download** para baixar o instalador e execute-o
   * Abra o CMD (Prompt de Comando) e digite:
```bash
ollama list
```
3. Baixe um modelo para uso
   * No site do Ollama, acesse **Models** e escolha o modelo desejado
   * No projeto, o padrão utilizado foi o **phi4-mini**, por ser mais leve
   * Para baixar:
```bash
ollama pull phi4-mini
```
4. Inicie o servidor do Ollama:
```bash
ollama serve
```
> O endereço padrão utilizado pelo projeto é:
> `http://localhost:11434/api/generate`
5. Abra o editor de código e no terminal execute:
```bash
cd src
pip install -r requirements.txt
```
6. No arquivo `app.py`, confirme as variáveis:
```python
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "phi4-mini"
```
7. Execute o projeto:
```bash
streamlit run app.py
```
