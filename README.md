# events-framework-template

Plantilla de proxecto para usar o
[events-framework](https://github.com/mDieguezVilas/framework)
como librería externa.

## Uso

1. Clona este repo como base do teu proxecto:

```bash
git clone https://github.com/mDieguezVilas/events-framework-template meu-proxecto
cd meu-proxecto
```

2. Crea o venv e instala as dependencias:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
pip install -e ".[dev]"
```

3. Copia o ficheiro de exemplo de credenciais:

```bash
cp .env.example .env
```

4. Edita `config.yaml` coas túas fontes e `sources/example_source.py`
   coa túa implementación.

5. Verifica que as fontes se detectan:

```bash
framework list-sources
```

6. Executa o ciclo completo:

```bash
framework update
```

## Estrutura

events-framework-template/
├── pyproject.toml          # Dependencia do framework pinneada
├── config.yaml             # Configuración de fontes e notificacións
├── .env.example            # Variables de entorno de exemplo
├── sources/
│   ├── init.py
│   └── example_source.py   # Fonte de exemplo para adaptar
├── event_types/
│   └── example.json        # EventType de exemplo
└── data/
└── .gitkeep

## Actualizar o framework

Para actualizar á última versión do framework edita `pyproject.toml`
e cambia o tag da dependencia:

```toml
dependencies = [
    "events-framework @ git+https://github.com/mDieguezVilas/framework.git@v0.2.0",
]
```

E reinstala:

```bash
pip install -e ".[dev]"
```